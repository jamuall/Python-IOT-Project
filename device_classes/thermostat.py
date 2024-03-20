import random
from device_classes.IoTDevice import IoTDevice


class Thermostat(IoTDevice):
    def __init__(self, device_id, status="off", temperature=22.0):
        """
        Initialize a Thermostat object.

        Parameters:
        - device_id (str): Unique identifier for the thermostat.
        - status (str, optional): Current status of the thermostat, default is "off".
        - temperature (float, optional): Current temperature setting of the thermostat, default is 22.0.

        Note:
        - Inherits from the IoTDevice class, which provides basic functionality and attributes for IoT devices.
        """
        super().__init__(device_id, status)
        self.temperature = temperature

    def set_temperature(self, temperature):
        """
        Set the temperature of the thermostat.

        Parameters:
        - temperature (float): The temperature setting to be set.

        Note:
        - The temperature value should be between 10 and 30.
        """
        self.temperature = temperature

    def randomize_device_state(self):
        # Simulate a random decision to turn on or off the thermostat
        if random.random() < 0.5:
            # If random number is less than 0.5, turn on the thermostat
            self.turn_on()
        else:
            # If random number is greater than or equal to 0.5, turn off the thermostat
            self.turn_off()

        # Simulate setting a random temperature between 10 and 30
        self.set_temperature(random.uniform(10, 30))
