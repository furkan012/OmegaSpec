# test_omegaspec.py
"""
Tests for OmegaSpec module.
"""

import unittest
from omegaspec import OmegaSpec

class TestOmegaSpec(unittest.TestCase):
    """Test cases for OmegaSpec class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmegaSpec()
        self.assertIsInstance(instance, OmegaSpec)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmegaSpec()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
