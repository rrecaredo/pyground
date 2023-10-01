from typing import Any

random_set = {"Educative", 1408, 3.142, (True, False)}
print(random_set)
print(len(random_set))  # Length of the set

empty_set: set[Any] = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
random_set.discard(1408)
random_set.remove((True, False))
print(random_set)

# Set union
set_A = {1, 2, 3, 4}
set_B = {"a", "b", "c", "d"}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

# Set intersection
set_C = {1, 2, 3, 4}
set_D = {2, 8, 4, 16}

print(set_C & set_D)
print(set_C.intersection(set_D))
print(set_D.intersection(set_C))

# Set difference
print(set_C - set_D)
print(set_C.difference(set_D))

print(set_D - set_C)
print(set_D.difference(set_C))
