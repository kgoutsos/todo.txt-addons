import os, os.path
import subprocess
from datetime import date, datetime
from pytodo import task as tt

RECUR_TXT = os.environ['TODO_DIR'] + "/recurring.txt"

def add_months(sdate, months):
    y = sdate.year + (sdate.month + months)/12
    return date(y, (sdate.month + months) % 12, sdate.day)

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

if not os.path.isfile(RECUR_TXT):
    print("File recurring.txt not found at {:}/\nExiting...".format(os.environ['TODO_DIR']))
    exit()

f = open(RECUR_TXT, 'r')
for line in f:
    if line[0] == "#":
        continue

    lps = line.split(":")
    if len(lps) != 2:
        print("Failed parsing " + line)
        continue

    rcmd = lps[0].lower().strip()
    task = lps[1].strip()
    if rcmd == "daily":
        tt.add_task(task, date.today())
    elif "day" in rcmd and rcmd[4:] == date.today().strftime("%d").lower():
        tt.add_task(task, date.today())
    elif "month" in rcmd:
        parts = rcmd[6:].split(' ')
        if add_months(datetime.strptime(parts[1],'%Y-%m-%d').date(), int(parts[0])) == date.today():
            tt.add_task(task, date.today())
    elif rcmd in days and rcmd == date.today().strftime("%A").lower():
        tt.add_task(task, date.today())

f.close()
