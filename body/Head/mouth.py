from hardware import Servo
from utils import hex_to_decimal

class Mouth:
    def __init__(self, debug=False):
        self.left_upper_lip = Servo (
            name="Left Upper Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}00"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.left_lower_lip = Servo (
            name="Left Lower Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}01"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.right_upper_lip = Servo (
            name="Right Upper Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}02"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.right_lower_lip = Servo (
            name="Right Lower Lip",
            hardware_id=(f"{hex_to_decimal('0x44')}03"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

        # Lip Corners (fully specified)
        self.left_upper_lip_corner = Servo (
            name="Left Upper Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}04"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.left_lower_lip_corner = Servo (
            name="Left Lower Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}05"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.right_upper_lip_corner = Servo (
            name="Right Upper Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}06"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )
        self.right_lower_lip_corner = Servo (
            name="Right Lower Lip Corner",
            hardware_id=(f"{hex_to_decimal('0x44')}07"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

        self.jaw = Servo (
            name="Jaw",
            hardware_id=(f"{hex_to_decimal('0x44')}08"),
            min_angle=0, max_angle=20, rest_angle=10, debug=debug
        )

        self.lips = [
            self.left_upper_lip, self.left_lower_lip,
            self.right_upper_lip, self.right_lower_lip
        ]

        self.lip_corners = [
            self.left_upper_lip_corner, self.left_lower_lip_corner,
            self.right_upper_lip_corner, self.right_lower_lip_corner
        ]

    def get_motors(self):
        return [
            self.left_upper_lip, self.left_lower_lip,
            self.right_upper_lip, self.right_lower_lip,
            self.left_upper_lip_corner, self.left_lower_lip_corner,
            self.right_upper_lip_corner, self.right_lower_lip_corner,
            self.jaw
        ]
    
    def __str__(self):
        motors = self.get_motors()
        return f"Mouth ({len(motors)}) :\n\t" + "\n\t".join(str(motor) for motor in motors)