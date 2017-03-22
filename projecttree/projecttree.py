#! /usr/bin/python

import sys
import re
import os

PROJECT_REGEX = "\+\S*/?\S* ?"
INDENT_STRING = "    "

ansiRegex = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
priorityRegex = re.compile(r'^(\([A-Z]\)) ')
addDateRegex = re.compile(r'[0-9]{4}-[0-1][0-9]-[0-3][0-9] ')

def cleanupTask(task):
    task = priorityRegex.sub("", task)
    return addDateRegex.sub("", task)

tasks = {}
for line in sys.stdin:
    line = ansiRegex.sub("", line).strip()
    if line == "" or line == "--" or line[0:4] == "TODO:":
        continue
    match = re.search(PROJECT_REGEX, line)
    if match:
        task = re.sub(PROJECT_REGEX, "", line)
        project = match.group()[1:]
        if project not in tasks:
            tasks[project] = []
        tasks[project].append(task)

projects = sorted(tasks.keys())
separator = "-" * max(len(p) for p in projects)

for p in projects:
    tasks[p] = sorted(tasks[p])
    indent = INDENT_STRING * p.count("/")
    print("%s%s" % (indent, p))
    print("%s%s" % (indent, separator))
    for t in tasks[p]:
        print("%s%s%s" % (indent, INDENT_STRING, cleanupTask(t)))
    print("")
