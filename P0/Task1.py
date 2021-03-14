"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_telephones = set()
   
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        unique_telephones.add(text[0])
        unique_telephones.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        unique_telephones.add(call[0])
        unique_telephones.add(call[1])

message = f'There are {len(unique_telephones)} different telephone numbers in the records.'
print(message)
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
