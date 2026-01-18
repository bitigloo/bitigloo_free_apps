from odoo import models, fields

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    mobile = fields.Char(tracking=True)
