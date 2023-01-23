from FilePlayingField import PlayingField
from FileClassShip import Ship

# Код игры
# Создаем два словаря с пустыми значениями
string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
my_dictionary_values = {}
enemy_dictionary_values = {}

for letter_ in string_letters_table:
    for number_ in range(1, 11):
        my_dictionary_values[letter_ + str(number_)] = " "
        enemy_dictionary_values[letter_ + str(number_)] = " "

# Выводим пустые экраны перед началом игры
battlefield = PlayingField(my_dictionary_values, enemy_dictionary_values)
battlefield.output_screen(my_dictionary_values, enemy_dictionary_values)
# Вводим координаты нового корабля
try:
    my_ship_four_decked_ship = Ship([], my_dictionary_values, True)
    my_ship_four_decked_ship.enter_coordinates_ship = input(
        "Введите координаты корабля, например: А1А2А3А4 или Г3Д3Е3: ")
except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
    print(e)
# Выводим экран после добавления корабля
battlefield.output_screen(my_ship_four_decked_ship.dict_values, enemy_dictionary_values)
# Добавляем корабль во флот пользователя
my_ship_four_decked_ship.fleet = my_ship_four_decked_ship.ship_coordinates
print(my_ship_four_decked_ship.fleet)
