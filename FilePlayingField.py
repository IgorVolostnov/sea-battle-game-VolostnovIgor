# Создаем класс "Игровое поле"
class PlayingField:
    def __init__(self, screen_game):
        self.screen_game = screen_game

    # Вывод на экран Игрового поля

    @property
    def output_screen(self):
        return self.screen_game

    @output_screen.getter
    def output_screen(self):
        separator = "          "
        number_field = [" "]
        name_field = ["\033[34m        Моё поле       \033[0m", separator, "\033[31m    Поле противника    \033[0m"]
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
                my_list_row_value = "|" + "\u0332" + self.screen_game[0][letter + str(number_)]
                my_value_field.append(my_list_row_value)
                enemy_list_row_value = "|" + "\u0332" + self.screen_game[1][letter + str(number_)]
                enemy_value_field.append(enemy_list_row_value)
            list_row = ["".join(my_value_field) + "|" + separator + "".join(enemy_value_field) + "|"]
            screen.append(list_row)
        for i in range(12):
            print("".join(screen[i]))
        return self.screen_game

    # Подсчет количества символов, оставшихся на игровом поле
    def symbol(self, value_):
        number_symbol0 = 0
        number_symbol1 = 0
        for item0 in self.screen_game[0].values():
            if item0 == value_:
                number_symbol0 += 1
        for item1 in self.screen_game[1].values():
            if item1 == value_:
                number_symbol1 += 1
        number_symbol = number_symbol0 + number_symbol1
        return number_symbol
