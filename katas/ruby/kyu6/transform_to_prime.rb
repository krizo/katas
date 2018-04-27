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
require 'spec_helper'

def minimum_number(numbers)
  sum = numbers.inject(&:+)
  0.step do |n|
    return n if is_prime(sum + n)
  end
end


def is_prime(number)
  return false if number % 2 == 0 && number > 2
  for i in (3..number - 1) do
    return false if number % i == 0
  end
  true
end
