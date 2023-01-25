# Создаем класс "Корабль"
class Ship:

    def __init__(self, ship_coordinates, dict_values, fleet_composition):
        self.ship_coordinates = ship_coordinates
        self.dict_values = dict_values
        self.fleet_composition = fleet_composition

    # Позиции четырехпалубных кораблей
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

    @staticmethod
    def Positions_four_decked_ships():
        string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
        list_values = []
        for letter_ in string_letters_table:
            list_ = []
            for i in range(1, 11):
                list_.append(letter_ + str(i))
            list_values.append(list_)
        four_decked_ships = {}
        for prev_letters, item_letters, next_letters in Ship.generator_item(list_values):
            for prev_number, item_number, next_number in Ship.generator_item(range(7)):
                if prev_letters is None:
                    if prev_number is None:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            item_letters[item_number + 4],
                            *next_letters[item_number:item_number + 5]]
                    elif next_number is None:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            item_letters[item_number - 1],
                            *next_letters[item_number - 1:item_number + 4]]
                    else:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *item_letters[item_number - 1:item_number + 5:5],
                            *next_letters[item_number - 1:item_number + 5]]
                elif next_letters is None:
                    if prev_number is None:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *prev_letters[item_number:item_number + 5],
                            item_letters[item_number + 4]]
                    elif next_number is None:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *prev_letters[item_number - 1:item_number + 4],
                            item_letters[item_number - 1]]
                    else:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *prev_letters[item_number - 1:item_number + 5],
                            *item_letters[item_number - 1:item_number + 5:5]]
                else:
                    if prev_number is None:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *prev_letters[item_number:item_number + 5],
                            item_letters[item_number + 4],
                            *next_letters[item_number:item_number + 5]]
                    elif next_number is None:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *prev_letters[item_number - 1:item_number + 4],
                            item_letters[item_number - 1],
                            *next_letters[item_number - 1:item_number + 4]]
                    else:
                        four_decked_ships["".join(item_letters[item_number:item_number + 4])] = [
                            *prev_letters[item_number - 1:item_number + 5],
                            *item_letters[item_number - 1:item_number + 5:5],
                            *next_letters[item_number - 1:item_number + 5]]
        return four_decked_ships

    @property
    def enter_coordinates_ship(self):
        return self.dict_values

    @enter_coordinates_ship.setter
    def enter_coordinates_ship(self, value):
        list_around_values = {}
        if len(value) == 8:
            if value in Ship.Positions_four_decked_ships().keys():
                for item in Ship.Positions_four_decked_ships()[value]:
                    list_around_values[item] = " "
                sign = list(value)
                shit = [{
                    sign[0] + sign[1]: "\u25A0",
                    sign[2] + sign[3]: "\u25A0",
                    sign[4] + sign[5]: "\u25A0",
                    sign[6] + sign[7]: "\u25A0"},
                    list_around_values]
                self.ship_coordinates = shit
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

    @property
    def fleet(self):
        return self.fleet_composition

    @fleet.setter
    def fleet(self, value):
        if len(value[0]) == 4:
            if len(self.fleet_composition[0]) < 1:
                self.fleet_composition[0].append(value)
            else:
                raise ValueError("Вы уже добавили четырехпалубный корабль, добавьте оставшиеся корабли!")
        elif len(value[0]) == 3:
            if len(self.fleet_composition[1]) < 2:
                self.fleet_composition[1].append(value)
            else:
                raise ValueError("Вы уже добавили все трехпалубные корабли, добавьте оставшиеся корабли!")
        elif len(value[0]) == 2:
            if len(self.fleet_composition[2]) < 3:
                self.fleet_composition[2].append(value)
            else:
                raise ValueError("Вы уже добавили все двухпалубные корабли, добавьте оставшиеся корабли!")
        else:
            if len(self.fleet_composition[3]) < 4:
                self.fleet_composition[3].append(value)
        return self.fleet_composition
