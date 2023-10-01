
# for i in range(10):
#     print(i)

# for i in range(5, 10):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# Additional homework problems

# 1. Write a function that takes in a string and returns a string made 
# from every other letter in the string. For example, given the string
# "hello", the function should return "hlo".
# def every_other(word):
#     output_string = ''
#     for i in range(0, len(word), 2):
#         output_string = output_string + word[i]
#     return output_string

# print(every_other('welcome'))

# 2. Write a function that takes in a string and returns a string made
# from the first three letters of the string. If the string is less than
# three letters long, the function should return the whole string. For
# example, given the string "hello", the function should return "hel".
def first_three(word):
    output_string = ''
    for i in range(0, 3):
        output_string = output_string + word[i]
    return output_string
print(first_three('hello'))

# 3. Write a function that takes in a string and returns a string made from
# every third letter in the string. For example, given the string
# "hellothere", the function should return "hlhe". Do this three different
# ways as we discussed in class.
