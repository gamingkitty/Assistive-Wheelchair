import board
from adafruit_motorkit import MotorKit


class Wheelchair:
    def __init__(self):
        self.kit = kit = MotorKit(i2c=board.I2C())

    # Positive power = forward, negative power = reverse
    def forward(self, power):
        self.kit.motor1.throttle = power
        self.kit.motor3.throttle = -power

    # Positive power = left, negative power = right
    def turn(self, power):
        self.kit.motor1.throttle = power
        self.kit.motor3.throttle = power

    # Stops the wheelchair from moving
    def stop(self):
        self.forward(0)
