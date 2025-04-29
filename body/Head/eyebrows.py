from hardware import Motor
from utils import hex_to_decimal

class Eyebrows:
    def __init__(self, debug=False):
        self.left_left_eyebrow = Motor(
            name="Left-Left Eyebrow",
            hardware_id=int(f"{hex_to_decimal('0x40')}06"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        self.left_right_eyebrow = Motor(
            name="Left-Right Eyebrow",
            hardware_id=int(f"{hex_to_decimal('0x40')}07"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.right_left_eyebrow = Motor (
            name="Right-Left Eyebrow",
            hardware_id=int(f"{hex_to_decimal('0x40')}08"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.right_right_eyebrow = Motor (
            name="Right-Right Eyebrow",
            hardware_id=int(f"{hex_to_decimal('0x40')}09"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        
    def get_motors(self):
        return [self.left_left_eyebrow, self.left_right_eyebrow, self.right_left_eyebrow, self.right_right_eyebrow]
    
    def __str__(self):
        return f"Eyebrows:\n\t{self.left_left_eyebrow}\n\t{self.left_right_eyebrow}\n\t{self.right_left_eyebrow}\n\t{self.right_right_eyebrow}"