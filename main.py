from FilePlayingField import PlayingField
from FileClassShip import Ship
from transliterate import translit
import random
import sys


# Игра Морской бой
def hello():
    print("\033[33m {}".format("Привет! Это Игра Морской Бой! Правила Игры:"))
    print("\033[33m {}".format("Игроки по очереди пишут координаты на неизвестной им карте соперника. Если  "))
    print("\033[33m {}".format("у соперника по этим координатам есть корабль, то корабль 'ранен' или 'убит',"))
    print("\033[33m {}".format("а попавший получает право сделать ещё один ход. Цель игрока — первым убить  "))
    print("\033[33m {}".format("все корабли противника.\033[0m"))


def rules():
    print("\033[33m {}".format("У каждого игрока флот состоит из: "))
    print("\033[33m {}".format("\033[34m\u25A0 \u25A0 \u25A0 \u25A0 - 1 четырехпалубный корабль"))
    print("\033[33m {}".format("\033[34m\u25A0 \u25A0 \u25A0   \u25A0 \u25A0 \u25A0 - 2 трехпалубных корабля"))
    print("\033[33m {}".format("\033[34m\u25A0 \u25A0   \u25A0 \u25A0   \u25A0 \u25A0 - 3 двухпалубных корабля"))
    print("\033[33m {}".format("\033[34m\u25A0   \u25A0   \u25A0   \u25A0 - 4 однопалубных корабля"))
    print("\033[33m {}".format("Корабли могут располагаться в одну линию вертикально или горизонтально."))
    print("\033[33m {}".format("Между кораблями должно быть не менее одной клетки.\033[0m"))


# Генератор итераций
def generator_item(iterable_object):
    iterator = iter(iterable_object)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield prev_item, current_item, next_item
        prev_item = current_item
        current_item = next_item
    yield prev_item, current_item, None


# Обрабатываем ввод пользователя: меняем латинские буквы на русские, приводим к верхнему регистру,
# сортируем по возрастанию, если пользователь ввел координаты клеток не по порядку
def input_handler(text):
    value = translit(text.upper(), 'ru')
    list_value = list(value)  # Ввод координат нового корабля
    list_value_change = []

    for prev_letter, current_letter, next_letter in generator_item(list_value):
        if all([current_letter == "1", next_letter == "0"]):
            united_sign = current_letter + next_letter
            list_value_change.append(united_sign)
        else:
            list_value_change.append(current_letter)

    list_value = list_value_change
    list_value_change = []

    for current_letter in list_value:
        if current_letter != "0":
            list_value_change.append(current_letter)

    list_value = list_value_change
    list_value_change = []

    for i in range(0, len(list_value) - 1, 2):
        list_value_change.append(list_value[i] + list_value[i + 1])

    list_value_change.sort()
    list_value = list_value_change
    list_value_change = []
    list_10 = []

    for item in list_value:
        if "10" in item:
            list_10.append(item)
        else:
            list_value_change.append(item)

    list_value_change.sort()
    list_10.sort()
    list_value = [*list_value_change, *list_10]
    return list_value


