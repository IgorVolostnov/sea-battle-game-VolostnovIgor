coordinates = {'Б4Б5Б6Б7': ['А3', 'А4', 'А5', 'А6', 'А7', 'А8', 'Б3', 'Б8', 'В3', 'В4', 'В5', 'В6', 'В7', 'В8']}
value_around_shit = [item for sublist in list(coordinates.values()) for item in sublist]
print(value_around_shit)
print("\u25FC")
