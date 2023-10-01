my_list = [1, 2.5, "A string", True]
print(my_list)

num_seq = range(0, 10)  # A sequence from 0 to 9
num_list = list(num_seq)  # The list() method casts the sequence into a list
print(num_list)

num_seq = range(3, 20, 3)  # A sequence from 3 to 19 with a step of 3
print(list(num_seq))

world_cup_winners = [
    [2006, "Italy"],
    [2010, "Spain"],
    [2014, "Germany"],
    [2018, "France"],
]
print(world_cup_winners)

part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]

merged_list = part_A + part_B
print(merged_list)

part_A = [1, 2, 3, 4, 5]
part_B = [6, 7, 8, 9, 10]
part_A.extend(part_B)
print(part_A)

num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
num_list.insert(11, 7)
print(num_list)

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()  # Removes and returns the last element
other_house = houses.pop(1)  # Removes and returns the element at index 1
print(last_house)
print(other_house)
print(houses)

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# For nested lists
populations = [["Winterfell", 10000], ["King's Landing", 50000], ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

# List slicing
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

num_list = [20, 40, 10, 50, 30, 100, 5]
num_list.sort()
print(num_list)

print(cities.count("London"))

# --------------------------------

list1 = [30, 50, 110, 40, 15, 75]
list2 = [10, 60, 20, 50]

sum_list = [(n1, n2) for n1 in list1 for n2 in list2 if n1 + n2 > 100]

print(sum_list)

# --------------------------------

odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if not num % 2 == 0:
        odd_list.append(num)

print(odd_list)
