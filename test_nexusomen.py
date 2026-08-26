# test_nexusomen.py
"""
Tests for NexusOmen module.
"""

import unittest
from nexusomen import NexusOmen

class TestNexusOmen(unittest.TestCase):
    """Test cases for NexusOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NexusOmen()
        self.assertIsInstance(instance, NexusOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NexusOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
