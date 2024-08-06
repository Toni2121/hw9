import random

list1 = []
for i in range(20):
    list1.append(random.randint(-50, 50))
print(list1)
print(list(map(lambda x: x ** 3, list1)))
print(list(map(lambda x: x % 10, list1)))
print(list(map(lambda x: (x * 1.8) + 32, list1)))
print(list(map(lambda x: "positive" if x > 0 else "negative" , list1)))
max_value = max(list1)
min_value = min(list1)
print(list(map(lambda x: "max" if x == max_value else "min" if x == min_value else x, list1)))
print(list(map(lambda x: ((abs(x) % 10 * 10 + abs(x) // 10) * (1 if x >= 0 else -1)), list1)))
print(list(map(lambda x: abs(x), list1)))
list2 = [[7000, 10000], [5000, 300], [8000, 2000]]
print(list(map(lambda x: x[0] - x[1], list2)))