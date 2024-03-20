from device_classes.IoTDevice import IoTDevice

class SecurityCamera(IoTDevice):
    def __init__(self, device_id, status="off", security_status="Secure"):
        """
        Initialize a SecurityCamera object.

        Parameters:
        - device_id (str): Unique identifier for the security camera.
        - status (str, optional): Current status of the security camera, default is "off".
        - security_status (str, optional): Current security status of the camera, default is "Secure".

        Note:
        - Inherits from the IoTDevice class, which provides basic functionality and attributes for IoT devices.
        """
        super().__init__(device_id, status)
        self.security_status = security_status

    def set_security_status(self, security_status):
        """
        Set the security status of the security camera.

        Parameters:
        - security_status (str): The security status to be set.

        Note:
        - The security status can be "Secure" or "Insecure".
        """
        self.security_status = security_status
