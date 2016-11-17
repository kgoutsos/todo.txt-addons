#! /usr/bin/python
import os, os.path
import subprocess
import sys
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from pytodo import task as tt
from pytodo import duedate as dd

RECUR_TXT = os.environ['TODO_DIR'] + "/recurring.txt"

def add_months(sdate, months):
    y = sdate.year + (sdate.month + months)/12
    return date(y, (sdate.month + months) % 12, sdate.day)

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

if not os.path.isfile(RECUR_TXT):
    print("File recurring.txt not found at {:}/\nExiting...".format(os.environ['TODO_DIR']))
    exit()

old_task = sys.argv[1]
tdate = dd.get_due_date(old_task)
old_date = tdate if tdate is not None else date.today()
if old_date < date.today():
    old_date = date.today()
old_task = ' '.join(dd.remove_due_date(old_task).split(' ')[1:])

flag = False
f = open(RECUR_TXT, 'r')
for line in f:
    if line[0] == "#" or line.strip() == "":
        continue

    lps = line.split(":")
    if len(lps) != 2:
        print("Failed parsing " + line)
        continue

    rcmd = lps[0].lower().strip()
    task = lps[1].strip()

    if task != old_task:
        continue

    flag = True
    print("Task was found in the recurring list, adding it again...")

    if rcmd == "daily":
        next_date = old_date + relativedelta(days = +1)
    elif rcmd[0:3] == "day":
        next_date = old_date.replace(day = int(rcmd[4:]))
        if next_date <= old_date:
            next_date = next_date + relativedelta(months = +1)
    elif rcmd[0:6] == "months":
        months = int(rcmd.split(' ')[1])
        start = datetime.strptime(rcmd.split(' ')[2],'%Y-%m-%d').date()
        next_date = start
        while(next_date <= date.today()):
            next_date = next_date + relativedelta(months = +months)
    elif rcmd in days:
        weekday = days.index(rcmd)
        days_ahead = weekday - date.today().weekday()
        if days_ahead <= 0:
            days_ahead += 7
        next_date = old_date + relativedelta(days = +days_ahead)
        if next_date == date.today():
            next_date = next_date + relativedelta(weeks = +1)

    tt.add_task(task, next_date, False, True)

f.close()
if flag:
    print("[{:%c}] todo.txt recurring task operations completed.".format(datetime.now()))
