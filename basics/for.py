float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
# print(float_list)

for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
    float_list[i] = float_list[i] * 2

# print(float_list)

# ----------------------------

count_greater = 0

for num in float_list:  # Iterator traverses to the last index of the list
    if num > 10:
        count_greater += 1

# print(count_greater)

# ----------------------------

n = 50
num_list = [10, 25, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
    for n2 in num_list:
        if n1 != n2:
            if n1 + n2 == n:
                found = True  # Set found to True
                break  # Break inner loop if a pair is found
    if found:
        print(n1, n2)  # Print the pair
        break  # Break outer loop if a pair is found

# ----------------------------

num_list = list(range(0, 10))

for num in num_list:
    if num == 3 or num == 6 or num == 8:
        continue
    print(num)

# ----------------------------

num_list = list(range(20))

for num in num_list:
    pass  # You can write code here later on

print(len(num_list))
