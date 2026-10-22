"""Reusable milk-rate calculation functions for Ksheera Village Co-operative."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP_RATE = Decimal("0.40")
SNF_STEP_RATE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")

def money(value):
    """Round a monetary value to the nearest paisa."""
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def _steps(value, base):
    """Count 0.1 percentage-point steps, rounding to the nearest step."""
    return int(((Decimal(str(value)) - base) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP))

def calculate_rate(fat, snf, base_rate=BASE_RATE, fat_step_rate=FAT_STEP_RATE):
    """Calculate rate per litre. SNF adjustment remains ₹0.30 per 0.1% step."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError(f"Fat must be between {MIN_FAT}% and {MAX_FAT}%.")
    if snf <= 0:
        raise ValueError("SNF must be greater than 0%.")
    fat_steps = _steps(fat, BASE_FAT)
    snf_steps = _steps(snf, BASE_SNF)
    rate = Decimal(str(base_rate)) + fat_steps * Decimal(str(fat_step_rate)) + snf_steps * SNF_STEP_RATE
    return money(rate)

def calculate_payment(litres, rate):
    litres = Decimal(str(litres))
    if litres < 0:
        raise ValueError("Litres cannot be negative.")
    return money(litres * Decimal(str(rate)))

def farmer_bonus(total_litres):
    """Day-4 seasonal incentive: ₹0.50/L only when total exceeds 500 L."""
    litres = Decimal(str(total_litres))
    return money(litres * Decimal("0.50")) if litres > Decimal("500") else Decimal("0.00")
