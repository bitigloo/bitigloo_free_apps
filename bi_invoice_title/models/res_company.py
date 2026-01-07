from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    invoice_title_position_selection = fields.Selection([
        ('before', 'Before'),
        ('replace', 'Replace'),
        ('after', 'After')], string="Invoice Title Display",
        required=True, default='before'
    )