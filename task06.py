"""Task 6: Process and summarize records for multiple farmers."""
from milkrate import calculate_rate, calculate_payment, money
from decimal import Decimal
def run():
    rows = [("F001", 10, 3.5, 8.5), ("F002", 12, 4.0, 8.7), ("F001", 8, 3.8, 8.6)]
    summary = {}
    for farmer, litres, fat, snf in rows:
        summary.setdefault(farmer, {"litres": Decimal("0"), "pay": Decimal("0")})
        summary[farmer]["litres"] += Decimal(str(litres))
        summary[farmer]["pay"] += calculate_payment(litres, calculate_rate(fat, snf))
    print("TASK 6 - FARMER SUMMARY")
    for farmer, values in sorted(summary.items()):
        print(f"{farmer}: {values['litres']:.2f} L; ₹{money(values['pay']):.2f}")
if __name__ == "__main__": run()
