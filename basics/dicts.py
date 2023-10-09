from typing import Any, List, Union

empty_dict: dict[str, Any] = {}
print(empty_dict)

phone_book = {"Batman": 468426, "Cersei": 237734, "Ghostbusters": 44678}
print(phone_book)

empty_dict = dict()  # Empty dictionary
phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([("Batman", 468426), ("Cersei", 237734), ("Ghostbusters", 44678)])

print(phone_book.get("Ghostbusters"))
print(phone_book["Ghostbusters"])

phone_book = {"Batman": 468426, "Cersei": 237734, "Ghostbusters": 44678}
phone_book["Godzilla"] = 46394  # New entry
del phone_book["Godzilla"]
print(phone_book)

phone_book = {"Batman": 468426, "Cersei": 237734, "Ghostbusters": 44678}
cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# Removes and returns the last inserted pair, as a tuple
# In Python versions before 3.7, popitem() removes and returns the random item
lastAdded = phone_book.popitem()
print(lastAdded)
print(len(phone_book))

# Checking Key Existence
phone_book = {"Batman": 468426, "Cersei": 237734, "Ghostbusters": 44678}
print("Batman" in phone_book)
print("Godzilla" in phone_book)

# Merging dictionaries

phone_book1 = {"Batman": 468426, "Cersei": 237734, "Ghostbusters": 44678}
phone_book2 = {"Godzilla": 46394, "Harry Potter": 67490}
phone_book1.update(phone_book2)
print(phone_book1)

# Comprehension

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n * 2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)

# --------------------------------

star_wars_list: List[List[Any]] = [
    [1, "Anakin"],
    [2, "Darth Vader"],
    [3, 1000],
]
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}

star_wars_dict: dict[Any, Any] = dict(star_wars_list)  # Converting from list
print(star_wars_dict)

star_wars_dict = dict(star_wars_tup)  # Converting from tuple
print(star_wars_dict)

star_wars_dict = dict(star_wars_set)  # Converting from set
print(star_wars_dict)
