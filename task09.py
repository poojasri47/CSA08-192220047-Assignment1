"""Task 9: Demonstrate scalable aggregation by farmer ID."""
from decimal import Decimal
from milkrate import calculate_rate, calculate_payment
def aggregate(entries):
    result = {}
    for e in entries:
        key = e["farmer_id"]
        result.setdefault(key, {"litres": Decimal("0"), "payment": Decimal("0")})
        result[key]["litres"] += Decimal(str(e["litres"]))
        result[key]["payment"] += calculate_payment(e["litres"], calculate_rate(e["fat"], e["snf"]))
    return result
def run():
    entries = [{"farmer_id": f"F{i%300:04d}", "litres": 5, "fat": 3.5, "snf": 8.5} for i in range(10000)]
    summary = aggregate(entries)
    print("TASK 9 - SCALABLE AGGREGATION")
    print(f"Input deliveries: {len(entries)}; unique farmers: {len(summary)}")
    print("Example F0000:", summary["F0000"]["litres"], "L")
if __name__ == "__main__": run()
