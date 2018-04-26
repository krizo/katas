"""
https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""


def expanded_form(num):
    pow = 0
    numbers = []
    for digit in reversed(str(num)):
        if digit != '0':
            numbers.append(str(int(digit) * (10 ** pow)))
        pow += 1
    return " + ".join(list(reversed(numbers)))
