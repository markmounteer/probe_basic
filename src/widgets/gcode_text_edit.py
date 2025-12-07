from qtpy.QtCore import Slot
from qtpyvcp.widgets.input_widgets.gcode_text_edit import GcodeTextEdit as _BaseGcodeTextEdit


class GcodeTextEdit(_BaseGcodeTextEdit):
    """G-code editor widget with a slot to toggle editability."""

    @Slot(bool)
    def EditorReadWrite(self, enabled: bool) -> None:
        """Switch the widget between read-only and read-write modes.

        Parameters
        ----------
        enabled: bool
            ``True`` to allow editing, ``False`` to make the editor read-only.
        """

        self.setReadOnly(not enabled)
