# test_esp32drift.py
"""
Tests for ESP32Drift module.
"""

import unittest
from esp32drift import ESP32Drift

class TestESP32Drift(unittest.TestCase):
    """Test cases for ESP32Drift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ESP32Drift()
        self.assertIsInstance(instance, ESP32Drift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ESP32Drift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
