list1: list[str] = ["Grand Theft Auto V", "Fortnite", "Overwatch", "Dark souls", "The Elder Scrolls V: Skyrim"]
print(list(filter(lambda list1: len([char for char in list1]) > 8, list1)))
print(list(filter(lambda list1: [char for char in list1][0].lower() == "f", list1)))
print(list(filter(lambda list1: len([char for char in list1]) == 2, list1)))
print(list(filter(lambda list1: any(["v" in char for char in list1]), list1)))
print(list(filter(lambda list1: any([char in "*&^!:" for char in list1]), list1)))
years = [2013, 2017, 2016, 2011, 2011]
new_list = (list(map(lambda x: (x[0], x[1]), zip(list1, years))))
print(new_list)
new_list2 = []
print(list(map(lambda game: game[0], filter(lambda game: game[1] > 2014, zip(list1, years)))))