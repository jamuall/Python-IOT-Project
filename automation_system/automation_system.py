import random
import datetime
from device_classes.smart_light import SmartLight
from device_classes.thermostat import Thermostat
from device_classes.security_camera import SecurityCamera
from device_classes.IoTDevice import IoTDevice

class AutomationSystem:
    def __init__(self):
        """
        Initializes an empty list for storing IoT devices.
        """
        self.devices = []

    def discover_device(self, device):
        """
        Adds an IoT device to the list of discovered devices.

        Args:
            device (IoTDevice): An instance of an IoT device.
        """
        self.devices.append(device)

    def execute_automation(self):
        """
        Iterates through the list of devices and triggers the randomization of their states.
        """
        for device in self.devices:
            self.randomize_device_state(device)

    def randomize_device_state(self, device):
        """
        Randomly changes the state of an IoT device, simulating gradual changes for specific device types.

        Args:
            device (IoTDevice): An instance of an IoT device.
        """
        if random.random() < 0.5:
            device.turn_on()
        else:
            device.turn_off()

        if isinstance(device, SmartLight):
            # Simulate gradual changes in brightness
            current_brightness = device.brightness
            random_change = random.uniform(-10, 10)  # Allow for a random change between -10 and 10
            new_brightness = max(0, min(100, current_brightness + random_change))
            device.set_brightness(new_brightness)

        elif isinstance(device, Thermostat):
            # Simulate gradual changes in temperature
            current_temperature = device.temperature
            random_change = random.uniform(-2, 2)  # Allow for a random change between -2 and 2
            new_temperature = max(10, min(30, current_temperature + random_change))
            device.set_temperature(new_temperature)

        elif isinstance(device, SecurityCamera):
            # Simulate random changes in security status
            device.set_security_status(random.choice(['secure', 'insecure']))

    def log_device_data(self):
        """
        Collects and returns data on the current states of all discovered devices, including status, timestamp,
        brightness (for smart lights), temperature (for thermostats), and security status (for security cameras).

        Returns:
            dict: A dictionary containing device data.
        """
        data = {}
        for device in self.devices:
            data[device.device_id] = {
                "status": device.status,
                "timestamp": datetime.datetime.now()
            }
            if isinstance(device, SmartLight):
                data[device.device_id]["brightness"] = device.brightness
            elif isinstance(device, Thermostat):
                data[device.device_id]["temperature"] = device.temperature
            elif isinstance(device, SecurityCamera):
                data[device.device_id]["security_status"] = device.security_status
        return data

    def simulate(self, num_iterations):
        """
        Runs the automation system simulation for a specified number of iterations, triggering changes in device states.

        Args:
            num_iterations (int): The number of iterations to run the simulation.
        """
        for _ in range(num_iterations):
            self.execute_automation()
