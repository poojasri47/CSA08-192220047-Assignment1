"""Task 7: Use a separate milkrate module."""
from milkrate import calculate_rate, calculate_payment
def run():
    rate = calculate_rate(4.0, 8.7)
    payment = calculate_payment(25.5, rate)
    print("TASK 7 - MODULE IMPORT")
    print(f"Imported rate function: ₹{rate:.2f}/L")
    print(f"Imported payment function: ₹{payment:.2f}")
if __name__ == "__main__": run()
