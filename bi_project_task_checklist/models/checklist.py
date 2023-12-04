# -*- coding: utf-8 -*-

from odoo import fields, models


class Checklist(models.Model):
    _name = 'checklist'
    _description = 'Checklist'

    description = fields.Char(string='Description', required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    checkbox = fields.Boolean(string='Done', default=False)
    task_id = fields.Many2one('project.task', string='Task')
    project_id = fields.Many2one(related='task_id.project_id', string='Project', store=True)
    assignee_ids = fields.Many2many(string='Assignees', related='task_id.user_ids')
    task_stage_id = fields.Many2one(related='task_id.stage_id', string='Task Stage', store=True)
