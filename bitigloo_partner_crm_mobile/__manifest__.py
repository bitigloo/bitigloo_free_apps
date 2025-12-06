# Copyright 2024 bitigloo <http://www.bitigloo.com>

{
    "name": "Restore Mobile Field on Partner (Contact) and Lead/Opportunity with Upgrade Script - bitigloo GmbH",
    "version": "19.0.1.0",
    "category": "Contact/Partner,CRM",
    "author": "bitigloo GmbH",
    "summary": "Restore Mobile Field on Partner (Contact) and Lead/Opportunity with Upgrade Script",
    "description": """
Bring Back Mobile Number on Partner (Contact) and Lead/Opportunity after Odoo 19 migration/upgrade
==================================================================================================

This module brings back the mobile number field on partner (contact) as well as on lead/opportunity after Odoo 19 migration/upgrade. It also adds a script to migrate the mobile number from the message on the contact to the new field after the migration/upgrade. Besides, it also adjusts the computed function for search_phone_mobile to include the newly added mobile field.
""",
    "depends": [
        "phone_validation",
        "crm",
    ],
    "data": [
        "views/res_partner_views.xml",
        "views/crm_lead_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "website": "https://www.bitigloo.com",
    "images": ['static/description/background_v18.png'],
    "license": "LGPL-3",
    "support": "apps@bitigloo.com",
}
