#! /usr/bin/python

import sys
from datetime import date
from pytodo import duedate as dd

for line in sys.stdin:
    due = dd.get_due_date(line)
    if due is None:
        continue
    if due < date.today():
        print(line.strip())
