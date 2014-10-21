#!/usr/bin/python 

# Problem taken from:
#   https://projecteuler.net/problem=41
# Problem:
#   We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#   What is the largest n-digit pandigital prime that exists?

import math
# Recusive function to calculate the permutations (pandigital) of the string in tail. Adds the strings to the global permutations list.

# perm("","ab") = perm(a,b) = perm(ab,"") => base case
#               = perm(b,a) = perm(ba,"") => base case
#
permutations = []

def perm(head,tail):
  if len(tail) == 0:
    global permutations
    permutations.append(head)
  else:
    for i in range(0,len(tail)):
      perm(head + tail[i],tail[0:i] + tail[i+1:len(tail)])

# Returns 1 if the number is prime and 0 otherwise.  If the number is odd, then we check if its evenly divisible from numbers 2 through its square root.
def isPrime(number):
  if number == 1 or number == 2:
    return 1
  if number % 2 == 0:
    return 0
  else:
    for i in range(2,int(math.sqrt(number))):
      if number % i == 0:
        return 0
    return 1

# Brute force approach. Generate all n palindromes and keep track of the biggest prime.
digits = ""
biggest_nth_prime_pandigital = 1
for i in range(1,8):
  digits += str(i)
  perm("",digits)
  for permutation in permutations:
    if isPrime(int(permutation)):
      if int(permutation) > biggest_nth_prime_pandigital:
        biggest_nth_prime_pandigital = int(permutation)

print biggest_nth_prime_pandigital
