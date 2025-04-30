from hardware import Servo 
from utils import hex_to_decimal

class Neck:
    def __init__(self, debug=False):
        self.roll_motor = Servo (
            name="Neck Roll Motor",
            hardware_id=(f"{hex_to_decimal('0x44')}09"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.left_motor = Servo (
            name="Neck Yam Motor",
            hardware_id=(f"{hex_to_decimal('0x44')}10"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.right_motor = Servo (
            name="Neck Pitch Motor",
            hardware_id=(f"{hex_to_decimal('0x44')}11"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        
    def get_motors(self):
        return [self.roll_motor, self.left_motor, self.right_motor]
    
    def __str__(self):
        motors = self.get_motors()
        return f"Neck ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)