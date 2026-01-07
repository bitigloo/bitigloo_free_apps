# -*- coding: utf-8 -*-

from odoo import fields, models


# ---------------------------------------------------------
# Res Config Settings Inheritance
# ---------------------------------------------------------


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    invoice_title_position_selection = fields.Selection(string="Invoice Title Display",
        required=True, default='before', readonly=False,
        related='company_id.invoice_title_position_selection')
