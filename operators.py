def floor_division():
    print(43 // 10)
    float1 = 5.5
    float2 = 4.5
    print(float1 // float2)
    print(12.4 // 2)


def modulo():
    print(10 % 2)

    twenty_eight = 28
    print(twenty_eight % 10)

    print(-28 % 10)  # The remainder is positive if the right-hand operand is positive
    print(28 % -10)  # The remainder is negative if the right-hand operand is negative
    print(34.4 % 2.5)  # The remainder can be a float


def logical():
    # OR Expression
    my_bool = True or False
    print(my_bool)

    # AND Expression
    my_bool = True and False
    print(my_bool)

    # NOT expression
    my_bool = False
    print(not my_bool)
    print(not not my_bool)


def booleans_as_1s_and_0s():
    print(10 * True)
    print(10 * False)
