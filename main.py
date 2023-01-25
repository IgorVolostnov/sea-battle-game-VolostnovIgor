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
battlefield = PlayingField(my_dictionary_values, enemy_dictionary_values)  # Создали поле боя
battlefield.output_screen(my_dictionary_values, enemy_dictionary_values)  # Вывод поля боя на экран
# Ввод координат всех кораблей
sum_fleet = 0
while True:
    try:
        my_ship_four_decked_ship = Ship([], my_dictionary_values, [[], [], [], []])  # Новый объект "Корабль"
        my_ship_four_decked_ship.enter_coordinates_ship = input(
            "Введите координаты корабля, например: А1А2А3А4 или Г3Д3Е3: ")  # Ввод координат нового корабля
        my_ship_four_decked_ship.fleet = my_ship_four_decked_ship.ship_coordinates  # Добавление корабля во флот
        battlefield.output_screen(my_ship_four_decked_ship.dict_values, enemy_dictionary_values)
        for list_ in my_ship_four_decked_ship.fleet_composition:
            sum_fleet += len(list_)
        if sum_fleet == 1:
            print("Ваш флот готов к сражению!")
            break
    except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
        print(e)

# Выводим экран после добавления корабля
battlefield.output_screen(my_ship_four_decked_ship.dict_values, enemy_dictionary_values)
print(my_ship_four_decked_ship.Positions_four_decked_ships())
# Добавляем корабль во флот пользователя
