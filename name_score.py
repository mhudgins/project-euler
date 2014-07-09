#!/usr/bin/python
# Author: mhudgins

# Problem taken from:
#   http://projecteuler.net/problem=22
#
# Problem: 
#   Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
#  For example, when the list is sorted into alphabetical order, COLIN, which is worth 3+15+12+9+14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714 
#
#   What is the total of all the name scores in the file?

names_file = open("names.txt","r")
names_str = names_file.read()
names_file.close()

# Convert the names into a format better suited for split and sort it.  
names_str = names_str.replace('"','')
names_list = names_str.split(',')
names_list = sorted(names_list)

total_name_score = 0
list_position = 1 
for name in names_list: 
  char_sum = 0
  for character in name:
    # Use ord() to return the ASCII value of a character. Subtract 64 to get the problem definition character value (A-65). 
    number = ord(character) - 64
    char_sum += number
  name_score = char_sum * list_position
  total_name_score += name_score 
  list_position += 1 

print "The total name score is: %d" % total_name_score 

