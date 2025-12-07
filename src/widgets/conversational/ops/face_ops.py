from textwrap import dedent


class FaceOps:
    def __init__(self):
        self.wcs = None
        self.coolant = None
        self.units = None
        self.tool_number = None
        self.spindle_rpm = None
        self.spindle_dir = None
        self.z_clear = None
        self.z_start = None
        self.z_end = None
        self.retract = None
        self.z_feed = None

        self.tool_diameter = None
        self.x_start = None
        self.x_end = None
        self.y_start = None
        self.y_end = None
        self.step_down = None
        self.step_over = None

    def _header(self):
        return dedent(
            f"""( Conversational operation: FACE )
            ( WCS: {self.wcs or 'G54'} )
            ( Units: {self.units or 'MM'} )
            ( Tool: {self.tool_number or 0}  Dia: {self.tool_diameter or 0} )
            ( Spindle: {self.spindle_dir or 'CW'} @ {self.spindle_rpm or 0} )
            ( Coolant: {self.coolant or 'OFF'} )
            ( Clearance: {self.z_clear or 0} )
            ( Z start: {self.z_start or 0}  Z end: {self.z_end or 0} )
            ( Retract height: {self.retract or 0} )
            ( Z feed: {self.z_feed or 0} )
            ( Step over: {self.step_over or 0}  Step down: {self.step_down or 0} )
            ( X: {self.x_start or 0} -> {self.x_end or 0} )
            ( Y: {self.y_start or 0} -> {self.y_end or 0} )
            """
        ).strip()

    def face(self):
        return "\n".join([self._header(), "( Facing path placeholder )"])

