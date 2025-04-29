from hardware import Motor
from utils import hex_to_decimal

class Neck:
    def __init__(self, board, start_unit, debug=False):
        self.horizontal_motor = Motor(
            name="Neck Horizontal Motor",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
        self.vertical_motor = Motor(
            name="Neck Vertical Motor",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+1:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )
    
    def __str__(self):
        return f"Neck:\n\t{self.horizontal_motor}\n\t{self.vertical_motor}"