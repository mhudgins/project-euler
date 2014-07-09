#!/router/bin/python
# Author: mhudgins

# Problem taken from:
#   http://projecteuler.net/problem=17
#  
# Problem: 
#   If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#   If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

# Global dictionaries mapping numbers to their written expression. 

ones_place = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
tens_place = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
hundreds_place = {1:"one hundred",2:"two hundred",3:"three hundred",4:"four hundred",5:"five hundred",6:"six hundred",7:"seven hundred",8:"eight hundred",9:"nine hundred"}

def num_to_str_two_digit(number):
  if number < 20 and number > 9:
    return teens[number]
  else: 
    number_string = str(number)
    # Numbers which end in 0, ie. 20,30,40....
    if number_string[1] == '0':
      tens = tens_place[int(number_string[0])]
      return tens
    # Regular two digit numbers, ie. 21,31...
    else:
      tens = tens_place[int(number_string[0])]
      ones = ones_place[int(number_string[1])]
      return tens+'-'+ones

def num_to_str_three_digit(number):
  number_string = str(number) 
  # Whole hundreds, 100,200,300...
  if number_string[1] == '0' and number_string[2] == '0':
    return hundreds_place[int(number_string[0])]
  else:
    # Low hundreds, 101-109,201-209...
    if int(number_string[-2:]) < 10:
      return hundreds_place[int(number_string[0])]+" and "+ones_place[int(number_string[-2:])]
    # Regular three digit number, 102,103..199
    else:
      return hundreds_place[int(number_string[0])]+" and "+num_to_str_two_digit(int(number_string[-2:]))

# Return the letter count according to the problem definition
def letter_count(number):
  count = 0
  for char in str(number): 
    if char != ' ' and char != '-':
      count += 1
  return count

letter_count_sum = 0
for number in range(1,1001): 
  # 0-9 
  if len(str(number)) < 2:
    letter_count_sum += letter_count(ones_place[number])
  # 10-99 
  elif len(str(number)) < 3: 
    letter_count_sum += letter_count(num_to_str_two_digit(number))
  # 100-999
  elif len(str(number)) < 4:
    letter_count_sum += letter_count(num_to_str_three_digit(number))
  else: 
    letter_count_sum += letter_count("one thousand")

print "The sum of the letters is: %d" % letter_count_sum
