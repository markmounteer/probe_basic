import math
from textwrap import dedent


class DrillOps:
    def __init__(self):
        self.holes = []
        self.retract_mode = "G98"
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

    def add_hole(self, x, y):
        self.holes.append([float(x), float(y)])

    def add_hole_circle(self, num_holes, circle_diam, circle_center, start_angle=0):
        radius = circle_diam / 2.0
        cx, cy = circle_center
        for idx in range(int(num_holes)):
            angle_rad = math.radians(start_angle + (360.0 / num_holes) * idx)
            x = cx + radius * math.cos(angle_rad)
            y = cy + radius * math.sin(angle_rad)
            self.add_hole(x, y)

    def _header(self, operation):
        return dedent(
            f"""( Conversational operation: {operation} )
            ( WCS: {self.wcs or 'G54'} )
            ( Units: {self.units or 'MM'} )
            ( Tool: {self.tool_number or 0} )
            ( Spindle: {self.spindle_dir or 'CW'} @ {self.spindle_rpm or 0} )
            ( Coolant: {self.coolant or 'OFF'} )
            ( Retract mode: {self.retract_mode} )
            ( Clearance: {self.z_clear or 0} )
            ( Z start: {self.z_start or 0}  Z end: {self.z_end or 0} )
            ( Retract height: {self.retract or 0} )
            ( Z feed: {self.z_feed or 0} )
            ( Holes: {len(self.holes)} )
            """
        ).strip()

    def _hole_lines(self):
        lines = []
        for hole in self.holes:
            lines.append(f"( Hole at X{hole[0]:.4f} Y{hole[1]:.4f} )")
        return "\n".join(lines)

    def _operation(self, name, detail=None):
        body = [self._header(name)]
        holes = self._hole_lines()
        if holes:
            body.append(holes)
        if detail:
            body.append(f"( {detail} )")
        return "\n".join(body)

    def drill(self):
        return self._operation("DRILL")

    def peck(self, peck_depth):
        return self._operation("PECK", f"Peck depth: {peck_depth}")

    def chip_break(self, break_depth):
        return self._operation("CHIP BREAK", f"Break depth: {break_depth}")

    def dwell(self, dwell_time):
        return self._operation("DWELL", f"Dwell time: {dwell_time}s")

    def tap(self, pitch):
        return self._operation("TAP", f"Pitch: {pitch}")

    def rigid_tap(self, pitch):
        return self._operation("RIGID TAP", f"Pitch: {pitch}")

    def manual(self):
        return self._operation("MANUAL")

