# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return

    _logger.info("Migrating stock.scrap fields reason_id & note to stock.move...")
    cr.execute("""
        UPDATE stock_move AS sm
           SET reason_id = ss.reason_id,
               note = ss.note
          FROM stock_scrap AS ss
         WHERE sm.scrap_id = ss.id
           AND (ss.reason_id IS NOT NULL OR ss.note IS NOT NULL)
    """)
    _logger.info("Successfully copied reason_id & note values to stock.move.")
