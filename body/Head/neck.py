from hardware import Motor
from utils import hex_to_decimal

class Neck:
    def __init__(self, debug=False):
        self.horizontal_motor = Motor(
            name="Neck Horizontal Motor",
            hardware_id=int(f"{hex_to_decimal('0x40')}11"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        self.vertical_motor = Motor(
            name="Neck Vertical Motor",
            hardware_id=int(f"{hex_to_decimal('0x40')}12"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        
    def get_motors(self):
        return [self.horizontal_motor, self.vertical_motor]

    def __str__(self):
        return f"Neck:\n\t{self.horizontal_motor}\n\t{self.vertical_motor}"