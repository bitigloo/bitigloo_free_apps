# -*- coding: utf-8 -*-

from odoo import fields, models

# ---------------------------------------------------------
# Invoice Title Model
# ---------------------------------------------------------


class InvoiceTitle(models.Model):
    _name = "invoice.title"
    _description = "Invoice Titles"
    _order = "name"

    name = fields.Char(string="Invoice Title", required=True, translate=True)
    invoice_note = fields.Html('Note')
