# Design, pseudocode, test table, and complexity

## UML-style module diagram
```text
+----------------------+       imports       +----------------------+
| tasks/task01..12.py  | ------------------> |      milkrate.py     |
+----------------------+                     | calculate_rate()     |
                                             | calculate_payment()  |
+----------------------+       imports       | farmer_bonus()       |
|       main.py        | ------------------> +----------------------+
+----------------------+             |
          | reads                     |
          v                           v
+----------------------+     +----------------------+
| inputs/*.json        |     | Decimal / validation |
+----------------------+     +----------------------+
```

## Pseudocode — standard payment
```text
READ litres, fat, SNF
IF fat is outside 2.0% to 7.0% OR SNF <= 0:
    REPORT validation error
fat_steps = nearest integer((fat - 3.5) / 0.1)
snf_steps = nearest integer((SNF - 8.5) / 0.1)
rate = 30.00 + fat_steps * 0.40 + snf_steps * 0.30
payment = round_to_paisa(litres * rate)
DISPLAY rate and payment
```

## Pseudocode — ten-day farmer summary
```text
INITIALIZE empty farmer_summary
FOR each delivery:
    calculate rate and payment
    add litres and payment to the record keyed by farmer ID
FOR each farmer:
    IF seasonal mode AND total litres > 500:
        bonus = total litres * 0.50
    ELSE:
        bonus = 0
    DISPLAY litres, milk payment, bonus, final payment
```

## Test table
| Test | Fat | SNF | Expected standard rate | Purpose |
|---|---:|---:|---:|---|
| Base | 3.5 | 8.5 | ₹30.00 | Base point |
| Fat +0.5 | 4.0 | 8.5 | ₹32.00 | Five fat steps |
| SNF +0.5 | 3.5 | 9.0 | ₹31.50 | Five SNF steps |
| Both | 4.0 | 8.7 | ₹32.60 | Fat and SNF changes |
| Lower fat boundary | 2.0 | 8.5 | ₹24.00 | Inclusive lower boundary |
| Upper fat boundary | 7.0 | 8.5 | ₹44.00 | Inclusive upper boundary |
| Invalid fat | 1.9 | 8.5 | Error | Below allowed range |
| Invalid SNF | 3.5 | 0 | Error | Non-positive SNF |

## Complexity
- Rate calculation: O(1) time and O(1) auxiliary space.
- Single payment: O(1) time and O(1) auxiliary space.
- Processing n deliveries and aggregating f farmers: O(n) expected time and O(f) summary space.
- Reading and parsing a JSON input with n deliveries: O(n) time and O(n) memory.
- Unit tests: O(t) time for t independent test cases.
