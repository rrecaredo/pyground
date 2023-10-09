from dataclasses import dataclass

# This way we can combine @dataclass with a constructor that takes custom parameters


@dataclass
class MyClass:
    aaa: str
    bbb: str
    ccc: int
    ddd: float

    def __init__(self, aaa: str, bbb: str, ccc: int, ddd: float, custom_param: str):
        # Call the data class generated constructor to initialize aaa, bbb, ccc, and ddd
        super().__init__(aaa, bbb, ccc, ddd)  # type: ignore

        # Initialize the custom parameter
        self.custom_param = custom_param


obj = MyClass("ValueA", "ValueB", 42, 3.14, "Custom Value")

print(obj.aaa)  # Output: "ValueA"
print(obj.bbb)  # Output: "ValueB"
print(obj.ccc)  # Output: 42
print(obj.ddd)  # Output: 3.14
print(obj.custom_param)  # Output: "Custom Value"
