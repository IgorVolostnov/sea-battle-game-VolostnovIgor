# Создаем класс "Игровое поле"
class PlayingField:
    def __init__(self, my_field_values, enemy_field_values):
        self.my_field_values = my_field_values
        self.enemy_field_values = enemy_field_values

    # Вывод на экран Игрового поля
    @property
    def output_screen(self):
        separator = "          "
        number_field = [" "]
        name_field = ["        Моё поле       ", separator, "    Поле противника    "]
        string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
        for number_ in range(1, 11):
            element_string = " " + "\u0332" + str(number_)
            number_field.append(element_string)
        string_numbers_table = "".join(number_field)
        screen = [name_field, string_numbers_table + separator + string_numbers_table]
        for letter in string_letters_table:
            my_value_field = [letter]
            enemy_value_field = [letter]
            for number_ in range(1, 11):
                my_list_row_value = "|" + "\u0332" + self.my_field_values[letter + str(number_)]
                my_value_field.append(my_list_row_value)
                enemy_list_row_value = "|" + "\u0332" + self.enemy_field_values[letter + str(number_)]
                enemy_value_field.append(enemy_list_row_value)
            list_row = ["".join(my_value_field) + "|" + separator + "".join(enemy_value_field) + "|"]
            screen.append(list_row)
        for i in range(12):
            print("".join(screen[i]))

    def location_ships(self, coordinates):
        shit = coordinates[0]
        value_around_shit = coordinates[1]
        for key, item in shit.items():
            if key in self.my_field_values.keys():
                self.my_field_values[key] = item
        for key, item in value_around_shit.items():
            if key in self.my_field_values.keys():
                self.my_field_values[key] = item
        return self.my_field_values
