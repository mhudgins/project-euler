#!/usr/bin/python 
# Author: mhudgins

# Problem taken from:
#   http://projecteuler.net/problem=25
#
# Problem:
#   What is the first term in the Fibonacci sequence to contain 1000 digits?

# Store the returns of fib_of_n to cut down on the recursion calls 
fib_dict = {}

def fib_of_n(n): 
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else: 
    if n in fib_dict.keys(): 
      return fib_dict[n]
    else:
      return fib_of_n(n-1) + fib_of_n(n-2)

for number in range(3,5000):
  fib = fib_of_n(number)
  if len(str(fib)) > 999:
    print "The first Fibonacci term with at least 1,000 digits is: %d" % number 
    break
  fib_dict[number] = fib 

