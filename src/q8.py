"""
Question 8 — Python: Find and Fix the Bug  [Short Answer — Write Code]

The function below is SUPPOSED to count how many even numbers are in a list.
It runs without crashing, but it returns the wrong answer.

    def count_evens(numbers):
        count = 0
        for n in numbers:
            if n % 2 == 1:      # <-- something here is wrong
                count = count + 1
        return count

    # Expected: 4  (the evens are 2, 4, 6, 8)
    print(count_evens([1, 2, 3, 4, 5, 6, 8]))

------------------------------------------------------------------
Task
------------------------------------------------------------------

(a) What does the buggy version actually return for [1, 2, 3, 4, 5, 6, 8], and why?

    Answer: 3, this is because 'n % 2 == 1' checks on odd numbers.

(b) Fix the bug. Write the corrected function below.
    (A one-character change is enough, but you must understand why.)
"""

def count_evens(numbers):
    # even number checks shold be n % 2 == 0 and 'pass' was removed as it is not required here
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count = count + 1
    return count


"""
(c) In one sentence, explain in plain English what `n % 2 == 0` checks.

    Answer: It checks for even numbers. % gives remainer after division. A remainer of 0 divided by 2 means the number divides evenly.
"""
