# -*- coding: utf-8 -*-

from odoo import models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def write(self, values):
        res = super(ProjectTask, self).write(values)
        if values.get('stage_id'):
            stage = self.stage_id
            if stage.activity_type:
                activity_type_id = stage.activity_type.id
                activity_vals = {
                    'res_id': self.id,
                    'res_model_id': self.env['ir.model'].sudo().search([('model', '=', 'project.task')]).id,
                    'activity_type_id': activity_type_id,
                }

                if stage.user_type == 'specific_user' and stage.specific_user:
                    activity_vals['user_id'] = stage.specific_user.id
                elif stage.user_type == 'project_manager' and self.manager_id:
                    activity_vals['user_id'] = self.manager_id.id

                if 'user_id' in activity_vals:
                    self.env['mail.activity'].sudo().create(activity_vals)

        return res
