from device_classes.smart_light import SmartLight
from device_classes.thermostat import Thermostat
from device_classes.security_camera import SecurityCamera
from automation_system.automation_system import AutomationSystem
from gui.dashboard import Dashboard

if __name__ == "__main__":
    automation_system = AutomationSystem()

    light = SmartLight(device_id="Living Room Light", status="off", brightness=0)
    thermostat = Thermostat(device_id="Living Room Thermostat", status="off", temperature=22.0)
    camera = SecurityCamera(device_id="Front Door Camera", status="off", security_status="Secure")

    automation_system.discover_device(light)
    automation_system.discover_device(thermostat)
    automation_system.discover_device(camera)

    # Start the simulation loop
    automation_system.simulate(num_iterations=3)

    # Create and run the dashboard
    dashboard = Dashboard(automation_system)
    dashboard.mainloop()