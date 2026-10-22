"""Integrated Ksheera milk payment demonstration."""
import json
from pathlib import Path
from decimal import Decimal
from milkrate import calculate_rate, calculate_payment, farmer_bonus, money

ROOT = Path(__file__).resolve().parent

def process_entries(entries, seasonal=False):
    totals = {}
    for entry in entries:
        farmer = str(entry["farmer_id"])
        litres = Decimal(str(entry["litres"]))
        rate = calculate_rate(
            entry["fat"], entry["snf"],
            base_rate=Decimal("32.00") if seasonal else Decimal("30.00"),
            fat_step_rate=Decimal("0.45") if seasonal else Decimal("0.40")
        )
        payment = calculate_payment(litres, rate)
        if farmer not in totals:
            totals[farmer] = {"litres": Decimal("0"), "milk_payment": Decimal("0")}
        totals[farmer]["litres"] += litres
        totals[farmer]["milk_payment"] += payment
        print(f'{farmer:<12} {entry["session"]:<8} {litres:>7.2f} L  '
              f'fat={Decimal(str(entry["fat"])):>4.2f}%  snf={Decimal(str(entry["snf"])):>4.2f}%  '
              f'rate=₹{rate:>5.2f}/L  payment=₹{payment:>8.2f}')
    print("\\nFARMER TOTALS")
    for farmer, values in sorted(totals.items()):
        bonus = farmer_bonus(values["litres"]) if seasonal else Decimal("0.00")
        final = money(values["milk_payment"] + bonus)
        print(f"{farmer}: {values['litres']:.2f} L; milk ₹{values['milk_payment']:.2f}; "
              f"bonus ₹{bonus:.2f}; final ₹{final:.2f}")
    return totals

def main():
    path = ROOT / "inputs" / "sample_milk_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    print("KSHEERA VILLAGE MILK PAYMENT SYSTEM")
    print("Mode:", data.get("mode", "standard"))
    process_entries(data["entries"], seasonal=data.get("mode") == "seasonal")

if __name__ == "__main__":
    main()
