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

def task_exists(needle):
    cmd = "{:} ls".format(TODO_SH)
    lines = subprocess.check_output(cmd, shell=True).split('\n')
    for l in lines:
        if needle in l:
            return True
    return False

def add_task(task, due_date = None, duplicate = True):
    if due_date is not None:
        task = "due:{:%Y-%m-%d} {:}".format(due_date, task)    
    if not duplicate and task_exists(task):
        print(task)
        print("Task already exists. Nothing added.")
        return
    cmd = "{:} add {:}".format(TODO_SH, task)
    print(subprocess.check_output(cmd, shell=True).strip())

def update_task(task_no, new_task):
    cmd = "{:} replace {:} \"{:}\"".format(TODO_SH, task_no, new_task)
    print(subprocess.check_output(cmd, shell=True).strip())
