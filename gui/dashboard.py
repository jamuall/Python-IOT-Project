import tkinter as tk
from tkinter import ttk
from device_classes.smart_light import SmartLight
from device_classes.thermostat import Thermostat
from device_classes.security_camera import SecurityCamera
from device_classes.IoTDevice import IoTDevice


def update_label(value, device, label):
    """
    Updates the label text dynamically based on the adjusted value (brightness or temperature).

    Args:
        value: The adjusted value (brightness or temperature).
        device (IoTDevice): The IoT device instance.
        label (ttk.Label): The label to be updated.
    """
    if isinstance(device, SmartLight):
        label.config(text=f"Brightness: {int(round(float(value)))}%")
    elif isinstance(device, Thermostat):
        label.config(text=f"Temperature: {int(round(float(value)))}°C")


class Dashboard(tk.Tk):
    def __init__(self, automation_system):
        """
        Initializes the Dashboard with a specified AutomationSystem instance.

        Args:
            automation_system (AutomationSystem): An instance of the AutomationSystem managing IoT devices.
        """
        tk.Tk.__init__(self)
        self.title("IoT Device Simulator Dashboard")
        self.geometry("1000x600")  # Increase the window size
        self.automation_system = automation_system

        self.status_display = tk.Text(self, wrap=tk.WORD, height=5, width=60)  # Adjust the size of the status display
        self.status_display.pack()

        self.create_widgets()

    def create_widgets(self):
        """
        Configures and places widgets on the GUI for each discovered IoT device.
        """
        for device in self.automation_system.devices:
            device_frame = ttk.LabelFrame(self, text=device.device_id)
            device_frame.pack(pady=10)

            status_label = ttk.Label(device_frame, text=f"Status: {device.status}")
            status_label.pack()

            if isinstance(device, SmartLight):
                brightness_label = ttk.Label(device_frame, text=f"Brightness: {device.brightness}%")
                brightness_label.pack()

                brightness_var = tk.IntVar(value=device.brightness)
                brightness_adjuster = ttk.Scale(device_frame, from_=0, to=100, orient=tk.HORIZONTAL,
                                                variable=brightness_var, command=lambda value, dev=device, label=brightness_label: update_label(value, dev, label))
                brightness_adjuster.pack()

                on_off_button = ttk.Button(device_frame, text="Toggle On/Off",
                                           command=lambda dev=device, adj=brightness_var: self.toggle_light(dev, adj))
                on_off_button.pack()

            elif isinstance(device, Thermostat):
                temperature_label = ttk.Label(device_frame, text=f"Temperature: {int(device.temperature)}°C")
                temperature_label.pack()

                temperature_var = tk.DoubleVar(value=device.temperature)
                temperature_adjuster = ttk.Scale(device_frame, from_=10, to=30, orient=tk.HORIZONTAL,
                                                 variable=temperature_var, command=lambda value, dev=device, label=temperature_label: update_label(value, dev, label))
                temperature_adjuster.pack()

                on_off_button = ttk.Button(device_frame, text="Toggle On/Off",
                                           command=lambda dev=device, adj=temperature_var: self.toggle_thermostat(dev, adj))
                on_off_button.pack()

            elif isinstance(device, SecurityCamera):
                motion_label = ttk.Label(device_frame, text=f"Motion Detection: {device.security_status}")
                motion_label.pack()

                random_motion_button = ttk.Button(device_frame, text="Random Detect Motion",
                                                  command=lambda dev=device: self.detect_motion(dev))
                random_motion_button.pack()

                on_off_button = ttk.Button(device_frame, text="Toggle On/Off",
                                           command=lambda dev=device: self.toggle_camera(dev))
                on_off_button.pack()

        automation_rule_label = ttk.Label(self, text="Automation Rule: Turn on lights when motion is detected")
        automation_rule_label.pack()

    def toggle_light(self, device, adjuster):
        """
        Toggles the state of a SmartLight device and updates the GUI with the new status and brightness.

        Args:
            device (SmartLight): The SmartLight device instance.
            adjuster (tk.IntVar): The brightness adjuster variable.
        """
        if device.status == "on":
            device.turn_off()
        else:
            device.turn_on()
        self.update_device_status(device)  # Update status label immediately
        device.set_brightness(adjuster.get())  # Update brightness value
        self.update_data()

    def toggle_thermostat(self, device, adjuster):
        """
        Toggles the state of a Thermostat device and updates the GUI with the new status and temperature.

        Args:
            device (Thermostat): The Thermostat device instance.
            adjuster (tk.DoubleVar): The temperature adjuster variable.
        """
        if device.status == "on":
            device.turn_off()
        else:
            device.turn_on()
        self.update_device_status(device)  # Update status label immediately
        device.set_temperature(adjuster.get())  # Update temperature value
        self.update_data()

    def detect_motion(self, device):
        """
        Simulates motion detection for a SecurityCamera device, updates the status, and triggers camera state toggle.

        Args:
            device (SecurityCamera): The SecurityCamera device instance.
        """
        device.set_security_status("Motion Detected")
        self.toggle_camera(device)
        self.update_data()

    def toggle_camera(self, device):
        """
        Toggles the state of a SecurityCamera device and updates the GUI with the new status.

        Args:
            device (SecurityCamera): The SecurityCamera device instance.
        """
        if device.status == "on":
            device.turn_off()
        else:
            device.turn_on()
        self.update_device_status(device)  # Update status label immediately
        self.update_data()

    def update_data(self):
        """
        Updates the GUI with the latest status data for all discovered devices.
        """
        data = self.automation_system.log_device_data()
        status_text = ""
        for device_id, device_data in data.items():
            status_text += f"{device_id}: {device_data['status']}\n"
        self.status_display.delete(1.0, tk.END)
        self.status_display.insert(tk.END, status_text)

    def update_device_status(self, device):
        """
        Updates the status label for a specific device in the GUI.

        Args:
            device (IoTDevice): The IoT device instance.
        """
        for frame in self.winfo_children():
            if isinstance(frame, ttk.LabelFrame) and frame['text'] == device.device_id:
                for label in frame.winfo_children():
                    if isinstance(label, ttk.Label) and label.cget("text").startswith("Status:"):
                        label.config(text=f"Status: {device.status}")
                        break
                break
