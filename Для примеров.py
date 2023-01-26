def number_values_game(symbol, screen_game):
    number_symbol = 0
    for item in screen_game.values():
        if item == symbol:
            number_symbol += 1
    return number_symbol

string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
my_dictionary_values = {}
enemy_dictionary_values = {}

for letter_ in string_letters_table:
    for number_ in range(1, 11):
        my_dictionary_values[letter_ + str(number_)] = " "
        enemy_dictionary_values[letter_ + str(number_)] = " "


print(number_values_game(" ", my_dictionary_values))

