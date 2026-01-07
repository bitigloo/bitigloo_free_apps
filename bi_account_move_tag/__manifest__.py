# Copyright 2024 bitigloo <http://www.bitigloo.com>

{
    "name": "Invoice & Bill Tags (all Journal Entry types) - bitigloo GmbH",
    "version": "19.0.1.0",
    "category": "Invoicing",
    "author": "bitigloo GmbH",
    "summary": "Add Tag to invoice, bill or any other journal entry types",
    "description": """
It makes it possible to add a tag to any type of journal entry.
================================================================

This module makes it possible to add a tag to any type of journal entry,
i.e. invoice, bill, credit note, refund bill, entry, etc.
""",
    "depends": [
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_views.xml",
        "views/account_move_tag_views.xml",
    ],
    "installable": True,
    "website": "https://www.bitigloo.com",
    "images": ['static/description/background_v18.png'],
    "license": "LGPL-3",
    "support": "apps@bitigloo.com",
}
