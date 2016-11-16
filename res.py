#! /usr/bin/python

import sys
import os
import parsedatetime
from datetime import datetime
import subprocess
from pytodo import duedate as dd
from pytodo import task as tt

if len(sys.argv) != 3:
    print("Invalid rescheduling arguments.")
    print("Usage: todo.sh res TASK_NUMBER NEW_DATE")
    exit()

task_no = sys.argv[1]
new_date_arg = sys.argv[2].lower()
task = tt.get_task(task_no)
task_date = dd.get_due_date(task)

if new_date_arg == "none":
    task = dd.remove_due_date(task)
else:
    cal = parsedatetime.Calendar()
    time_struct, parse_status = cal.parse(sys.argv[2])
    if parse_status == 1:
        new_date = datetime(*time_struct[:6]).date()
        if task_date == new_date:
            print("The new date is the same as the old one")
        else:
            task = dd.set_due_date(task, new_date)
            tt.update_task(task_no, task)
    else:
        print("New date could not be parsed")
