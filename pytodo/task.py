import subprocess
import os

TODO_SH = "{0} -d {1}".format(os.environ['TODO_FULL_SH'], os.environ['TODOTXT_CFG_FILE'])

def get_task(task_no):
    cmd = "{:} ls".format(TODO_SH)
    lines = subprocess.check_output(cmd, shell=True).split('\n')
    task = None
    for l in lines:
        parts = l.split(' ')
        if len(parts) < 2:
            continue
        if int(parts[0]) == int(task_no):
            del parts[0]
            del parts[0]
            return " ".join(parts)

def add_task(task, due_date = None):
    if due_date is None:
        cmd = "{:} add {:}".format(TODO_SH, task)
    else:
        cmd = "{:} add due:{:%Y-%m-%d} {:}".format(TODO_SH, due_date, task)
    print(subprocess.check_output(cmd, shell=True).strip())

def update_task(task_no, new_task):
    cmd = "{:} replace {:} \"{:}\"".format(TODO_SH, task_no, new_task)
    print(subprocess.check_output(cmd, shell=True).strip())
