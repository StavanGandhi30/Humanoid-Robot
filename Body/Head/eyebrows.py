from hardware import Motor
from utils import hex_to_decimal

class Eyebrows:
    def __init__(self, board, start_unit, debug=False):
        self.left_left_eyebrow = Motor(
            name="Left-Left Eyebrow",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        self.left_right_eyebrow = Motor(
            name="Left-Right Eyebrow",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+1:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.right_left_eyebrow = Motor (
            name="Right-Left Eyebrow",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+2:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.right_right_eyebrow = Motor (
            name="Right-Right Eyebrow",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+3:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

    def __str__(self):
        return f"Eyebrows:\n\t{self.left_left_eyebrow}\n\t{self.left_right_eyebrow}\n\t{self.right_left_eyebrow}\n\t{self.right_right_eyebrow}"