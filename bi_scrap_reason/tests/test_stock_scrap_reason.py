# Copyright 2023 bitigloo <http://www.bitigloo.com>
# License GPL-3.0 or laterGPL-3 or any later version (https://www.gnu.org/licenses/licenses.html#LicenseURLs).

from odoo.tests.common import TransactionCase


class TestStockScrapReason(TransactionCase):
    def setUp(self):
        super(TestStockScrapReason, self).setUp()
        self.ScrapReason = self.env['stock.scrap.reason']

    def create_product(self, name):
        return self.env['product.product'].create({'name': name})

    def create_product_category_uom(self, name):
        return self.env['uom.category'].create({'name': name})

    def create_product_uom(self, name, category_id):
        return self.env['uom.uom'].create({
            'name': name,
            'category_id': category_id
        })

    def create_scrap_order(self, reason, product, product_uom, category_uom, state):
        return self.env['stock.scrap'].create({
            'reason_id': reason.id,
            'product_id': product.id,
            'product_uom_id': product_uom.id,
            'product_uom_category_id': category_uom.id,
            'state': state
        })

    def test_compute_scrap_order_count(self):
        # Create a product category uom
        product_category_uom = self.create_product_category_uom("Test category uom")

        # Create a product uom with the category
        product_uom = self.create_product_uom("Test Uom", product_category_uom.id)

        # Create a scrap reason
        reason = self.ScrapReason.create({'name': 'Test Reason'})

        # Create scrap orders associated with the reason
        self.create_scrap_order(reason, self.create_product("Test Product"), product_uom, product_category_uom, 'done')
        self.create_scrap_order(reason, self.create_product("Test Product"), product_uom, product_category_uom, 'done')
        self.create_scrap_order(reason, self.create_product("Test Product"), product_uom, product_category_uom, 'draft')

        # Trigger the computation method
        reason._compute_scrap_order_count()

        # Check if scrap_order_count is correctly computed
        self.assertEqual(reason.scrap_order_count, 2, "Scrap order count should be 2")

    def test_action_see_scrap_orders(self):
        # Create a product category uom
        product_category_uom = self.create_product_category_uom("Test category uom")

        # Create a product uom with the category
        product_uom = self.create_product_uom("Test Uom", product_category_uom.id)

        # Create a scrap reason
        reason = self.ScrapReason.create({'name': 'Test Reason'})

        # Create scrap orders associated with the reason
        scrap1 = self.create_scrap_order(reason, self.create_product("Test Product"), product_uom, product_category_uom,
                                         'done')
        scrap2 = self.create_scrap_order(reason, self.create_product("Test Product"), product_uom, product_category_uom,
                                         'done')

        # Call the action
        action = reason.action_see_scrap_orders()

        # Get the domains and sort them for comparison
        expected_domain = [('id', 'in', [scrap2.id, scrap1.id])]
        actual_domain = action['domain']

        # Check if the sorted lists are equal
        self.assertEqual(expected_domain, actual_domain, "Domain should be the same")
