def slicing():
    v = "Hello World"
    print(v[2:5])  # llo
    print(v[2:])  # llo World
    print(v[:5])  # Hello
    print(v[-5:-2])  # Wor
    print(v[-5:])  # World
    print(v[:-2])  # Hello Wor
    print(v[2:5:2])  # lo
    print(v[::2])  # HloWrd
    print(v[::-1])  # dlroW olleH
    print(v[::-2])  # drWolH

    print(v[0:7])  # A step of 1
    print(v[0:7:2])  # A step of 2
    print(v[0:7:5])  # A step of 5


def reverse_slicing():
    str = "Hello World"
    print(str[::-1])  # dlroW olleH
