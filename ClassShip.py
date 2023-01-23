class Ship:

    def __init__(self, ship_coordinates, dict_values, condition_ship):
        self.ship_coordinates = ship_coordinates
        self.dict_values = dict_values
        self.condition_ship = condition_ship

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
        for key, item in self.ship_coordinates[0]:
            if key in self.dict_values.keys():
                self.dict_values[key] = item
        for key, item in self.ship_coordinates[1]:
            if key in self.dict_values.keys():
                self.dict_values[key] = item
