#!/bin/bash

# v0.0.1

action=$1
no=$2
new_date=$3
shift

[ "$action" = "usage" ] && {
  echo ""
  echo "  Reschedule tasks:"
  echo "    res ITEM# DATE"
  echo "      reschedules the task with number ITEM# to the specified date."
  echo "      The DATE argument can be in most date formats or in natural language i.e. 'today', 'tomorrow', 'in 2 days'."
  exit
}
[ "$action" = "res" ] && {
    python $TODO_ACTIONS_DIR/res.py $no "$new_date"
}
