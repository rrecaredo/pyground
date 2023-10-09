def lexical():
    if True:
        a = 3

    print(a)


lexical()

num = 60

output = (
    "The number is less than or equal to 50"
    if num <= 50
    else "The number is greater than 50"
)

print(output)

light = "Red"

if light == "Green":
    print("Go")

elif light == "Yellow":
    print("Caution")

elif light == "Red":
    print("Stop")

else:
    print("Incorrect light signal")
