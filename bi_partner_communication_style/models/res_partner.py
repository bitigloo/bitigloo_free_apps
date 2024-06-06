from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"
    
    communication_style = fields.Selection([
        ('formal', 'Formal'),
        ('informal', 'Informal')],
        default="formal",
        help="You can use this field to identify how to communicate with the partner, e.g. dynamically on the reports or email templates.")
    