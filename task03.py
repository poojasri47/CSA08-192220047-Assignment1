"""Task 3: Validate fat and SNF input."""
from milkrate import calculate_rate
def run():
    print("TASK 3 - INPUT VALIDATION")
    for fat, snf in [(2.0, 8.5), (7.0, 8.5), (1.9, 8.5), (7.1, 8.5), (3.5, 0)]:
        try: print(f"{fat}% fat, {snf}% SNF -> ₹{calculate_rate(fat, snf):.2f}/L")
        except ValueError as exc: print(f"{fat}% fat, {snf}% SNF -> INVALID: {exc}")
if __name__ == "__main__": run()
