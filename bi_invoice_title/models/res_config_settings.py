# -*- coding: utf-8 -*-

from odoo import fields, models


# ---------------------------------------------------------
# Res Config Settings Inheritance
# ---------------------------------------------------------


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    invoice_title_position_selection = fields.Selection([
        ('before', 'Before'),
        ('replace', 'Replace'),
        ('after', 'After')], string="Invoice Title Display",
        required=True, default='before',
        config_parameter='bi_invoice_title.invoice_title_position_selection')
