"""Compatibility helpers for the qtpyvcp MDIHistory widget."""

from __future__ import annotations

import logging
from typing import Any

from qtpy.QtWidgets import QListWidget

LOG = logging.getLogger(__name__)


def _patch_remove_all(cls: type[Any]) -> bool:
    """Attach a ``removeAll`` slot to *cls* if it is missing."""

    if hasattr(cls, "removeAll"):
        return False

    def removeAll(self: Any) -> None:  # noqa: N802 - PyQt slot naming convention
        history_manager = getattr(self, "history_manager", None)
        clear_history = getattr(history_manager, "clear", None)
        if callable(clear_history):
            clear_history()
        # ``clear`` is provided by the underlying ``QListWidget``.
        self.clear()

    cls.removeAll = removeAll
    return True


def ensure_mdihistory_remove_all() -> None:
    """Ensure the ``MDIHistory`` widget exposes a ``removeAll`` slot.

    Some versions of ``qtpyvcp`` ship ``MDIHistory`` without a ``removeAll``
    method even though the UI files connect a button click to that slot. When
    the method is missing, the UI loader raises an ``AttributeError`` and the
    application fails to start. This helper adds a lightweight implementation
    that clears both the widget contents and any attached history manager if
    the slot is absent. The patch also falls back to the ``QListWidget`` base
    class to cover environments where ``MDIHistory`` cannot be imported.
    """

    try:
        from qtpyvcp.widgets.input_widgets.mdihistory_widget import MDIHistory
    except Exception as exc:  # pragma: no cover - defensive logging
        LOG.debug("Unable to import MDIHistory for patching", exc_info=exc)
    else:
        if _patch_remove_all(MDIHistory):
            LOG.info("Patched MDIHistory with missing removeAll slot")
            return

    if _patch_remove_all(QListWidget):
        LOG.info("Patched QListWidget with missing removeAll slot as fallback")
