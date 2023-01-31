import random


# Создаем класс "Корабль"
class Ship:

    def __init__(self, ship_coordinates, dict_values, fleet_composition, cell_value, condition_ship):
        self.ship_coordinates = ship_coordinates
        self.dict_values = dict_values
        self.fleet_composition = fleet_composition
        self.cell_value = cell_value
        self.condition_ship = condition_ship

    # Генератор итераций
    @staticmethod
    def generator_item(iterable_object):
        iterator = iter(iterable_object)
        prev_item = None
        current_item = next(iterator)  # throws StopIteration if empty.
        for next_item in iterator:
            yield prev_item, current_item, next_item
            prev_item = current_item
            current_item = next_item
        yield prev_item, current_item, None

    # Перебираем позиции кораблей в зависимости от количества клеток
    @staticmethod
    def positions_ships(number_letters):
        string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
        list_values = []
        for letter_ in string_letters_table:
            list_ = []
            for i in range(1, 11):
                list_.append(letter_ + str(i))
            list_values.append(list_)
        decked_ships = {}
        for prev_letters, item_letters, next_letters in Ship.generator_item(list_values):
            for prev_number, item_number, next_number in Ship.generator_item(range(11 - number_letters)):
                if prev_letters is None:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            item_letters[item_number + number_letters],
                            *next_letters[item_number:item_number + number_letters + 1]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            item_letters[item_number - 1],
                            *next_letters[item_number - 1:item_number + number_letters]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *item_letters[item_number - 1:item_number + number_letters + 1:number_letters + 1],
                            *next_letters[item_number - 1:item_number + number_letters + 1]]
                elif next_letters is None:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number:item_number + number_letters + 1],
                            item_letters[item_number + number_letters]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters],
                            item_letters[item_number - 1]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters + 1],
                            *item_letters[item_number - 1:item_number + number_letters + 1:number_letters + 1]]
                else:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number:item_number + number_letters + 1],
                            item_letters[item_number + number_letters],
                            *next_letters[item_number:item_number + number_letters + 1]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters],
                            item_letters[item_number - 1],
                            *next_letters[item_number - 1:item_number + number_letters]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters + 1],
                            *item_letters[item_number - 1:item_number + number_letters + 1:number_letters + 1],
                            *next_letters[item_number - 1:item_number + number_letters + 1]]
        list_values = []
        for i in range(1, 11):
            list_ = []
            for letter_ in string_letters_table:
                list_.append(letter_ + str(i))
            list_values.append(list_)
        for prev_letters, item_letters, next_letters in Ship.generator_item(list_values):
            for prev_number, item_number, next_number in Ship.generator_item(range(11 - number_letters)):
                if prev_letters is None:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            item_letters[item_number + number_letters],
                            *next_letters[item_number:item_number + number_letters + 1]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            item_letters[item_number - 1],
                            *next_letters[item_number - 1:item_number + number_letters]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *item_letters[item_number - 1:item_number + number_letters + 1:number_letters + 1],
                            *next_letters[item_number - 1:item_number + number_letters + 1]]
                elif next_letters is None:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number:item_number + number_letters + 1],
                            item_letters[item_number + number_letters]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters],
                            item_letters[item_number - 1]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters + 1],
                            *item_letters[item_number - 1:item_number + number_letters + 1:number_letters + 1]]
                else:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number:item_number + number_letters + 1],
                            item_letters[item_number + number_letters],
                            *next_letters[item_number:item_number + number_letters + 1]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters],
                            item_letters[item_number - 1],
                            *next_letters[item_number - 1:item_number + number_letters]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + number_letters])] = [
                            *prev_letters[item_number - 1:item_number + number_letters + 1],
                            *item_letters[item_number - 1:item_number + number_letters + 1:number_letters + 1],
                            *next_letters[item_number - 1:item_number + number_letters + 1]]
        return decked_ships

    # Устанавливаем координаты корабля знаком "квадрат" и координаты вокруг корабля в значение "пустая строка"
    @property
    def enter_coordinates_ship(self):
        return self.dict_values

    @enter_coordinates_ship.setter
    def enter_coordinates_ship(self, value):
        list_around_values = {}
        str_value = "".join(value)
        list_keys = []
        # Проверяем входят ли координаты в координаты уже введенных кораблей
        for list_ in self.fleet_composition:
            for list1_ in list_:
                for dict_ in list1_:
                    for key_ in dict_.keys():
                        list_keys.append(key_)

        for cell_ in value:
            if cell_ in list_keys:
                raise ValueError("По правилам игры, корабли должны находится друг от друга на расстоянии "
                                 "минимум одной клетки")

        # Проверяем входят ли координаты в игровое поле
        if all([len(value) < 5, len(value) > 0]):
            if str_value in Ship.positions_ships(len(value)).keys():
                for item in Ship.positions_ships(len(value))[str_value]:
                    list_around_values[item] = " "
                shit = []
                key_dict = {}
                for cell_ in value:
                    key_dict[cell_] = self.cell_value  # "\033[34m\u25A0\033[0m"
                shit.append(key_dict)
                shit.append(list_around_values)
                # Добавляем корабль во флот
                if len(value) == 4:
                    if len(self.fleet_composition[0]) < 1:
                        self.ship_coordinates = shit
                        self.fleet_composition[0].append(self.ship_coordinates)
                    else:
                        raise ValueError("Будьте внимательны! Вы уже добавили четырехпалубный корабль, "
                                         "но у Вас ещё остались другие не добавленные корабли!")
                elif len(value) == 3:
                    if len(self.fleet_composition[1]) < 2:
                        self.ship_coordinates = shit
                        self.fleet_composition[1].append(self.ship_coordinates)
                    else:
                        raise ValueError("Вы уже добавили все трехпалубные корабли, "
                                         "но у Вас ещё остались другие не добавленные корабли!")
                elif len(value) == 2:
                    if len(self.fleet_composition[2]) < 3:
                        self.ship_coordinates = shit
                        self.fleet_composition[2].append(self.ship_coordinates)
                    else:
                        raise ValueError("Вы уже добавили все двухпалубные корабли, "
                                         "но у Вас ещё остались другие не добавленные корабли!")
                elif len(value) == 1:
                    if len(self.fleet_composition[3]) < 4:
                        self.ship_coordinates = shit
                        self.fleet_composition[3].append(self.ship_coordinates)
                    else:
                        raise ValueError("Вы уже добавили все однопалубные корабли, "
                                         "но у Вас ещё остались другие не добавленные корабли!")

            else:
                raise ValueError("Вы не правильно ввели координаты корабля, корабль должен размещаться в одну линию,"
                                 " вертикально или горизонтально!")
        else:
            raise ValueError(
                "Вы не правильно ввели данные, нужно ввести координаты слитно перечислив те клетки, "
                "в которых Вы хотите разместить корабль, например, А4А5А6А7 или Г3Д3Е3: ")
        for key, item in self.ship_coordinates[0].items():
            if key in self.dict_values.keys():
                self.dict_values[key] = item
        for key, item in self.ship_coordinates[1].items():
            if key in self.dict_values.keys():
                self.dict_values[key] = item
        return self.dict_values

    # Варианты выстрела, когда компьютер ранил корабль
    @staticmethod
    def shot():
        string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
        list_values = []
        for letter_ in string_letters_table:
            list_ = []
            for i in range(1, 11):
                list_.append(letter_ + str(i))
            list_values.append(list_)
        decked_ships = {}
        for prev_letters, item_letters, next_letters in Ship.generator_item(list_values):
            for prev_number, item_number, next_number in Ship.generator_item(range(10)):
                if prev_letters is None:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            item_letters[item_number + 1],
                            *next_letters[item_number]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            item_letters[item_number - 1],
                            *next_letters[item_number]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *item_letters[item_number - 1:item_number + 2:2],
                            *next_letters[item_number]]
                elif next_letters is None:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *prev_letters[item_number],
                            item_letters[item_number + 1]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *prev_letters[item_number],
                            item_letters[item_number - 1]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *prev_letters[item_number],
                            *item_letters[item_number - 1:item_number + 2:2]]
                else:
                    if prev_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *prev_letters[item_number],
                            item_letters[item_number + 1],
                            *next_letters[item_number]]
                    elif next_number is None:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *prev_letters[item_number],
                            item_letters[item_number - 1],
                            *next_letters[item_number]]
                    else:
                        decked_ships["".join(item_letters[item_number:item_number + 1])] = [
                            *prev_letters[item_number],
                            *item_letters[item_number - 1:item_number + 2:2],
                            *next_letters[item_number]]
        return decked_ships

    # Выстрел компьютера в зависимости от того, выстрел это после ранения или просто выстрел
    def computer_shot(self, previous_shot):
        if self.condition_ship == "Wounded":
            value_shot = random.choice(Ship.positions_ships(1)[previous_shot])
            return value_shot
        else:
            value_shot = random.choice(list(self.dict_values.keys()))
            return value_shot

    # Выстрел
    def shot_at_ship(self, value, color_symbol):
        enemy_key = {}
        for fleet_item in self.fleet_composition:
            for list_ in fleet_item:
                if value in list_[0].keys():
                    enemy_key = list_[0]

        # Проверяем выстрел
        if value in self.dict_values.keys():
            if value in enemy_key.keys():
                if self.dict_values[value] == self.cell_value:
                    self.dict_values[value] = color_symbol  #"\033[31mX\033[0m"
                    enemy_key[value] = color_symbol
                    if self.cell_value not in enemy_key.values():
                        print("\033[33m{}\033[0m".format("Корабль потоплен! Вы ходите ещё раз!"))
                        self.condition_ship = "Whole"  # Корабль убит
                    else:
                        print("\033[33m{}\033[0m".format("Корабль ранен! Вы ходите ещё раз!"))
                        self.condition_ship = "Wounded"  # Корабль ранен
                    # Закрашиваем клетки, если корабль убит
                    for fleet_item in self.fleet_composition:
                        for list_ in fleet_item:
                            list_keys = []
                            for key_, item_ in list_[0].items():
                                if key_ in self.dict_values.keys():
                                    list_[0][key_] = self.dict_values[key_]
                                list_keys.append(list_[0][key_])
                            if self.cell_value not in list_keys:
                                for key, item in list_[1].items():
                                    list_[1][key] = "\033[31m\u25CF\033[0m"
                else:
                    raise ValueError("В эту часть корабля уже прилетел снаряд, попробуйте ещё раз!")
            elif self.dict_values[value] == "\033[31m\u25CF\033[0m":
                raise ValueError("Вы уже стреляли в это место, попробуйте ещё раз!")
            else:
                self.dict_values[value] = "\033[31m\u25CF\033[0m"
                self.condition_ship = "Miss"  # Выстрел мимо
                print("\033[31m{}\033[0m".format("К сожалению это промах"))
        else:
            raise ValueError("Вы не правильно ввели координаты выстрела, попробуйте ещё раз!")
        # Обновляем словарь
        list_keys_with_values = []
        for fleet_item in self.fleet_composition:
            for list_ in fleet_item:
                for key_, item_ in list_[1].items():
                    if item_ == "\033[31m\u25CF\033[0m":
                        list_keys_with_values.append(key_)

        for key_list in list_keys_with_values:
            if key_list in self.dict_values.keys():
                self.dict_values[key_list] = "\033[31m\u25CF\033[0m"
        return self.dict_values
