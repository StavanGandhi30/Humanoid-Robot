from Hardware import Motor
from Utils import hex_to_decimal

class Eyebrows:
    def __init__(self, board, start_unit, debug=False):
        self.left_eyebrow = Motor(
            name="Left Eyebrow",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        self.right_eyebrow = Motor (
            name="Right Eyebrow",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+1:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

    def __str__(self):
        return f"Eyebrows:\n\t{self.left_eyebrow}\n\t{self.right_eyebrow}"