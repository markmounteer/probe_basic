"""Manual tool change dialog implementation."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from qtpy import uic
from qtpy.QtWidgets import QDialog


class ToolChangeDialog(QDialog):
    """Simple dialog to prompt the operator for a manual tool change.

    Parameters
    ----------
    ui_file: str | Path | None
        Path to the Qt Designer ``.ui`` file defining the dialog layout.
    parent: QWidget | None
        Optional parent widget.
    """

    def __init__(self, ui_file: Optional[Path] = None, parent=None):
        super().__init__(parent)

        if ui_file is not None:
            ui_path = Path(ui_file)
            if ui_path.is_file():
                uic.loadUi(str(ui_path), self)
            else:
                raise FileNotFoundError(f"Tool change dialog UI not found: {ui_path}")

    def set_tool_info(self, tool_number: int, remark: str | None = None):
        """Populate the dialog with tool information."""

        if hasattr(self, "lblToolNumber"):
            self.lblToolNumber.setText(str(tool_number))

        if remark is not None and hasattr(self, "lblToolRemark"):
            self.lblToolRemark.setText(remark)
