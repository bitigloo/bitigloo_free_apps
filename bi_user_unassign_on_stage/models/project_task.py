# -*- coding: utf-8 -*-

from odoo import models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def write(self, vals):
        res = super(ProjectTask, self).write(vals)
        stage = self.stage_id

        unassign_actions = {
            'self': [(3, user_id) for user_id in self.user_ids.ids if self.env.uid == user_id],
            'all': [(5,)],
            'specific': [(3, user_id) for user_id in stage.users_to_unassign.ids if user_id in self.user_ids.ids]
        }

        if self.user_ids and stage:
            action = unassign_actions.get(stage.unassign)
            if action:
                self.user_ids = action
        return res
