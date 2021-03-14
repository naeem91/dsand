"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv



text_senders_receivers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        text_senders_receivers.add(text[0])
        text_senders_receivers.add(text[1])

possible_telemarketers = set()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    callers = set()
    receivers = set()
    
    for call in calls:
        callers.add(call[0])
        receivers.add(call[1])

    for caller in callers:
        if not caller in receivers and not caller in text_senders_receivers:
            possible_telemarketers.add(caller)

message = 'These numbers could be telemarketers:'
print(message, *sorted(possible_telemarketers), sep='\n')
    
    
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

