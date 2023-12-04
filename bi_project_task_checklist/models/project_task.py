# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    checklist_template_id = fields.Many2one('checklist.template', string="Checklist Template")
    checklist_ids = fields.One2many('checklist', 'task_id', string='Checklist')

    @api.model
    def create(self, vals):
        sol_id = vals.get('sale_line_id')
        if sol_id:
            sol = self.env['sale.order.line'].browse(sol_id)
            checklist_template_id = sol.product_id.product_tmpl_id.checklist_template_id.id
            if checklist_template_id:
                vals['checklist_template_id'] = checklist_template_id
        res = super(ProjectTask, self).create(vals)
        res.update_task_checklist_ids()
        return res

    @api.onchange('checklist_template_id')
    def update_task_checklist_ids(self):
        if self.checklist_template_id:
            checklist_ids = [(5, 0, 0)] + [(0, 0, {'description': item.item_description}) for item in self.checklist_template_id.item_ids]
            self.checklist_ids = checklist_ids

    def write(self, vals):
        res = super(ProjectTask, self).write(vals)
        if 'stage_id' in vals:
            if self.stage_id.block_on_checklist and not all(self.checklist_ids.mapped('checkbox')):
                raise UserError(_("All the checklist items must be done before moving to the next stage"))
        return res
