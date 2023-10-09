def print_str():
    a = "Hello World"
    print(len(a))


def multi_line():
    a = """Hello
    World"""
    print(len(a))


def batman():
    batman = "Bruce Wayne"

    first = batman[0]  # Accessing the first character
    print(first)

    space = batman[5]  # Accessing the empty space in the string
    print(space)

    last = batman[len(batman) - 1]
    print(last)

    # err = batman[50]
    # print(err)

    print(batman[-1])  # Corresponds to batman[10]
    print(batman[-5])  # Corresponds to batman[6]


def substrings():
    random_string = "This is a random string"

    print("of" in random_string)  # Check whether 'of' exists in randomString
    print("random" in random_string)  # 'random' exists!


print("hey que tal".find("que", 0, 7))
print("hey que tal".replace("que", "gasa"))

print("UpperCase".upper())
print("LowerCase".lower())

llist = ["a", "b", "c"]
print(">>".join(llist))  # joining strings with >>
print("<<".join(llist))  # joining strings with <<
print(", ".join(llist))  # joining strings with comma and space

string1 = "Learn Python {version} at {cname}".format(version=3, cname="Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)
