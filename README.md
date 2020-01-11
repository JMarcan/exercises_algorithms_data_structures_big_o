# Investigating_Texts_and_Calls

## Project description
In this project I've implemented code,
to analyze dataset of phone calls and texts,
and for each solution performed its run time complexity analysis (Worst Case Big O Notation).

This project was completed as part of my Data Structures & Algorithms Nanodegree at Udacity.

![comparison of computational complexity](comparison_computational_complexity.png)

## Tasks description
### Task 0
- What is the first record of texts and what is the last record of calls
- Run time complexity of my solution: `O(0n + 1)` = `O(1)` | where n = count of records (count of records for calls + count of records for texts)

### Task 1
- How many different telephone numbers are there in the records
- Run time complexity of my solution: `O(n)` | where n = count of records (count of records for texts)

### Task 2
- Which telephone number spent the longest time on the phone
- Run time complexity of my solution: `O(n)` | where n = count of records (count of records for calls)

### Task 3
- Find all of the area codes and mobile prefixes called by people in Bangalore. 
- What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore
- Run time complexity of my solution: `O(n)` | where n = count of records (count of records for calls)

### Task 4
- Create a set of possible telemarketers: these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.
- Run time complexity of my solution: `O(n)` | where n = count of records (count of records for calls + count of records for texts)

## Usage
The project only purpose was my training,
however the code can be downloaded and directly run for each task in its own file.

## Files in the repository
- `Task0.py`: Implemented code for task 0
- `Task1.py`: Implemented code for task 1
- `Task2.py`: Implemented code for task 2
- `Task3.py`: Implemented code for task 3
- `Task4.py`: Implemented code for task 4
- `Analysis.txt`: Run time complexity analysis for each task (Worst Case Big O Notation)
- `calls.csv`: Analyzed calls data. The following columns are present: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
- `texts.csv`: Analyzed text data. The following columns are present: sending telephone number (string), receiving telephone number (string), timestamp of text message (string)

## Libraries used
Python 3