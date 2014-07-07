#!/usr/bin/python

# Author: mhudgins 
# Solution to projecteuler.net problem 13, longest collatz sequence from seed numbers below one million.
# Problem description: https://projecteuler.net/problem=14

longest_seq_seen = 0

for starting_number in range(1,1000000):
  sequence_number = starting_number
  sequence_count = 1 
  while sequence_number > 1:
    if sequence_number % 2:
      sequence_number = (3*sequence_number) + 1 
    else:
      sequence_number = sequence_number/2
    sequence_count += 1
  if sequence_count > longest_seq_seen:
    longest_seq_seen = sequence_count 

print("The longest collatz sequence between one and a million is: %d.") % longest_seq_seen
