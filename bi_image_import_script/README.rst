=====================
Image Import Script
=====================

This script was written to make it possible to import images into Odoo.

**Features:**
  * simply converts the images in a suitable language for Odoo binary field.
  * you can run the script multiple times and add new rows to your csv file.

How to Use:
===========

To use this script, you need to first have python installed, then:

#. copy the directory where all your images are located; the images can be in
   subdirectories as well.
#. add the directory path into the script for 'image_directory' field
#. copy the directory where the csv file should be created or where your current csv
   file is located.
#. add the directory path into the sript for 'csv_directory' field
#. run the script and that's it; the script will generate a csv file which can be
   imported into Odoo easily.
#. for importing the images of already exisiting products in the system, a developer or
   a technical person can easily map the names of the image files with the external ids
   of the records in Odoo.

**Best Practice:**
   * If the images names are the external ids of the products, then it will be super easy


Feedback & Issues
=================

In case of feedback or any possible issues, this can be reported through submitting this
form https://www.bitigloo.com/r/rYu or via an email to apps@bitigloo.com.
If you like it, please give us a rating on our product page (https://www.bitigloo.com/r/zjj).

Credits
=======

Authors
-------

* bitigloo GmbH <https://github.com/bitigloo>

Maintainers
-----------

This module is maintained by bitigloo GmbH (https://www.bitigloo.com/r/bw4). Check out our 
products (https://www.bitigloo.com/r/zjj) and services (https://www.bitigloo.com/r/Lzo).

.. image:: ./static/description/icon.png
   :alt: bitigloo GmbH, Odoo Partner in Bonn, NRW, Germany
   :target: https://www.bitigloo.com/r/bw4
   :width: 10%

bitigloo GmbH is a certified Odoo partner in Germany which enjoys the expertise of a
team of proficient Odoo experts with years of experience in finding the best ERP
solutions for various businesses, tailoring them to their specific needs, and
implementing them in the most effective way.

License
=======

This module is under the license "GPL-3 or any later version":
https://www.gnu.org/licenses/licenses.html#LicenseURLs