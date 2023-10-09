def identity():
    dynamic_object = {"name": "John", "age": 30, "city": "New York"}

    another_dynamic_object = {"name": "John", "age": 30, "city": "New York"}

    print(dynamic_object is another_dynamic_object)
    print(dynamic_object == another_dynamic_object)
    print(dynamic_object is not another_dynamic_object)


identity()
