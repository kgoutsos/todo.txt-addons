# Recurring Tasks (recur)

The recur script expects one task per line in the format `<recurring option>: <task string (without creation or due dates)>`
Lines starting with # are ignored.

The script does not check for existing tasks so it should be executed only once per day to avoid duplicate tasks. Usually, it is convenient to schedule the script to automatically run daily (i.e. as a cron job).

The following options are supported:
* `daily`: Runs daily.
* `day <number>`: 'number' is the number of a day in a month (i.e. 23) Runs every month on the specified day.
* `<dayname>`: 'dayname' it a full day name in English (i.e. Monday). Runs every week on the specified day.
* `month <number> <start date>`: 'number' is the number of months between each run and 'start date' is the starting date of the recurring task in YYYY-MM-DD format.

## Example reccuring.txt
```
# Runs every day
daily: Do the dishes @home
# Runs on the 5th day of every month
day 5: Pay the rent @home
# Runs every Saturday
saturday: Grocery shopping @town
# Runs every second month starting from May 1st, 2016
month 2 2016-05-01: Verify backups
```
