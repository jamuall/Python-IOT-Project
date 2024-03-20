import unittest
from device_classes.smart_light import SmartLight
from device_classes.IoTDevice import IoTDevice

class TestSmartLight(unittest.TestCase):
    def test_turn_on(self):
        light = SmartLight(device_id="Living Room Light", status="off", brightness=0)
        light.turn_on()
        self.assertEqual(light.status, "on")

    def test_turn_off(self):
        light = SmartLight(device_id="Living Room Light", status="on", brightness=50)
        light.turn_off()
        self.assertEqual(light.status, "off")

    def test_set_brightness(self):
        light = SmartLight(device_id="Living Room Light", status="on", brightness=0)
        light.set_brightness(50)
        self.assertEqual(light.brightness, 50)

    def test_randomize_device_state(self):
        light = SmartLight(device_id="Living Room Light", status="off", brightness=0)

        # Run the randomization test multiple times
        for _ in range(100):
            light.randomize_device_state()
            self.assertIn(light.status, ["on", "off"])
            self.assertTrue(0 <= light.brightness <= 100)


if __name__ == '__main__':
    unittest.main()
