"""Task 2: Calculate milk rate from fat and SNF percentages."""
from milkrate import calculate_rate
def run():
    print("TASK 2 - MILK RATE")
    for fat, snf in [(3.5, 8.5), (4.0, 8.5), (3.5, 9.0), (4.0, 8.7)]:
        print(f"Fat {fat:.1f}%, SNF {snf:.1f}% -> ₹{calculate_rate(fat, snf):.2f}/L")
if __name__ == "__main__": run()
