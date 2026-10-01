from odoo import api, fields, models

class CRMLead(models.Model):

    _inherit = 'crm.lead'

    mobile = fields.Char(tracking=True)
    mobile_sanitized = fields.Char(
        string="Sanitized Mobile Number",
        compute="_compute_mobile_sanitized",
        compute_sudo=True,
        store=True,
    )
    mobile_formatted = fields.Char(
        string="Formatted Mobile Number",
        compute="_compute_mobile_formatted",
        export_string_translation=False,
    )

    @api.depends("mobile", "country_id")
    def _compute_mobile_sanitized(self):
        """Store each mobile number in normalized format."""
        for lead in self:
            lead.mobile_sanitized = lead._phone_format(fname="mobile") or False

    @api.depends("mobile_sanitized")
    def _compute_mobile_formatted(self):
        """Prepare the international display value used by the mobile widget."""
        for lead in self:
            lead.mobile_formatted = lead._phone_get_formatted(lead.mobile_sanitized)

    @api.model
    def _phone_get_phone_mobile_search_fields(self):
        """Include normalized mobile values in generic phone searches."""
        fields_to_search = super()._phone_get_phone_mobile_search_fields()
        if "mobile_sanitized" not in fields_to_search:
            fields_to_search.append("mobile_sanitized")
        return fields_to_search
