import sys
import os
import dateparser
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
    new_date = dateparser.parse(sys.argv[2])
    if new_date == None:
        print("New date could not be parsed")
        exit()
    new_date = new_date.date()
    if task_date == new_date:
        print("The new date is the same as the old one")
        exit()

    task = dd.set_due_date(task, new_date)

tt.update_task(task_no, task)
