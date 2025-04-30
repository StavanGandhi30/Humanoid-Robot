# from Adafruit_PCA9685 import PCA9685

class ServoDriver:
    def __init__(self, address=0x41, channel=0, frequency=60, servo_min=150, servo_max=600):
        # self.pwm = PCA9685(address=address)
        # self.pwm.set_pwm_freq(frequency)
        self.servo_min = servo_min
        self.servo_max = servo_max
        self.channel = channel

    def set_servo_angle(self, angle):
        pulse = int(self.servo_min + (self.servo_max - self.servo_min) * int(angle) / 180)
        # self.pwm.set_pwm(self.channel, 0, pulse)
        print(f"Moving {self.channel} to {angle} degrees")

if __name__ == "__main__":
    import time
    
    controller = ServoDriver()

    try:
        while True:
            controller.set_servo_angle(0)
            time.sleep(1)

            controller.set_servo_angle(90)
            time.sleep(1)

            controller.set_servo_angle(180)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program stopped")
        controller.set_servo_angle(0, 90)  # Reset to neutral position
