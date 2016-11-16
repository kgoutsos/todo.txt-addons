# Collection of todo.txt Addons

_These addons are the result of very quick and dirty coding, they are working for me but they are in no way fully tested or optimised_

## Installation
Just clone the repository in your todo.txt action directory (by default at ~/.todo.actions.d/) and enjoy!

Prerequisites: todo.txt, python 2+

## Contents & Usage
A small collection of helper functions is contained in pytodo/ as those functions came up more often than not.

### Actions
Actions are usually made up of two files: a bash script (without an extension) and a python script. The bash script interacts with todo.txt and uses the python script to perform more complex functions.

* `todo.sh res ITEM# DATE`: reschedules the task with number ITEM# to the specified date. The DATE argument can be in most date formats or in natural language i.e. 'today', 'tomorrow', 'in 2 days'. DATE needs to be quoted in case it spans more than one words.
* `todo.sh week`: prints a list of the tasks due in the next 7 days grouped by day.
* `todo.sh mover`: reschedules all overdue tasks to the current date.
* `todo.sh recur`: when executed, adds the appopriate tasks from recurring.txt (in the same directory as todo.txt) with the appropriate due dates. See README-RECUR.md for details.

### Filters
Filters operate on the standard I/O, reading the input from todo.sh and producing the output. todo.txt support the use of custom filters via the environment variable TODOTXT_FINAL_FILTER which can be set to any script operating on the standard I/O.

When this variable is set, the output `todo.sh ls` will be filtered by the specified script. The filtering is done on a per-line basis and the output of the filter is fed back to todo.sh.

* week-filter.py: shows tasks due in the next 7 days.
* overdue-filter.py: shows overdue tasks only.

Usually, you wouldn't want the filters to be applied every time `todo.sh ls` is run. In that case the environment variable can be temporarily set with the `env` command: `env TODOTXT_FINAL_FILTER=week-filter.py todo.sh ls`. This makes it easy to setup aliases for filtered views: `alias tw="env TODOTXT_FINAL_FILTER=week-filter.py todo.sh ls"`

## Notes
The paths to executable files have been simplified for clarity. In reality you have to either add todo.sh and the filters to your PATH or include the full paths to your commands i.e. `env TODOTXT_FINAL_FILTER=$HOME/.todo.actions.d/week-filter.py todo.sh ls`

Due dates are represented with a "due:<date>" field in the respective task. The field is case sensitive (lowercase) and the date format used is YYYY-MM-DD mainly for sorting purposes.

In order to enable better sorting, the due date appears first in the tasks directly after the line number and the creation date (if any). Thus, when adding a due date the addons will add it as a prefix. However, if a due date already exists, they will edit it in place.
