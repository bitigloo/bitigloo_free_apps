# -*- coding: utf-8 -*-

from odoo import fields, models


class ChecklistTemplateItems(models.Model):
    _name = 'checklist.template.items'
    _description = 'Checklist Template Items'

    item_description = fields.Char('Checklist Item Description', required=True)
    checklist_template = fields.Many2one('checklist.template', string="Checklist Templates")
    sequence = fields.Integer(string="Sequence", default=10)
