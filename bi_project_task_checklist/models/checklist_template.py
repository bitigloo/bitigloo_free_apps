# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ChecklistTemplate(models.Model):
    _name = 'checklist.template'
    _description = 'Checklist Template'

    name = fields.Char('Template Name', required=True)
    item_ids = fields.One2many('checklist.template.items', 'checklist_template', string='Checklist Items')
    available_on_product = fields.Boolean(string='Available on Product?', default=True)
