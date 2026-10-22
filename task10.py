"""Task 10: Load delivery records from JSON."""
import json
from pathlib import Path
from milkrate import calculate_rate, calculate_payment
def run():
    path = Path(__file__).resolve().parents[1] / "inputs" / "sample_milk_data.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    print("TASK 10 - JSON INPUT")
    print(f"Loaded {len(data['entries'])} delivery records from {path.name}")
    for e in data["entries"]:
        rate = calculate_rate(e["fat"], e["snf"], base_rate="32.00" if data.get("mode") == "seasonal" else "30.00",
                              fat_step_rate="0.45" if data.get("mode") == "seasonal" else "0.40")
        print(e["farmer_id"], e["session"], f"₹{calculate_payment(e['litres'], rate):.2f}")
if __name__ == "__main__": run()
