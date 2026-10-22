"""Task 1: Demonstrate why Decimal is preferred for money."""
from decimal import Decimal
def run():
    float_total = sum([0.1 + 0.2 + 0.3 for _ in range(100000)])
    decimal_total = sum((Decimal("0.1") + Decimal("0.2") + Decimal("0.3") for _ in range(100000)), Decimal("0"))
    print("TASK 1 - FLOATING-POINT PRECISION")
    print("Float total:", float_total)
    print("Decimal total:", decimal_total)
if __name__ == "__main__": run()
