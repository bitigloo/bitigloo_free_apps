# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_check_template_with_available_on_product(self):
        check_list_obj = self.env['checklist.template'].search([])
        return [('available_on_product', '=', True) for item in check_list_obj]

    checklist_template_id = fields.Many2one(
        'checklist.template',
        string='Checklist Template',
        domain=lambda self: self._get_check_template_with_available_on_product()
    )
