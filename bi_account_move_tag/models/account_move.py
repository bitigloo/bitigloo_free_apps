# -*- coding: utf-8 -*-

from odoo import models, fields

class AccountMove(models.Model):
    _inherit = "account.move"

    tag_ids = fields.Many2many(
        "account.move.tag",
        string="Tags",
        context={'_order': 'sequence asc'}
    )
