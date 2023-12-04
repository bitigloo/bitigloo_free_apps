# -*- coding: utf-8 -*-

from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    block_on_checklist = fields.Boolean(string="Block On Checklist",
                                        help="If checked we cannot go to this stage until the whole checklist on the task is done.")
