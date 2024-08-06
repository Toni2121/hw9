city_list: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print(sorted(city_list, key=lambda city: len(city)))
print(sorted(city_list, key=lambda city: (city[-1])))
print(list(map(lambda city: city[::-1], city_list)))
print(sorted(city_list, key=lambda city: city[::-1]))
miles = [5760, 5690, 2050, 2240, 8780, 1300, 4920]
continent = ["Asia", "North America", "Europe", "Europe", "Australia", "Asia"]
new_list = (list(map(lambda x: (x[0], x[1]), zip(city_list, miles))))
last_list = (list(map(lambda x: (x[0], x[1]), zip(new_list, continent))))
print(last_list)
print(sorted(last_list, key=lambda x: x[0][1]))
print(sorted(last_list, key=lambda x: -x[0][1]))
print(sorted(last_list, key=lambda x: x[1]))
print(sorted(last_list, key=lambda x: x[1][1]))