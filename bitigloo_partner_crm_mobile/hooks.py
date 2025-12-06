from odoo import api, SUPERUSER_ID
import re

def post_init_hook(env):
    """
    Check the message on the res.partner records and add the removed mobile number 
    from the message to the related partner.
    """
    # Search for messages containing "Previous Mobile:" linked to res.partner
    messages = env['mail.message'].search([
        ('model', 'in', ['res.partner', 'crm.lead']),
        ('body', 'ilike', 'Previous Mobile:')
    ])
    
    for message in messages:
        if message.model == 'res.partner':
            partner = env['res.partner'].browse(message.res_id)
            lead = None
        elif message.model == 'crm.lead':
            lead = env['crm.lead'].browse(message.res_id)
            partner = None
        if (partner and not partner.mobile) or (lead and not lead.mobile):
            # Extract mobile number from body
            # Body is HTML, so we use regex to find the pattern
            # Pattern: "Previous Mobile: {mobile_number}"
            # We capture characters that are typical in phone numbers
            match = re.search(r'Previous Mobile:\s*([+\d\s\-\(\)]+)', message.body)
            if match:
                mobile = match.group(1).strip()
                # Basic cleanup to remove potential trailing HTML tags if regex was too greedy
                # (though the character class should prevent matching < or >)
                if mobile:
                    partner.write({'mobile': mobile}) if partner else lead.write({'mobile': mobile})
