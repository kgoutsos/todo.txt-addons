#!/bin/bash

[ "$1" = "usage" ] && exit 0

shift

TASK=$(sed "$1!d" "$TODO_FILE")
"$TODO_SH" command do "$@"
python "$TODO_ACTIONS_DIR"/recur.py "$TASK"
