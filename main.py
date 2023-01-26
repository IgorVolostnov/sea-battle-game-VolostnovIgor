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
battlefield = PlayingField((my_dictionary_values, enemy_dictionary_values))  # Создали поле боя
battlefield.output_screen
# Вывод поля боя на экран
# Ввод координат всех кораблей
my_ship = Ship([], my_dictionary_values, [[], [], [], []])  # Новый объект "Корабль"
while True:
    try: # Ввод координат всех кораблей
        my_ship.enter_coordinates_ship = input("Введите координаты корабля, например: А1А2А3А4 или Г3Д3Е3: ")
        my_ship.fleet = my_ship.ship_coordinates  # Добавление корабля во флот
        battlefield.output_screen
        sum_fleet = len(my_ship.fleet_composition[0]) + \
                    len(my_ship.fleet_composition[1]) + \
                    len(my_ship.fleet_composition[2]) + \
                    len(my_ship.fleet_composition[3])
        print(my_ship.fleet_composition)
        print(sum_fleet)
        if sum_fleet == 10:
            print("Ваш флот готов к сражению!")
            break
    except ValueError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
        print(e)

# Выводим экран после добавления корабля
print(my_ship.fleet_composition)
print(battlefield.symbol(" "))
print(battlefield.symbol("\u25A0"))
# Добавляем корабль во флот пользователя
