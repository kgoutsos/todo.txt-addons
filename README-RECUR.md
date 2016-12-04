# Recurring Tasks (recur)

The recur script expects one task per line in the format `<recurring option>: <task string (without creation or due dates)>`
Lines starting with # are ignored.

The script does check for existing tasks to avoid duplicate tasks. Usually, it is convenient to schedule the script to automatically run daily (i.e. as a cron job). It is designed to run upon task completion or deletion (see `do` and `del` scripts) which means that the first occurence of the tasks has to be manually added to the todo file.

The following options are supported:
* `daily`: Runs daily.
* `day <number>`: 'number' is the number of a day in a month (i.e. 23) Runs every month on the specified day.
* `<dayname>`: 'dayname' it a full day name in English (i.e. Monday). Runs every week on the specified day.
* `months <number> <start date>`: 'number' is the number of months between each run and 'start date' is the starting date of the recurring task in YYYY-MM-DD format.

## Example reccuring.txt
```
# Runs every day
daily: Do the dishes @home
# Runs on the 5th day of every month
day 5: Pay the rent @home
# Runs every Saturday
saturday: Grocery shopping @town
# Runs every second month starting from May 1st, 2016
months 2 2016-05-01: Verify backups
```
