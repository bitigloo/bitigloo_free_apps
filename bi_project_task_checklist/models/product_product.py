# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    checklist_template_id = fields.Many2one(
        related='product_tmpl_id.checklist_template_id',
        string='Checklist Template',
    )
