"""Task 5: Add morning/evening deliveries for a ten-day period."""
from milkrate import calculate_rate, calculate_payment, money
def run():
    deliveries = [(10.0, 3.5, 8.5), (12.5, 4.0, 8.7), (9.0, 3.8, 8.6)]
    total_litres = sum((__import__("decimal").Decimal(str(x[0])) for x in deliveries), __import__("decimal").Decimal("0"))
    total_pay = sum((calculate_payment(l, calculate_rate(f, s)) for l, f, s in deliveries), __import__("decimal").Decimal("0"))
    print("TASK 5 - PERIOD TOTAL")
    print(f"Recorded deliveries: {len(deliveries)}")
    print(f"Total litres: {total_litres:.2f}")
    print(f"Total payment: ₹{money(total_pay):.2f}")
if __name__ == "__main__": run()
