from Hardware import Motor
from Utils import hex_to_decimal

class Eyelids:
    def __init__(self, board, start_unit, debug=False):
        self.__left_top_eyelid = Motor (
            name="Left-Top Eyelids",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.__left_bottom_eyelid = Motor (
            name="Left-Bottom Eyelids",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+1:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.__right_top_eyelid = Motor (
            name="Right-Top Eyelids",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+2:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.__right_bottom_eyelid = Motor (
            name="Right-Bottom Eyelids",
            hardware_id=int(f'{hex_to_decimal(board)}{start_unit+3:02}'),
            min_angle=0,
            max_angle=20,
            rest_angle=10,
            debug=debug
        )

        self.left_eyelids = [self.__left_top_eyelid, self.__left_bottom_eyelid]
        self.right_eyelids = [self.__right_top_eyelid, self.__right_bottom_eyelid]
    
    def get_position(self):
        return [self.__left_top_eyelid.current_angle, self.__left_bottom_eyelid.current_angle, self.__right_top_eyelid.current_angle, self.__right_bottom_eyelid.current_angle]
        
    def __str__(self):
        return f"EyeLids:\n\t{self.__left_top_eyelid}\n\t{self.__left_bottom_eyelid}\n\t{self.__right_top_eyelid}\n\t{self.__right_bottom_eyelid}"