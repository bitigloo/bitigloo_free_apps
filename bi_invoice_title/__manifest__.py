# Copyright 2023 bitigloo <http://www.bitigloo.com>
# License GPL-3.0 or laterGPL-3 or any later version (https://www.gnu.org/licenses/licenses.html#LicenseURLs).

{
    "name": "Invoice Title - bitigloo",
    "version": "16.0.1.0.0",
    "category": "Accounting",
    "author": "bitigloo GmbH",
    "summary": "It adds a title to the invoice (form and report).",
    "website": "https://www.bitigloo.com",
    "depends": ["account", "l10n_din5008"],
    "data": [
        "security/ir.model.access.csv",
        "views/invoice_title_views.xml",
        "views/account_move_views.xml",
        "views/res_config_settings_views.xml",
        "report/report_invoice.xml",
    ],
    "installable": True,
    "images": ['static/description/invoice_title_background.png'],
    "application": False,
    "license": "LGPL-3",
    "support": "apps@bitigloo.com"
}
