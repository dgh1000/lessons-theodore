# Reversed strings
# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

# Here's the problem statement from codewars:

# def solution(string):
#   pass
# print(solution('foo'))

# But I don't want you to try to write this function
# right away. Instead we will work through the concepts
# one at a time.

# Here are some hints about the problem above.
# First, let's build a string one character at 
# a time. Uncomment this code and run it.
# the first line was nothing then the
# second line 
number = 1
# have an assignment statement, we plug into
# the variables on the right side
# x is 3 and y is 4, what is x + y?
# what is the current value of number? 
#
# How does the computer interpret an assignment
# statement? Always has a variable on the left
# side of the equals. Has an expression on the
# right side. It computes the value of the 
# expression and makes the variable on the left
# side equal to that value. To compute the
# value, it plugs in the current value of
# the variables
x = 3
y = 7
z = y + x # doesn't change the answer
#   ^ plugged in for x: current value which is
#     3
#       ^ plugged in for y: 7
# 
# + with strings
y = "h"
y = "e" + y
print(y)


# my_string = "" # empty string
# my_string = "h" + my_string
# my_string = "e" + my_string
# my_string = "l" + my_string
# my_string = "l" + my_string
# my_string = "o" + my_string
# print(my_string)

# Question #0: review what the + symbol does with strings. Try
#    a few of your own examples if you'd like.
# Question #1: What order did we add the letters to the string?
# Question #2: What order got printed out?

# Now we'll do this in a loop. 
# First uncomment this and run it. 
# 

def reverser(word):
    output_string = ''
    for i in range(len(word)):
        # print the character at index i
        # print(other_string[i])
        # add the character at index i to the output string
        
        output_string = word[i] + output_string 
    return output_string
# functions that return values are more flexible than functions
# that print values
print(reverser(reverser('abcdefg')))

# Question #3: Explain what the code above does and why it's doing that.
# In particular review what len(other_string) does.

# Now we'll use the loop to build a string.
# Uncomment this code and run it.
# other_string = "hello"
# my_string = ""
# # effect of range()
# for i in range(len(other_string)):
#     # i goes from 0 to 4
#     print(other_string[i])
#     # my_string = my_string + other_string[i]
# print(my_string)

# Question #4: Explain what the code above does. What does the
# + symbol on line 36 do when used with strings? Look at question
# #0 if you need a reminder. 

# Question #5: now for the challenging question. What can you 
#   do to the code above to make it print the string backwards?
#   In particular look at line 38. What can you change there to
#   make the string print backwards?

# Question #6: now enter the finished program in Codewars and 
# check that it passes the tests.
