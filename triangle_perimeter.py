#!/usr/bin/python
# Author: mhudgins

# Perimeterroblem taken from:
#   http://projecteuler.net/problem=39    
# 
# Perimeterroblem:

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

# Helper function to calculate the perimeter. 

def getPerimeter(triangle):
  return triangle[0] + triangle[1] + triangle[2]

# Use the pythagorean triples to generate all right trianges and keep track of the number of triangles whose perimeter meets a desired p value.  

triples = []
first = (3,4,5);
second = (5,12,13);
third = (8,15,17);
fourth = (7,24,25);
fifth = (20,21,29);

triples.append(first)
triples.append(second)
triples.append(third)
triples.append(fourth)
triples.append(fifth)

longest = []
optimal_perimeter = 0

for Perimeter in range(1,1200):
  answers = []
  for triple in triples:
    for i in range(1,Perimeter/2):
      new = (triple[0]*i,triple[1]*i,triple[2]*i)
      perimeter = getPerimeter(new)
      if perimeter == Perimeter:
        answers.append(new)
      if perimeter > Perimeter:
        break
  if len(answers) > len(longest):
    longest = answers
    optimal_perimeter = Perimeter

print optimal_perimeter 
