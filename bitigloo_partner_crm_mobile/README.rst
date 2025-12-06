==================================================================
Bring Back Mobile Number on Partner (Contact) and Lead/Opportunity
==================================================================

This module brings back the **Mobile** number field on the Partner (Contact) and Lead/Opportunity in Odoo 19, which was removed in the standard version.

Features
========

*   **Restores Mobile Field**: Adds the ``mobile`` field back to the ``res.partner`` and ``crm.lead`` model and views.
*   **Data Migration**: Includes a post-init script that checks for messages containing "Previous Mobile: {number}" (created by Odoo during upgrade) and automatically populates the restored mobile field with this data.
*   **Search Integration**: Ensures the mobile number is included in the phone/mobile search logic (via ``phone_validation`` dependency).
*   **UI Integration**: Places the mobile field with a mobile icon directly below the phone field, consistent with previous Odoo versions.

Table of contents
~~~~~~~~~~~~~~~~~

.. contents::
   :local:

Installation
============

Install the module normally. The post-init hook will automatically run to migrate any existing mobile numbers found in the chatter messages.

Configuration
=============

No specific configuration is required.

Usage
=====

*   Go to **Contacts**.
*   Open any contact form.
*   You will see the **Mobile** field below the **Phone** field.

*   Go to **Leads & Opportunities**.
*   Open any lead form.
*   You will see the **Mobile** field below the **Phone** field.

Credits
=======

Authors
-------

* bitigloo GmbH <https://github.com/bitigloo>

Maintainers
-----------

This module is maintained by bitigloo GmbH (https://www.bitigloo.com).

.. image:: https://www.bitigloo.com/web/image/website/1/favicon
   :alt: bitigloo GmbH
   :target: https://www.bitigloo.com
   :width: 10%

bitigloo GmbH is a certified Odoo partner in Germany.

License
=======

This module is under the license "LGPL-3".