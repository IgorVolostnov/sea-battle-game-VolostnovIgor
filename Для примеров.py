def generator_item(iterable_object):
    iterator = iter(iterable_object)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield prev_item, current_item, next_item
        prev_item = current_item
        current_item = next_item
    yield prev_item, current_item, None


string_letters_table = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
list_values = []
for letter_ in string_letters_table:
    list_ = []
    for i in range(1, 11):
        list_.append(letter_ + str(i))
    list_values.append(list_)
print(list_values)
four_decked_ships = {}
for my_list in list_values:
    for number_ in range(7):
        four_decked_ships[my_list[number_]] = "".join(my_list[number_ :number_ + 4])

print(four_decked_ships)

