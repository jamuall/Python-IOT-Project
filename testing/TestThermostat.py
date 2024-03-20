import unittest
from device_classes.thermostat import Thermostat
from device_classes.IoTDevice import IoTDevice


class TestThermostat(unittest.TestCase):
    def test_turn_on(self):
        thermostat = Thermostat(device_id="Living Room Thermostat", status="off", temperature=22.0)
        thermostat.turn_on()
        self.assertEqual(thermostat.status, "on")

    def test_turn_off(self):
        thermostat = Thermostat(device_id="Living Room Thermostat", status="on", temperature=22.0)
        thermostat.turn_off()
        self.assertEqual(thermostat.status, "off")

    def test_set_temperature(self):
        thermostat = Thermostat(device_id="Living Room Thermostat", status="on", temperature=22.0)
        thermostat.set_temperature(25.5)
        self.assertEqual(thermostat.temperature, 25.5)

    def test_randomize_device_state(self):
        thermostat = Thermostat(device_id="Living Room Thermostat", status="off", temperature=22.0)
        thermostat.randomize_device_state()
        self.assertIn(thermostat.status, ["on", "off"])
        self.assertTrue(10 <= thermostat.temperature <= 30)


if __name__ == '__main__':
    unittest.main()
