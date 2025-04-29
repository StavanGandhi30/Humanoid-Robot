from .Head import *

class Head:
    def __init__(self):
        self.eyes = Eyes()
        self.eyelids = Eyelids()
        self.eyebrows = Eyebrows()
        self.mouth = Mouth()
        self.neck = Neck()

    def loadVar(self):
        return self.eyes, self.eyelids, self.eyebrows, self.mouth, self.neck

    def __str__(self):
        return f"Face: {'-'*100}\n\n{self.eyes}\n{self.eyelids}\n{self.eyebrows}\n{self.mouth}\n{self.neck}\n"