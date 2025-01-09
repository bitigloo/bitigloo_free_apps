# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    unassign = fields.Selection(
        [('self', 'Self'), ('all', 'All'), ('specific', 'Specific User')],
        string="Unassign"
    )
    users_to_unassign = fields.Many2many(
        'res.users',
        'project_task_type_unassign_partner_rel',
        'task_type_unassign_id',
        'partner_id',
        string="Unassign Users"
    )
