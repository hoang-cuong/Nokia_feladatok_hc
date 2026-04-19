from pathlib import Path

from datetime import datetime

def calculate_parking_fee(entry: datetime, exit: datetime) -> int:

    if exit < entry:
        raise ValueError("A kilépési idő nem lehet korábbi a belépéi időnél!")

    duration_minutes = (exit - entry).total_seconds() / 60

    if duration_minutes <= 30:
        return 0

    full_days = int(duration_minutes // (24 * 60))

    remaining_minutes = duration_minutes % (24 * 60)

    fee = full_days * 10000

    if remaining_minutes <= 30:

        pass
    elif remaining_minutes <= 30 + 3 * 60:

        billable_minutes = remaining_minutes - 30

        fee += (billable_minutes/60) * 300
    else:

        fee += 3 * 300

        billable_minutes = remaining_minutes - 30 - 3 * 60

        fee += (billable_minutes / 60) * 500

    return round(fee)

def main():
    data = Path("parking_calculator/input.txt").read_text(encoding="utf-8")
    sorok = data.splitlines()

    eredmenyek = []

    for sor in sorok[2:]:
        sor = sor.strip()
        if not sor:
            continue

        parts = sor.split()

        if len(parts) < 5:
            continue

        plate = parts[0]

        entry_str = parts[1] + " " + parts[2]

        exit_str = parts[3] + " " + parts[4]

        try:
            entry = datetime.strptime(entry_str, "%Y-%m-%d %H:%M:%S")

            exit = datetime.strptime(exit_str, "%Y-%m-%d %H:%M:%S")

            fee = calculate_parking_fee(entry, exit)

            eredmenyek.append(f"{plate}\t{fee} Ft")

        except ValueError as e:
            eredmenyek.append(f"{plate}\tHIBA: {e}")

    kimenet = "\n".join(eredmenyek)

    print(kimenet)

    Path("output.txt").write_text(kimenet, encoding="utf-8")

if name == "main":
    main()