star_wars_list = ["Anakin", "Darth Vader", 1000]
star_wars_set = {"Anakin", "Darth Vader", 1000}
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}

star_wars_tup = tuple(star_wars_list)  # Converting from list
print(star_wars_tup)

star_wars_tup = tuple(star_wars_set)  # Converting from set
print(star_wars_tup)

star_wars_tup = tuple(star_wars_dict)  # Converting from dictionary
print(star_wars_tup)

star_wars_tup = tuple(star_wars_dict.items())
print(star_wars_list)
