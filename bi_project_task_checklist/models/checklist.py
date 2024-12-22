# -*- coding: utf-8 -*-

from odoo import fields, models


class Checklist(models.Model):
    _name = 'checklist'
    _description = 'Checklist'

    description = fields.Char(required=True)
    note = fields.Char()
    sequence = fields.Integer(default=10)
    checkbox = fields.Boolean(string='Done', default=False)
    task_id = fields.Many2one('project.task')
    project_id = fields.Many2one(related='task_id.project_id', store=True)
    assignee_ids = fields.Many2many(string='Assignees', related='task_id.user_ids')
    task_stage_id = fields.Many2one(related='task_id.stage_id', store=True)
