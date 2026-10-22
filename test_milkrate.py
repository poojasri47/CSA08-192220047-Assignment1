import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import unittest
from decimal import Decimal
from milkrate import calculate_rate, calculate_payment, farmer_bonus

class MilkRateTests(unittest.TestCase):
    def test_base_rate(self):
        self.assertEqual(calculate_rate(3.5, 8.5), Decimal("30.00"))
    def test_fat_adjustment(self):
        self.assertEqual(calculate_rate(4.0, 8.5), Decimal("32.00"))
    def test_snf_adjustment(self):
        self.assertEqual(calculate_rate(3.5, 9.0), Decimal("31.50"))
    def test_both_adjustments(self):
        self.assertEqual(calculate_rate(4.0, 8.7), Decimal("32.60"))
    def test_payment(self):
        self.assertEqual(calculate_payment("25.50", "32.60"), Decimal("831.30"))
    def test_fat_too_low(self):
        with self.assertRaises(ValueError): calculate_rate(1.9, 8.5)
    def test_fat_too_high(self):
        with self.assertRaises(ValueError): calculate_rate(7.1, 8.5)
    def test_bonus_threshold(self):
        self.assertEqual(farmer_bonus(500), Decimal("0.00"))
        self.assertEqual(farmer_bonus(501), Decimal("250.50"))

if __name__ == "__main__":
    unittest.main()
