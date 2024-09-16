# -*- coding: utf-8 -*-

from odoo import fields, models, _

# ---------------------------------------------------------
# Invoice Title Model
# ---------------------------------------------------------


class InvoiceTitle(models.Model):
    _name = "invoice.title"
    _description = "Invoice Titles"
    _order = "name"

    name = fields.Char(string=_("Invoice Title"), required=True, translate=True)
    invoice_note = fields.Html(_('Note'))
