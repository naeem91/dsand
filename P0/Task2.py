"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

call_times = defaultdict(int)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        caller1 = call[0]
        caller2 = call[1]
        call_duration = int(call[3])
        
        call_times[caller1] += call_duration
        call_times[caller2] += call_duration

longest_time_on_phone = 0
longest_callers_phone = ''

for caller, duration in call_times.items():
    if duration > longest_time_on_phone:
        longest_time_on_phone = duration
        longest_callers_phone = caller

message = f'{longest_callers_phone} spent the longest time, {longest_time_on_phone} seconds, on the phone during September 2016.'
print(message)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

