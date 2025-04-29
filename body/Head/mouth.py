from hardware import Motor
from utils import hex_to_decimal

class Mouth:
    def __init__(self, debug=False):
        self.jaw = Motor(
            name="Jaw",
            hardware_id=int(f"{hex_to_decimal('0x40')}10"),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

    def __str__(self):
        return f"Mouth:\n\t{self.jaw}"