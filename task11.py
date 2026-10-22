"""Task 11: Apply seasonal pricing and the >500 L bonus."""
from milkrate import calculate_rate, calculate_payment, farmer_bonus, money
from decimal import Decimal
def run():
    entries = [(250, 4.23, 8.67), (260, 4.20, 8.70)]
    litres = Decimal("0"); payment = Decimal("0")
    print("TASK 11 - SEASONAL RATE AND BONUS")
    for amount, fat, snf in entries:
        rate = calculate_rate(fat, snf, base_rate="32.00", fat_step_rate="0.45")
        pay = calculate_payment(amount, rate)
        litres += Decimal(str(amount)); payment += pay
        print(f"{amount} L at ₹{rate:.2f}/L = ₹{pay:.2f}")
    bonus = farmer_bonus(litres)
    print(f"Total: {litres:.2f} L; milk payment ₹{money(payment):.2f}; bonus ₹{bonus:.2f}; final ₹{money(payment+bonus):.2f}")
if __name__ == "__main__": run()
