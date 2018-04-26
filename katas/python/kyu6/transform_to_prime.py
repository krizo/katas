"""
http://www.codewars.com/kata/transform-to-prime

Task :
Given a List [] of n integers , find minimum mumber to be inserted in a list, so that sum of all elements of list should equal the closest prime number .

Notes
List size is at least 2 .

List's numbers will only positives (n > 0) .

Repeatition of numbers in the list could occur .

The newer list's sum should equal the closest prime number .

Input >> Output Examples
1- minimumNumber ({3,1,2}) ==> return (1)

"""


def minimum_number(numbers):
    number_to_insert = 0
    while True:
        if is_prime(sum(numbers) + number_to_insert):
            return number_to_insert
        number_to_insert += 1


def is_prime(number):
    if number % 2 == 0 and number > 2:
        return False
    for i in range(3, number):
        if number % i == 0:
            return False
    return True
