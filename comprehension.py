nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums]

print(nums)
print(nums_double)

nums = [10, 20, 30, 40, 50]

# List comprehension
nums_double = [n * 2 for n in nums if n % 4 == 0]

print(nums)
print(nums_double)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(list([row[i] for row in matrix] for i in range(4)))
print([[row[i] for row in matrix] for i in range(4)])
