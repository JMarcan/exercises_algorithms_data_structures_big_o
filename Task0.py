"""
Read file into texts and calls.
"""

import csv


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
    # store the first text line, so it can be later printed for Task 0
    first_text = texts[0]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
    # store the first calls line, so it can be later printed for Task 0
    first_call = calls[0]


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, <{0}> texts <{1}> at time <{2}>".format(first_text[0], first_text[1], first_text[2]))
print("First record of calls, <{0}> calls <{1}> at time <{2}>".format(first_call[0], first_call[1], first_call[2]))

