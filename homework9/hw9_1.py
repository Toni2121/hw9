import random

list1 = []
for i in range(50):
    list1.append(random.randint(1, 100))

print(list1)

print(list(filter(lambda x: x > 50, list1)))
print(list(filter(lambda x: x % 7 == 0, list1)))
print(list(filter(lambda x: 100 > x > 9, list1)))
print(list(filter(lambda x: 100 > x > 9 and i % 10 == i // 10, list1)))
print(list(filter(lambda x: x % 10 + x // 10 == 9, list1)))
print(list(filter(lambda x: x > (sum(list1) / len(list1)), list1)))
print(sum(list1) / len(list1))
print(list(filter(lambda x: x > (max(list1) / 2), list1)))
print(max(list1))
print(list(filter(lambda x: x > list1[25], list1)))


list2 = []
while len(list2) < 5:
    user_input = int(input("Please enter a number (enter -99 to finish early): "))
    if user_input == -99:
        break
    else:
        list2.append(user_input)
print(list2)
list1 = list(set(list1))  # Remove duplicates from list1
list1.extend(filter(lambda x: x not in list1, list2))
print(list1)

def rishoni(a: int) -> bool:
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

print(rishoni(6))