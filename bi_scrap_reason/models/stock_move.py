# -*- coding: utf-8 -*-

from odoo import models, fields


# --------------------------------------------------------------------
# This model adds new fields on stock.move to select reasons on Move
# --------------------------------------------------------------------

class StockMove(models.Model):
    _inherit = "stock.move"

    reason_id = fields.Many2one(
        "stock.scrap.reason",
        context={'_order': 'sequence asc'}
    )
    note = fields.Text()