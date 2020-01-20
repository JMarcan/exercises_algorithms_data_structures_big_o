# Investigating_Texts_and_Calls

## Project description
This project was completed as part of my Data Structures & Algorithms Nanodegree at Udacity,
that I took to ensure that my code is written efficiently. This is especially important for solutions that needs to be scaled. Or solutions with limited computing power. As robots.

In this project I've implemented code,
to analyze dataset of phone calls and texts,
and for each solution performed its run time and space complexity analysis (Worst Case Big O Notation).

![comparison of computational complexity](comparison_computational_complexity.png)

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

## Tasks description
### Task 0
* What is the first record of texts and what is the last record of calls?

* Solution to complete Task 0 has:
    * Time complexity: `O(1)` as we print the first and the last record, we execute always two prints, no matter how much records we have
    * Space complexity: `O(1)` as we print the first and the last record, we store them to two string variables, no matter how much records we have
    * Design choice:
    
        I prioritize readibility for a user, 
        so in the first part we store the first record in variable, then the last record one to second variable.
        Then in the print statement we pass those variables as arguments

### Task 1
* How many different telephone numbers are there in the records?

* Solution to complete Task 1 has:
    * Time complexity: `O(n)` as we loop through each record
    * Space complexity: `O(n)` as in the worst case each new record represents an unique number we need to store
    * Design choice: 
    
        To store unique numbers, set structure was used instead of List as it's the most efficient, 
        and we don't care about order of items to calculate total count of unique numbers.
           
        When testing whether we already stored the given number, set works with hash tables,
        it just looks whether the object is at the position determined by its hash,
        so the speed of this operation does not depend on the size of the Set.
        In contrast, for List the whole List would need to be searched,
        which would provide us with worse performance than with Set structure.


    [n = count of records (count of records for calls + count of records for texts)]

### Task 2
* Which telephone number spent the longest time on the phone?
* Solution to complete Task 2 has:
    * Time complexity: `O(n)` as we loop through each record  
    * Space complexity: `O(n)` as in the worst case each new record represents an unique number we need to store
    * Design choice:
    
        To store how much time each number spent by calling,
        Dictionary structure was choosen.  As we store key value pars between phone number and time spent by calling.    
     
    [n = count of records (count of records for calls)]

### Task 3
* Find all of the area codes and mobile prefixes called by people in Bangalore. 
* What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore?
* Solution to complete Task 3 has:
    * Time complexity: `O(n log n)` as  we use `.sort()` function with time complexity [O(n log n)](https://wiki.python.org/moin/TimeComplexity)
            and in the worst case each new record represents an unique area code we need to store and sort
            Looping through each record itself has time complexity `O(n)` 
                
    * Space complexity: `O(n)` as in the worst case each new record represents an unique area code we need to store
    * Design choice: 
    
        To store unique area codes,  and later display them in lexicographic order,
        List structure was choosen, as it allows us to sort list by lexicographic order by calling .sort()
    
    [n = count of records (count of records for calls)]

### Task 4
* Create a set of possible telemarketers: these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.
* Solution to complete Task 4 has complexity:
    * Time complexity: `O(n log n)` as  we use `.sort()` function with time complexity [O(n log n)](https://wiki.python.org/moin/TimeComplexity)
            and in the worst case each new record represents a possible telemarketer we need to store  and sort
            Looping through each record itself has time complexity `O(n)` 
    * Space complexity: `O(n)` as in the worst case each new record represents a possible telemarketer we need to store 
      
    * Design choice:
    
        To store list of possible telemarketers,  and later display them in lexicographic order,
        List structure was choosen, as it allows us to sort list by lexicographic order by calling .sort()  
    
    [n = count of records (count of records for calls + count of records for texts)]