# Код игры
hello()
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
battlefield.output_screen  # Вывод поля боя на экран
rules()
# Заполняем поле компьютера кораблями с пустыми значениями
enemy_ship = Ship([], enemy_dictionary_values, [[], [], [], []], " ", "Whole")  # Новый объект "Корабль"
while True:
    if input("Начнем игру? ДА/НЕТ: ").upper() == "ДА":
        # Ввод координат всех кораблей компьютера
        list_comp = [(4, 1), (3, 3), (2, 6), (1, 10)]
        for i in list_comp:
            while True:
                try:
                    enemy_ship.enter_coordinates_ship = input_handler(
                        random.choice(list(enemy_ship.positions_ships(i[0]).keys())))

                    sum_fleet = len(enemy_ship.fleet_composition[0]) + \
                                len(enemy_ship.fleet_composition[1]) + \
                                len(enemy_ship.fleet_composition[2]) + \
                                len(enemy_ship.fleet_composition[3])
                    if sum_fleet == i[1]:
                        break
                except ValueError as e:
                    continue
        print("\033[31m{}\033[0m".format("Флот компьютера готов к сражению!"))
        # Ввод координат всех кораблей пользователя
        my_ship = Ship([], my_dictionary_values, [[], [], [], []], "\033[34m\u25A0\033[0m", "Whole")
        while True:
            try:  # Ввод координат всех кораблей
                input_shit = input_handler(input("\033[34m{}\033[0m".format("Введите координаты корабля, "
                                                                            "например: А1А2А3А4 или Г3Д3Е3: ")))
                my_ship.enter_coordinates_ship = input_shit
                battlefield.output_screen
                sum_fleet = len(my_ship.fleet_composition[0]) + \
                            len(my_ship.fleet_composition[1]) + \
                            len(my_ship.fleet_composition[2]) + \
                            len(my_ship.fleet_composition[3])

                if sum_fleet == 10:
                    print("\033[34m{}\033[0m".format("Ваш флот готов к сражению!"))
                    break

            except ValueError as e:  # Выводим ту ошибку, которая произошла при вводе
                print("\033[31m{}\033[0m".format(e))

        # Начинаем стрелять
        prev_input_shot = None
        hit_list = [None, None]
        while True:
            if battlefield.symbol("\033[31mX\033[0m") == 20:
                print("\033[33m{}\033[0m".format("Все корабли противника уничтожены, Вы победили!"))
                if input("Сыграем ещё раз? ДА/НЕТ: ").upper() == "ДА":
                    break
                else:
                    sys.exit("До встречи в следующей игре!")
            elif battlefield.symbol("\033[34mX\033[0m") == 20:
                print("\033[31m{}\033[0m".format("Все Ваши корабли уничтожены, Компьютер  победил!"))
                if input("Сыграем ещё раз? ДА/НЕТ: ").upper() == "ДА":
                    break
                else:
                    sys.exit("До встречи в следующей игре!")
            else:
                if any([enemy_ship.condition_ship == "Whole",
                        enemy_ship.condition_ship == "Wounded"]):
                    while True:
                        try:  # Выстрел пользователя
                            input_shot = input_handler(input("\033[34m{}\033[0m".
                                                             format("Введите координаты выстрела, например Е2: ")))
                            enemy_ship.shot_at_ship(input_shot[0], "\033[31mX\033[0m")
                            if any([enemy_ship.condition_ship == "Whole",
                                    enemy_ship.condition_ship == "Wounded"]):
                                battlefield.output_screen
                                break
                            elif enemy_ship.condition_ship == "Miss":
                                battlefield.output_screen
                                break
                        except ValueError as e:  # Выводим ту ошибку, которая произошла при вводе
                            battlefield.output_screen
                            print("\033[31m{}\033[0m".format(e))
                else:  # Выстрел компьютера
                    while True:
                        if all([hit_list[0] == "Wounded", hit_list[1] == "Miss"]):
                            my_ship.condition_ship = "Wounded"
                            try:
                                input_shot = my_ship.computer_shot(prev_input_shot)
                                my_ship.shot_at_ship(input_shot, "\033[34mX\033[0m")
                                if my_ship.condition_ship == "Whole":
                                    hit_list = [None, None]
                                    battlefield.output_screen
                                    break
                                elif my_ship.condition_ship == "Wounded":
                                    prev_input_shot = input_shot
                                    battlefield.output_screen
                                    break
                                else:
                                    battlefield.output_screen
                                    hit_list = [None, None]
                                    enemy_ship.condition_ship = "Whole"
                                    break
                            except ValueError as e:
                                continue
                        else:
                            try:
                                input_shot = my_ship.computer_shot(prev_input_shot)
                                prev_input_shot = input_shot
                                my_ship.shot_at_ship(prev_input_shot, "\033[34mX\033[0m")
                                if my_ship.condition_ship == "Whole":
                                    hit_list = [None, None]
                                    battlefield.output_screen
                                    break
                                elif my_ship.condition_ship == "Wounded":
                                    hit_list[0] = "Wounded"
                                    battlefield.output_screen
                                    break
                                else:
                                    hit_list[1] = "Miss"
                                    battlefield.output_screen
                                    enemy_ship.condition_ship = "Whole"
                                    break
                            except ValueError as e:
                                continue
    else:
        print("Сыграем в другой раз")
        break
