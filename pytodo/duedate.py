from datetime import datetime

def get_due_date(line):
    if "due:" not in line:
        return None
    due = None
    parts = line.strip().split(' ')
    for p in parts:
        if p[0:4] == "due:":
            due = datetime.strptime(p.split(':')[1],"%Y-%m-%d").date()
            break
    return due

def set_due_date(line, new_date):
    if "due:" in line:
        parts = line.strip().split(' ')
        for i in range(0,len(parts)):
            if parts[i][0:4] == "due:":
                parts[i] = "due:" + "{:%Y-%m-%d}".format(new_date)
                break
        return " ".join(parts)
    else:
        return "{:} due:{:%Y-%m-%d}".format(line, new_date)

def remove_due_date(line):
    if "due:" not in line:
        return line
    parts = line.strip().split(' ')
    k = -1
    for i in range(0, len(parts)):
        if parts[i][0:4] == "due:":
            k = i
            break
    if k >= 0:
        del parts[k]
    return " ".join(parts)
