class IoTDevice:
    def __init__(self, device_id, status="off"):
        self.device_id = device_id
        self.status = status

    def turn_on(self):
        self.status = 'on'
        print(f"{self.device_id} turned on.")
        #Turns on the device.

    def turn_off(self):
        self.status = 'off'
        print(f"{self.device_id} turned off.")
        #Turns off the device.