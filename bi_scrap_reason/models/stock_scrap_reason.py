# -*- coding: utf-8 -*-

from odoo import models, fields


# ---------------------------------------------------------------------
# This model is for the scrap reasons
# ---------------------------------------------------------------------

class StockScrapReason(models.Model):
    _name = "stock.scrap.reason"
    _description = "Stock Scrap Reason"
    _order = "sequence asc"

    sequence = fields.Integer()
    name = fields.Char(string="Reason")
    scrap_order_count = fields.Integer(compute="_compute_scrap_order_count")

    def _compute_scrap_order_count(self):
        # Calculate the count of scrap orders for each reason using read_group
        scraps_data = self.env['stock.scrap']._read_group(
            domain=[('reason_id', 'in', self.ids), ('state', '=', 'done')],
            groupby=['reason_id'],
            aggregates=['__count']
        )
        counts = {reason.id: count for reason, count in scraps_data}
        for reason in self:
            reason.scrap_order_count = counts.get(reason.id, 0)

    def action_see_scrap_orders(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("stock.action_stock_scrap")
        scraps = self.env['stock.scrap'].search([
            ('reason_id', '=', self.id),
            ('state', '=', 'done')]
        )
        action['domain'] = [('id', 'in', scraps.ids)]
        action['context'] = dict(self.env.context, create=False)
        return action
