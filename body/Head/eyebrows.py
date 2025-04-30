from hardware import Servo
from utils import hex_to_decimal

class Eyebrows:
    def __init__(self, debug=False):
        self.left_eyebrow_outer = Servo (
            name="Left Outer Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}06"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.left_eyebrow_inner = Servo (
            name="Left Inner Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}07"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

        self.right_eyebrow_outer = Servo (
            name="Right Outer Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}08"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        
        self.right_eyebrow_inner = Servo (
            name="Right Inner Eyebrow",
            hardware_id=(f"{hex_to_decimal('0x41')}09"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

    def get_motors(self):
        return [ self.left_eyebrow_outer, self.left_eyebrow_inner, self.right_eyebrow_outer, self.right_eyebrow_inner ]
    
    def __str__(self):
        motors = self.get_motors()
        return f"Eyebrows ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)