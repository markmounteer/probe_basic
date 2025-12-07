import os
from pathlib import Path


class GCodeFile:
    """Simple container for conversational operations.

    The real qtpyvcp helper offers richer behaviour. This lightweight
    implementation only supports collecting the generated operation strings
    and writing them to disk.
    """

    def __init__(self):
        self.ops = []

    def write_to_file(self, path):
        """Write the collected operations to ``path``.

        Each operation is separated by a blank line to keep the output readable.
        The target directory is created if it does not already exist.
        """

        Path(os.path.dirname(path) or ".").mkdir(parents=True, exist_ok=True)
        payload = "\n\n".join(op for op in self.ops if op)
        with open(path, "w", encoding="utf-8") as gcode_file:
            gcode_file.write(payload)

