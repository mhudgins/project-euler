#!/usr/bin/python 
# Author: mhudgins 

# Problem taken from:
#   https://projecteuler.net/problem=36
#   
# Problem:
#   The decimal number, 585 = 1001001001 (base 2) is palindromic in both bases.
#   Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

import math

#  Returns true if the given string is a palindrome 
def is_palindrome(string):
  # Strings are immutable in Python, so create a list of characters to work with
  char_list = []
  char_list.extend(string)
  j = len(char_list) - 1 
  for index in range(0,len(char_list)-1):
    if j < index:
      break
    tmp = char_list[index]
    char_list[index] = char_list[j]
    char_list[j] = tmp
    j -= 1
  if string == ''.join(char_list):
    return 1

def decimal_to_binary(number):
  string = ""
  while number > 0:
    bit = number % 2 
    number /= 2
    if bit == 1:
      string = '1' + string
    else:
      string = '0' + string 
  return string 

sum_of_all_palindromes = 0
double_base_palindromes = []
for test_number in range(1,1000001):
  if is_palindrome(str(test_number)) and is_palindrome(str(decimal_to_binary(test_number))):
    sum_of_all_palindromes += test_number 
    double_base_palindromes.append(test_number)

print "The sum of all double base palindromes is: %d" % sum_of_all_palindromes
print "The double base palindrome numbers are: [%s]" % ', '.join(map(str, double_base_palindromes))
