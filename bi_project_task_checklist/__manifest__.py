# Copyright 2024 bitigloo <http://www.bitigloo.com>
{
    "name": "Project Task Checklist - bitigloo GmbH",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "summary": "Module Customizations for project app, to add checklist on the tasks",
    "description": """Some Customizations for project app, to add checklist on the tasks""",
    "author": "bitigloo GmbH",
    "website": "https://www.bitigloo.com",
    "depends": ["project", "sale", "sale_project", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/checklist_views.xml",
        "views/task_form_views.xml",
        "views/checklist_template_views.xml",
        "views/product_template_form_views.xml",
        "views/task_type_edit_views.xml",
    ],
    "images": ['static/description/background.png'],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
    "support": "apps@bitigloo.com"
}
