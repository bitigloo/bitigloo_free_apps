# -*- coding: utf-8 -*-

from odoo import fields, models


# ---------------------------------------------------------
# Project Task Stage Inheritance
# ---------------------------------------------------------


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    activity_type = fields.Many2one(
        "mail.activity.type", string="Activity Type",
        domain=lambda self: ['|', ('res_model', '=', False),
                             ('res_model', '=', 'project.project')]
    )
    specific_user = fields.Many2one("res.users", string="Specific User",
                                    domain=lambda self: [('share', '=', False)])
    user_type = fields.Selection(
        [
            ('project_manager', 'Project Manager'),
            ('specific_user', 'Specific User')
        ],
        string="User Type"
    )
