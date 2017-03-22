#! /usr/bin/python

import sys
import re
import os

indentString = "    "
projectRegex = re.compile(r'\+\S*/?\S* ?')
ansiRegex = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
priorityRegex = re.compile(r'^(\([A-Z]\)) ')
taskNumberRegex = re.compile(r'^[0-9]+ ')
addDateRegex = re.compile(r' [0-9]{4}-[0-1][0-9]-[0-3][0-9] ')

def cleanupTask(task):
    task = priorityRegex.sub("", task)
    task = addDateRegex.sub(" ", task)
    return task

tasks = {}
for line in sys.stdin:
    line = ansiRegex.sub("", line).strip()
    if line == "" or line == "--" or line[0:4] == "TODO:":
        continue
    match = projectRegex.search(line)
    if match:
        task = projectRegex.sub("", line)
        project = match.group()[1:]
        if project not in tasks:
            tasks[project] = []
        tasks[project].append(task)

projects = sorted(tasks.keys())
separator = "-" * max(len(p) for p in projects)

for p in projects:
    tasks[p] = sorted(tasks[p])
    indent = indentString * p.count("/")
    print("%s%s" % (indent, p))
    print("%s%s" % (indent, separator))
    for t in tasks[p]:
        print("%s%s%s" % (indent, indentString, cleanupTask(t)))
    print("")
