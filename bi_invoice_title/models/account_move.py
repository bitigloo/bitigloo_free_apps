# -*- coding: utf-8 -*-

from odoo import api, fields, models


# ---------------------------------------------------------
# Account Move Inheritance
# ---------------------------------------------------------


class AccountMove(models.Model):
    _inherit = "account.move"

    invoice_title = fields.Many2one("invoice.title", string="Invoice Title")
    invoice_note = fields.Html("Note")
    is_layout_to_print = fields.Boolean(default=True)

    @api.onchange('invoice_title')
    def onchange_invoice_note(self):
        self.ensure_one()
        if self.invoice_title:
            self.write({'invoice_note': self.invoice_title.invoice_note})

    def _get_invoice_title(self):
        invoice_title_position = self.env['ir.config_parameter'].get_param(
            'bi_invoice_title.invoice_title_position_selection', False
        )
        return invoice_title_position

