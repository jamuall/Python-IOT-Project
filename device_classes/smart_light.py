import random
from device_classes.IoTDevice import IoTDevice


class SmartLight(IoTDevice):
    def __init__(self, device_id, status="off", brightness=0):
            super().__init__(device_id, status)
            self.brightness = brightness

    def set_brightness(self, brightness):
            self.brightness = brightness

    def randomize_device_state(self):
        if random.random() < 0.5:
            self.turn_on()
        else:
            self.turn_off()

        self.set_brightness(random.randint(0, 100))
