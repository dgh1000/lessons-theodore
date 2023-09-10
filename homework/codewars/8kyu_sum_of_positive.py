# Codewars kata: 8kyu Sum of positive
# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
# def positive_sum(arr):
#     total = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             total += arr[i]
#     return total
# print(positive_sum([1,1,-900,6,-20]))



# Extra homework:

# 1. given an array of number, return the sum of every other number
#    def sum_every_other(numbers):
def positive_sum(numbers):
    total = 0
    # step: 0, 1, 2, 3, 4, 5
    # 0, 2, 4, 6, 8, 10, 12
    for i in range(0, len(numbers), 2):
        if numbers[i] > 0:
            total += numbers[i]
    return total
# print(positive_sum([6,2,3,5]))
# # 2. given an array of numbers, return the sum of the first and last number
def sum_first_and_last(nums):
    # len(nums) . or subscript by -1
    return nums[0] + nums[-1]
# print(sum_first_and_last([]))



# 3. given an array of numbers, return the sum of every third number
def sum_every_third(numbers):
    total = 0
    for i in range(0, len(numbers), 3):
        # i is the index. sum a number in the list
        total += numbers[i]
    return total
print(sum_every_third([1,7,9,2,86,44,3]))

