# Ksheera Village Milk Payment System — CSA08 Assignment 1

**Student repository:** [poojasri47/CSA08-192220047-Assignment1](https://github.com/poojasri47/CSA08-192220047-Assignment1)

This repository contains Python programs demonstrating milk-rate calculation, input validation, payment calculation, farmer-level aggregation, JSON input, seasonal pricing, and testing for the Ksheera Village Milk Producers' Co-operative.

## Rules implemented
- Standard base rate: ₹30.00/L at 3.5% fat and 8.5% SNF.
- Each 0.1 percentage-point fat step changes the rate by ₹0.40.
- Each 0.1 percentage-point SNF step changes the rate by ₹0.30.
- Fat input is accepted from 2.0% through 7.0%.
- Money is calculated with `Decimal` and rounded to the nearest paisa.
- Seasonal example: base ₹32.00/L and ₹0.45 per 0.1% fat step; SNF remains ₹0.30 per 0.1% step.
- Seasonal bonus: ₹0.50/L when a farmer's total is **greater than** 500 L over the period.

**Important assumption:** The problem statement supplied here does not specify a permitted SNF range, so the program validates SNF as positive rather than inventing a range. Percentage values are mapped to the nearest 0.1 percentage-point step using `ROUND_HALF_UP`. Confirm this rounding rule with the assignment handout/instructor if another rule is specified.

## Project structure
```text
.
├── README.md
├── main.py
├── milkrate.py
├── inputs/
│   ├── sample_milk_data.json
│   └── seasonal_milk_data.json
├── tasks/
│   ├── task01.py ... task12.py
├── tests/
│   └── test_milkrate.py
└── outputs/
    ├── task01_output.txt ... task12_output.txt
    └── task01_output.png ... task12_output.png
```

## Run the programs
Python 3.10+ is recommended. No third-party packages are required for the programs.

From the project folder:
```bash
python main.py
python tasks/task01.py
python tasks/task02.py
# Continue with tasks/task03.py through tasks/task12.py
python -m unittest discover -s tests -v
```

## Task guide
1. Floating-point versus `Decimal` precision.
2. Rate calculation from fat and SNF.
3. Input validation and fat boundaries.
4. Payment for a single delivery.
5. Total litres and payment across deliveries.
6. Farmer-wise aggregation.
7. Reusable `milkrate.py` module imported by `main.py`/task program.
8. Representative correctness and boundary cases.
9. Aggregation over a larger batch of records.
10. Loading delivery records from JSON.
11. Seasonal pricing and volume bonus.
12. Integrated program using input records and farmer totals.

## Sample input
See `inputs/sample_milk_data.json` and `inputs/seasonal_milk_data.json`.

## Test results
Run the unit tests with `python -m unittest discover -s tests -v`. Text logs and terminal-style output images are in `outputs/`. The PNGs are rendered captures of the generated program output for documentation; rerun the scripts on your own computer if your instructor requires screenshots captured directly from your own IDE/terminal.

## Design notes
- `milkrate.py` contains reusable functions so pricing rules are implemented once.
- `Decimal` avoids binary floating-point inaccuracies in currency calculations.
- Farmer aggregation uses a dictionary keyed by farmer ID, so processing *n* deliveries is O(n) expected time and the summary requires O(f) space for *f* distinct farmers.
- Individual task programs are deliberately small demonstrations; the integrated workflow is in `main.py`.

## Submission checklist
- [ ] Review the exact assignment handout and confirm every task prompt matches the task descriptions in this README.
- [ ] Run all 12 task scripts and the unit tests locally.
- [ ] Upload the `.py` files, JSON inputs, README, test file, and outputs folder to GitHub.
- [ ] Replace this checklist with any course-specific requirements (student details, screenshots, UML, pseudocode, complexity analysis) your instructor explicitly requested.
- [ ] Make sure the repository visibility matches your instructor's instructions.
- [ ] Copy the final repository URL into the submission form.

## Academic integrity
Use this as a working project template: run it, compare it with your course handout, and make sure you can explain the code. Adapt the programs and documentation to the exact instructions and your own understanding before submission.
