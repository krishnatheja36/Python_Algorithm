"""
Access Control Badge Mismatch — Karat | Arrays & Hashing

Pattern: Hash Set tracking
  Scan badge records in order. Maintain an entry_set of people currently inside.
  On "exit": if person is NOT in entry_set, they exited without entering — flag them.
             if person IS in entry_set, remove them (normal exit).
  On "enter": add to entry_set.
  After all records: anyone still in entry_set entered but never exited — also flag.

Time:  O(n) — single pass through records
Space: O(n) — entry set + mismatch set
"""


def access_control_mismatch(badge_records):
    entry_set  = set()
    no_entry   = set()   # exited without entering

    for person, action in badge_records:
        if action == "exit":
            if person not in entry_set:
                no_entry.add(person)
            else:
                entry_set.discard(person)
        else:
            entry_set.add(person)

    no_exit = entry_set   # entered but never exited
    return sorted(no_entry), sorted(no_exit)


if __name__ == "__main__":
    records = [
        ["Martha", "exit"], ["Paul", "enter"], ["Martha", "enter"],
        ["Martha", "exit"], ["Jennifer", "enter"], ["Paul", "enter"],
        ["Curtis", "enter"], ["Paul", "exit"], ["Martha", "enter"],
        ["Martha", "exit"], ["Jennifer", "exit"],
    ]
    no_entry, no_exit = access_control_mismatch(records)
    print("Exited without entering:", no_entry)   # ['Martha']
    print("Entered without exiting:", no_exit)    # ['Curtis', 'Paul']
