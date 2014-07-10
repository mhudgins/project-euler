#!/usr/bin/python
# Author: mhudgins

# Problem taken from:
#   http://projecteuler.net/problem=34    
# 
# Problem:
#   145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#   Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Store the factorial mappings to reduce recursive calls 
fact_dict = {}

def factorial(number):
  if number in fact_dict.keys():
    return fact_dict[number]
  else:
    if number == 1 or number == 0:
      return 1 
    else:
      return number*factorial(number-1)

sum_of_fact_numbers = 0 
for test_number in range(3,250000):
  fact_sum = 0 
  for digit in str(test_number):
    factorial_of_digit = factorial(int(digit))
    fact_sum += factorial_of_digit
    fact_dict[int(digit)] = factorial_of_digit
  if fact_sum == test_number: 
    sum_of_fact_numbers += fact_sum

print "The sum is: %d" % sum_of_fact_numbers 

