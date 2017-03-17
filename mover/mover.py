#! /usr/bin/python

import sys
from datetime import date
from pytodo import duedate as dd
from pytodo import task as tt

def isnumeric(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

for line in sys.stdin:
    due = dd.get_due_date(line)
    if due is None or due >= date.today():
        continue
    parts = line.strip().split(' ')
    task_no = parts[0]
    del parts[0]
    del parts[0]
    task = dd.set_due_date(" ".join(parts),date.today())
    tt.update_task(task_no, task)
    print("")
