from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

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

    @api.model
    def _phone_get_number_fields(self):
        """Keep the standard phone companion fields tied to ``phone``."""
        return [
            field_name
            for field_name in super()._phone_get_number_fields()
            if field_name != "mobile"
        ]

    @api.depends("mobile", "country_id")
    def _compute_mobile_sanitized(self):
        """Store each mobile number in normalized format."""
        for partner in self:
            partner.mobile_sanitized = partner._phone_format(fname="mobile") or False

    @api.depends("mobile_sanitized")
    def _compute_mobile_formatted(self):
        """Prepare the international display value used by the mobile widget."""
        for partner in self:
            partner.mobile_formatted = partner._phone_get_formatted(
                partner.mobile_sanitized
            )

    @api.model
    def _phone_get_phone_mobile_search_fields(self):
        """Include normalized mobile values in generic phone searches."""
        fields_to_search = super()._phone_get_phone_mobile_search_fields()
        for field_name in ("mobile", "mobile_sanitized"):
            if field_name not in fields_to_search:
                fields_to_search.append(field_name)
        return fields_to_search
