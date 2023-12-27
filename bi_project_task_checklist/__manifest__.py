# Copyright 2023 bitigloo <http://www.bitigloo.com>
# License GPL-3.0 or laterGPL-3 or any later version (https://www.gnu.org/licenses/licenses.html#LicenseURLs).

{
    "name": "Project Task Checklist - bitigloo",
    "version": "16.0.2.0.0",
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
    "images": ['static/description/project_task_checklist_background.png'],
    "installable": True,
    "application": False,
    "license": "GPL-3 or any later version",
    "support": "apps@bitigloo.com"
}
