import sys
from datetime import date, timedelta
from pytodo import duedate as dd

we = date.today() + timedelta(days=7)

for line in sys.stdin:
    due = dd.get_due_date(line)
    if due is None:
        continue
    if due < we:
        print(line.strip())
