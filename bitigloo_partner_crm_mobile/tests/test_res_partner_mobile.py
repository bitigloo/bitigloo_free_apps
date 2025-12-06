from odoo.tests.common import TransactionCase, tagged
from odoo.addons.bitigloo_partner_crm_mobile.hooks import post_init_hook

@tagged('post_install', '-at_install')
class TestResPartnerMobile(TransactionCase):

    def test_mobile_field(self):
        """Test that the mobile field can be set and retrieved."""
        partner = self.env['res.partner'].create({
            'name': 'Test Partner',
            'mobile': '+1234567890',
        })
        self.assertEqual(partner.mobile, '+1234567890')

    def test_mobile_search(self):
        """Test that searching by mobile number works."""
        partner = self.env['res.partner'].create({
            'name': 'Search Partner',
            'mobile': '+9876543210',
        })
        # The phone_validation module adds phone_mobile_search
        # We check if searching on phone_mobile_search finds the partner via mobile
        found_partner = self.env['res.partner'].search([('phone_mobile_search', '=', '+9876543210')])
        self.assertIn(partner, found_partner)

    def test_post_init_hook_logic(self):
        """Test the logic of the post_init_hook."""
        # Create a partner without mobile
        partner = self.env['res.partner'].create({
            'name': 'Migration Partner',
        })
        
        # Create a message with the pattern
        self.env['mail.message'].create({
            'model': 'res.partner',
            'res_id': partner.id,
            'body': '<p>Some text</p><p>Previous Mobile: +1122334455</p>',
            'message_type': 'comment',
        })

        # Run the hook logic manually
        post_init_hook(self.env)

        # Check if mobile was updated
        self.assertEqual(partner.mobile, '+1122334455')

    def test_post_init_hook_existing_mobile(self):
        """Test that post_init_hook does not overwrite existing mobile."""
        partner = self.env['res.partner'].create({
            'name': 'Existing Mobile Partner',
            'mobile': '+999999999',
        })
        
        self.env['mail.message'].create({
            'model': 'res.partner',
            'res_id': partner.id,
            'body': 'Previous Mobile: +111111111',
        })

        post_init_hook(self.env)

        # Should still be the original mobile
        self.assertEqual(partner.mobile, '+999999999')

    def test_crm_mobile_field(self):
        """Test that the mobile field can be set and retrieved on crm.lead."""
        lead = self.env['crm.lead'].create({
            'name': 'Test Lead',
            'mobile': '+1234567890',
        })
        self.assertEqual(lead.mobile, '+1234567890')

    def test_crm_mobile_search(self):
        """Test that searching by mobile number works for crm.lead."""
        lead = self.env['crm.lead'].create({
            'name': 'Search Lead',
            'mobile': '+9876543210',
        })
        # The phone_validation module adds phone_mobile_search
        # We check if searching on phone_mobile_search finds the lead via mobile
        found_lead = self.env['crm.lead'].search([('phone_mobile_search', '=', '+9876543210')])
        self.assertIn(lead, found_lead)

    def test_crm_post_init_hook_logic(self):
        """Test the logic of the post_init_hook for crm.lead."""
        # Create a lead without mobile
        lead = self.env['crm.lead'].create({
            'name': 'Migration Lead',
        })
        
        # Create a message with the pattern
        self.env['mail.message'].create({
            'model': 'crm.lead',
            'res_id': lead.id,
            'body': '<p>Some text</p><p>Previous Mobile: +1122334455</p>',
            'message_type': 'comment',
        })

        # Run the hook logic manually
        post_init_hook(self.env)

        # Check if mobile was updated
        self.assertEqual(lead.mobile, '+1122334455')

