from .Face import *

class Face:
    def __init__(self):
        self.eyes = Eyes(board="0x40", start_unit=0) # 2 Motors
        self.eyelids = Eyelids(board="0x40", start_unit=2) # 4 Motors
        self.eyebrows = Eyebrows(board="0x40", start_unit=6) # 4 Motors
        self.mouth = Mouth(board="0x40", start_unit=10) # 9 Motors

    def __str__(self):
        return f"Face: {"-"*100}\n\n{self.eyes}\n{self.eyelids}\n{self.eyebrows}\n{self.mouth}\n"