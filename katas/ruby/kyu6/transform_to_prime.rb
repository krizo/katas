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
require 'prime'

def minimum_number(numbers)
  sum = numbers.reduce(0, :+)
  #sum = numbers.sum  <- ruby 2.4+
  Prime.find { |prime| prime >= sum } - sum
end
