# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def _create_stock_move(self, location_dest_id, qty):
        move = self.env["stock.move"].create(
            {
                "name": "Stock move in",
                "location_id": self.supplier_location.id,
                "location_dest_id": location_dest_id.id,
                "product_id": self.product.id,
                "product_uom": self.product.uom_id.id,
                "product_uom_qty": qty,
            }
        )
        move._action_confirm()
        move._action_assign()
        for move_line in move.move_line_ids:
            move_line.quantity = qty
            move_line.picked = True
        move._action_done()
        return move
