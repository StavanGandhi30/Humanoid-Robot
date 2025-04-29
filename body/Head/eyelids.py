from hardware import Motor
from utils import hex_to_decimal

class Eyelids:
    def __init__(self, debug=False):
        self.__left_top_eyelid = Motor (
            name="Left-Top Eyelids",
            hardware_id=int(f'{hex_to_decimal('0x40')}02'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.__left_bottom_eyelid = Motor (
            name="Left-Bottom Eyelids",
            hardware_id=int(f'{hex_to_decimal('0x40')}03'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.__right_top_eyelid = Motor (
            name="Right-Top Eyelids",
            hardware_id=int(f'{hex_to_decimal('0x40')}04'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.__right_bottom_eyelid = Motor (
            name="Right-Bottom Eyelids",
            hardware_id=int(f'{hex_to_decimal('0x40')}05'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.left_eyelids = [self.__left_top_eyelid, self.__left_bottom_eyelid]
        self.right_eyelids = [self.__right_top_eyelid, self.__right_bottom_eyelid]
        self.debug=debug
    
    def close(self, type="both"):
        if (type=="both"):
            self.__left_top_eyelid.move_to_min_pos()
            self.__left_bottom_eyelid.move_to_min_pos()
            self.__right_top_eyelid.move_to_min_pos()
            self.__right_bottom_eyelid.move_to_min_pos()
        elif (type=="left"):
            self.__left_top_eyelid.move_to_min_pos()
            self.__left_bottom_eyelid.move_to_min_pos()
        elif (type=="right"):
            self.__right_top_eyelid.move_to_min_pos()
            self.__right_bottom_eyelid.move_to_min_pos()
        else:
            if self.debug:
                print("Invalid Parameter")

    def open(self, type="both"):
        if (type=="both"):
            self.__left_top_eyelid.move_to_max_pos()
            self.__left_bottom_eyelid.move_to_max_pos()
            self.__right_top_eyelid.move_to_max_pos()
            self.__right_bottom_eyelid.move_to_max_pos()
        elif (type=="left"):
            self.__left_top_eyelid.move_to_max_pos()
            self.__left_bottom_eyelid.move_to_max_pos()
        elif (type=="right"):
            self.__right_top_eyelid.move_to_max_pos()
            self.__right_bottom_eyelid.move_to_max_pos()
        else:
            if self.debug:
                print("Invalid Parameter")

    def get_motors(self):
        return [self.__left_top_eyelid, self.__left_bottom_eyelid, self.__right_top_eyelid, self.__right_bottom_eyelid]
    
    def get_position(self):
        return [self.__left_top_eyelid.current_angle, self.__left_bottom_eyelid.current_angle, self.__right_top_eyelid.current_angle, self.__right_bottom_eyelid.current_angle]
        
    def __str__(self):
        return f"EyeLids:\n\t{self.__left_top_eyelid}\n\t{self.__left_bottom_eyelid}\n\t{self.__right_top_eyelid}\n\t{self.__right_bottom_eyelid}"