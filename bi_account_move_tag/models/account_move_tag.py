# -*- coding: utf-8 -*-

from odoo import models, fields


# ----------------------------------------
# This model is for the account move tags
# ----------------------------------------

class AccountMoveTag(models.Model):
    _name = "account.move.tag"
    _description = "Journal Entry Tag"
    _order = "sequence asc"

    sequence = fields.Integer()
    name = fields.Char(string="Tag")
    color = fields.Integer()
