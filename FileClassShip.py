# Создаем класс "Корабль"
class Ship:

    def __init__(self, ship_coordinates):
        self.ship_coordinates = ship_coordinates

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
        four_decked_ships = {}
        for prev_letters, item_letters, next_letters in Ship.generator_item(string_letters_table):
            for prev_number, item_number, next_number in Ship.generator_item(range(1, 8)):
                if prev_letters is None:
                    if prev_number is None:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            item_letters + str(item_number + 4),
                            next_letters + str(item_number),
                            next_letters + str(item_number + 1),
                            next_letters + str(item_number + 2),
                            next_letters + str(item_number + 3),
                            next_letters + str(item_number + 4)]
                    elif next_number is None:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            item_letters + str(item_number - 1),
                            next_letters + str(item_number - 1),
                            next_letters + str(item_number),
                            next_letters + str(item_number + 1),
                            next_letters + str(item_number + 2),
                            next_letters + str(item_number + 3)]
                    else:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            item_letters + str(item_number - 1),
                            item_letters + str(item_number + 4),
                            next_letters + str(item_number - 1),
                            next_letters + str(item_number),
                            next_letters + str(item_number + 1),
                            next_letters + str(item_number + 2),
                            next_letters + str(item_number + 3),
                            next_letters + str(item_number + 4)]
                elif next_letters is None:
                    if prev_number is None:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            prev_letters + str(item_number),
                            prev_letters + str(item_number + 1),
                            prev_letters + str(item_number + 2),
                            prev_letters + str(item_number + 3),
                            prev_letters + str(item_number + 4),
                            item_letters + str(item_number + 4)]
                    elif next_number is None:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            prev_letters + str(item_number - 1),
                            prev_letters + str(item_number),
                            prev_letters + str(item_number + 1),
                            prev_letters + str(item_number + 2),
                            prev_letters + str(item_number + 3),
                            item_letters + str(item_number - 1)]
                    else:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            prev_letters + str(item_number - 1),
                            prev_letters + str(item_number),
                            prev_letters + str(item_number + 1),
                            prev_letters + str(item_number + 2),
                            prev_letters + str(item_number + 3),
                            prev_letters + str(item_number + 4),
                            item_letters + str(item_number - 1),
                            item_letters + str(item_number + 4)]
                else:
                    if prev_number is None:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            prev_letters + str(item_number),
                            prev_letters + str(item_number + 1),
                            prev_letters + str(item_number + 2),
                            prev_letters + str(item_number + 3),
                            prev_letters + str(item_number + 4),
                            item_letters + str(item_number + 4),
                            next_letters + str(item_number),
                            next_letters + str(item_number + 1),
                            next_letters + str(item_number + 2),
                            next_letters + str(item_number + 3),
                            next_letters + str(item_number + 4)]
                    elif next_number is None:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            prev_letters + str(item_number - 1),
                            prev_letters + str(item_number),
                            prev_letters + str(item_number + 1),
                            prev_letters + str(item_number + 2),
                            prev_letters + str(item_number + 3),
                            item_letters + str(item_number - 1),
                            next_letters + str(item_number - 1),
                            next_letters + str(item_number),
                            next_letters + str(item_number + 1),
                            next_letters + str(item_number + 2),
                            next_letters + str(item_number + 3)]
                    else:
                        four_decked_ships[
                            item_letters + str(item_number) +
                            item_letters + str(item_number + 1) +
                            item_letters + str(item_number + 2) +
                            item_letters + str(item_number + 3)] = [
                            prev_letters + str(item_number - 1),
                            prev_letters + str(item_number),
                            prev_letters + str(item_number + 1),
                            prev_letters + str(item_number + 2),
                            prev_letters + str(item_number + 3),
                            prev_letters + str(item_number + 4),
                            item_letters + str(item_number - 1),
                            item_letters + str(item_number + 4),
                            next_letters + str(item_number - 1),
                            next_letters + str(item_number),
                            next_letters + str(item_number + 1),
                            next_letters + str(item_number + 2),
                            next_letters + str(item_number + 3),
                            next_letters + str(item_number + 4)]
        return four_decked_ships

    @property
    def enter_coordinates_ship(self):
        return self.ship_coordinates

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
                raise ValueError("Вы не правильно ввели координаты корабля!")
        else:
            raise ValueError(
                "Вы не правильно ввели данные, нужно ввести координаты слитно перечислив те клетки, "
                "в которых Вы хотите разместить корабль, например, А4А5А6А7 или Г3Д3Е3: ")

    @property
    def fleet(self):
        return self.fleet_composition

    @fleet.setter
    def fleet(self, value):
        fleet_composition = [[], [], [], []]
        if len(value) == 8:
            if len(fleet_composition[0] < 1):
                fleet_composition[0].append(value)
            else:
                raise ValueError("Вы уже добавили четырехпалубный корабль, добавьте оставшиеся корабли!")
        elif len(value) == 6:
            if len(fleet_composition[1] < 2):
                fleet_composition[1].append(value)
            else:
                raise ValueError("Вы уже добавили все трехпалубные корабли, добавьте оставшиеся корабли!")
        elif len(value) == 4:
            if len(fleet_composition[2] < 3):
                fleet_composition[2].append(value)
            else:
                raise ValueError("Вы уже добавили все двухпалубные корабли, добавьте оставшиеся корабли!")
        else:
            if len(fleet_composition[3] < 4):
                fleet_composition[3].append(value)
        return fleet_composition
