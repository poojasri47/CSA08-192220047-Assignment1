"""Task 8: Run representative boundary and correctness cases."""
from milkrate import calculate_rate
def run():
    print("TASK 8 - TEST CASE TABLE")
    cases = [(3.5, 8.5, "30.00"), (4.0, 8.5, "32.00"), (3.5, 9.0, "31.50"), (4.0, 8.7, "32.60")]
    for fat, snf, expected in cases:
        actual = f"{calculate_rate(fat, snf):.2f}"
        print(f"fat={fat}, snf={snf}, expected=₹{expected}, actual=₹{actual}, {'PASS' if actual == expected else 'FAIL'}")
if __name__ == "__main__": run()
