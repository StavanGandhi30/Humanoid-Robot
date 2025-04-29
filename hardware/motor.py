class Motor:
    def __init__(self, name, hardware_id, min_angle=0, max_angle=180, rest_angle=90, debug = False):
        self.name = name
        self.hardware_id = hardware_id
        self.min_angle = min_angle if min_angle>=0 else 0
        self.max_angle = max_angle if max_angle<=360 else 360
        self.rest_angle = rest_angle if self._isValid(rest_angle) else self.min_angle
        self.current_angle = rest_angle
        self.debug = debug

        self.move_to(self.rest_angle)

    def move_to(self, angle):
        # Clamp the angle within allowed range
        if self._isValid(angle):
            # TODO: Send PWM signal here to the real motor
            self.current_angle = angle

        if self.debug:
            print(f"Moving motor {self.name} (ID: {self.hardware_id}) to {angle} degrees.")

    def move_to_max_pos(self):
        self.move_to(self.rest_angle)

    def move_to_min_pos(self):
        self.move_to(self.rest_angle)

    def move_to_rest_pos(self):
        self.move_to(self.rest_angle)

    def _isValid(self, angle):
        if (angle >= self.min_angle) and (angle<=self.max_angle):
            return True
        
        if self.debug:
            print(f"[Invalid Angle Error] Motor {self.name} (ID: {self.hardware_id}) cannot move to {angle} degrees.")

        return False
    
    def __str__(self):
        return f"Motor {self.name}, ID: {self.hardware_id}, Current Angle: {self.current_angle} degrees, Minimum Angle: {self.min_angle} degrees, Maximum Angle: {self.max_angle} degrees, Rest Angle: {self.rest_angle} degrees"