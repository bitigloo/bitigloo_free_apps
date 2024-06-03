# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ChecklistTemplateItems(models.Model):
    _name = 'checklist.template.items'
    _description = 'Checklist Template Items'

    item_description = fields.Char(_('Checklist Item Description'), required=True)
    checklist_template = fields.Many2one('checklist.template', string=_("Checklist Templates"))
    sequence = fields.Integer(default=10)
