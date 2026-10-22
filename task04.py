"""Task 4: Calculate payment for a single milk delivery."""
from milkrate import calculate_rate, calculate_payment
def run():
    litres, fat, snf = 25.50, 4.0, 8.7
    rate = calculate_rate(fat, snf)
    print("TASK 4 - SINGLE DELIVERY PAYMENT")
    print(f"Litres: {litres:.2f}; rate: ₹{rate:.2f}/L; payment: ₹{calculate_payment(litres, rate):.2f}")
if __name__ == "__main__": run()
