from Hardware import Motor
from Utils import hex_to_decimal

class Eyes:
    def __init__(self, board, start_unit, debug=False):
        self.horizontal_motor = Motor(
            name="Horizontal Motor",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.vertical_motor = Motor (
            name="Vertical Motor",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+1:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

    # Move some amount in left, right, up, or down direction
    def move_left(self, amount):
        self.horizontal_motor.move_to(self.horizontal_motor.current_angle - amount)

    def move_right(self, amount):
        self.horizontal_motor.move_to(self.horizontal_motor.current_angle + amount)

    def move_up(self, amount):
        self.vertical_motor.move_to(self.vertical_motor.current_angle - amount)

    def move_down(self, amount):
        self.vertical_motor.move_to(self.vertical_motor.current_angle + amount)

    # Move all the way in left, right, up, or down direction
    def look_left(self):
        self.horizontal_motor.move_to(self.horizontal_motor.min_angle)

    def look_right(self):
        self.horizontal_motor.move_to(self.horizontal_motor.max_angle)

    def look_up(self):
        self.vertical_motor.move_to(self.vertical_motor.max_angle)

    def look_down(self):
        self.vertical_motor.move_to(self.vertical_motor.min_angle)

    def look_center(self):
        self.horizontal_motor.move_home()
        self.vertical_motor.move_home()

    def get_position(self):
        return [self.horizontal_motor.current_angle, self.vertical_motor.current_angle]
        
    def __str__(self):
        return f"Eyes:\n\t{self.horizontal_motor}\n\t{self.vertical_motor}"