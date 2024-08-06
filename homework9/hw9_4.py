fruit_list: list[str] = ["Mango", "Orange", "Banana", "Apple", "Watermelon",\
                         "Grapes", "pineapple", "strawberry"]
print(list(map(lambda x: x[::-1], fruit_list)))
print(list(map(lambda x: x[0], fruit_list)))
print(list(map(lambda fruit_list: fruit_list.upper(), fruit_list)))
print(list(map(lambda x: len(x), fruit_list)))
print(list(map(lambda x: "!" if x[-1].lower() == "s" else x, fruit_list)))
calories = [60, 47, 89, 52, 30, 69, 50, 32]
calories_and_fruits = (list(map(lambda x: (x[0], x[1]), zip(fruit_list, calories))))
print(calories_and_fruits)
print(list(map(lambda x: (x[0] + "!" if x[1] > 50 else x[0], x[1]), calories_and_fruits)))
