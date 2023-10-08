

my_list = [6, 1, -2, 3, 10, 13]

# Here is a demonstration of indexing or subscripting the list: (please
# write down the words indexing and subscripting to help you remember them)

# EXAMPLE A:

# Uncomment and run this code. Before you
# run it, predict what it will do.
# print(my_list[0])

# Question 1: 
# Explain in your own words what the code on line 8 does.
# - Because zero is the start of numbers in python it takes the start
# of the numbers in the list and prints it

# Question 2:
# Which of the values on line 8 is the "subscript" or "index"?
# - the [] is the subscript and the zero in it is the index
# the brackets indicate that subscripting will be happening

# Question 3:
# What "syntax" is used to subscript a list? In other words, 
# what characters are used and where do they go?
# - this [] and a number that chooses which one, they go inside the print parenthesis next to the variable your calling to print

# Question 4:
# Write a line of code that will print the value 10 from the list.
# Figure what index you need, and then write the code.
# print(my_list[4])
# EXAMPLE B:

# Now we will address the topic of what you need to do to print 
# several items in a row from the list. You can start like this:
# Uncomment this code and run it. First predict what it will do.
# it will print 6, 1 and -2

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])

# Question 5:
# Modify the code on lines 28 through 30 to print the values
# 3, 10, and 13 from the list.
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# EXAMPLE C:

# Uncomment the following code and run it. First see if
# you can predict what it will do. You may not remember 
# it or perhaps we haven't done it before.

# print(my_list[0:3])

# Question 6:
# Explain in your own words what the code on line 48 does.
# It prints the values between 0 and 3
# EXPLANATION
# syntax of slicing is [start:end] the brackets and a colon
#
# 
# This syntax is called "slicing" a list. It is a way to
# get a section of a list. The first number is the starting
# index and the second number is the ending index. The
# ending index is not included in the slice. So in this
# example, the slice starts at index 0 and ends at index 2.
# The value at index 3 is not included.

# Question 7:
# What is different between the values printed in EXAMPLE B
# and the values printed in EXAMPLE C?
# B has multiple lines, c has one
# Question 8:
# Modify the code on line 48 to print the values 3, 10, and 13.
# What's the last index you need to include? What should the 
# second number be in the slice?
# 3, 4, and 5
# print(my_list[3:6]) # one past the last index or 6
# EXAMPLE D:

# Uncomment the following code and run it. First see if


# Uncomment the following code and run it. First see if you
# can predict what it will do. Note this involves list
# concatenation. We did this in lists/list-plus-01.py

my_list = [6, 1, -2, 3, 10, 13, 15, -1, -10, 14]
# notice how if I omit second number I don't need to know
# where the list ends (i.e. how long it is).

# print(my_list[::-1])

sentence1 = "Sphinx of black quartz, judge my vow."
#            0123456789
sentence2 = "The quick brown fox jumps over the lazy dog."
print(sentence1[::2])

# Question 9:
# Explain in your own words what the code on line 78 does. 

# Question 10:
# Modify the code on line 78 to print the list
# [6, 1, 3, 10]

# To review, Here is a copy of the line above that assigns 
# my_list:
