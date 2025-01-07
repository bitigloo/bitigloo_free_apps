# Copyright 2024 bitigloo <http://www.bitigloo.com>

{
    "name": "Add Scrap Reason & Note - bitigloo",
    "version": "18.0.1.0",
    "category": "Inventory",
    "author": "bitigloo GmbH",
    "summary": "Select a reason and add a note on Scrap",
    "description": """
It makes it possible to select a reason and add a note on Scrap.
================================================================

This module makes it possible to defined some reasons in the configurations and
then on Scrap wizard or form view, we can select the reason for Scrap. Besides,
it adds a Note field on those views.
""",
    "depends": [
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_scrap_views.xml",
        "views/stock_scrap_reason_views.xml",
    ],
    "installable": True,
    "website": "https://www.bitigloo.com",
    "images": ['static/description/background.png'],
    "license": "LGPL-3",
    "support": "apps@bitigloo.com",
}
