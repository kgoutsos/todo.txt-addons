#! /usr/bin/python

import sys
from datetime import date, timedelta
from pytodo import duedate as dd

today = date.today()
week_list = {}

for line in sys.stdin:
    due = dd.get_due_date(line)
    if due is None or due < today or due >= today + timedelta(days=7):
        continue
    days = (due - today).days
    if days not in week_list:
        week_list[days] = []
    week_list[days].append(dd.remove_due_date(line.strip()))

for d in week_list:
    print("{:%A, %B %d}".format(today + timedelta(days=d)))
    print("============================")
    for t in week_list[d]:
        print(t)
    print("")
