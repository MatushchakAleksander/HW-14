def delete_item(obj: list, position: int) -> list:
    position -= 1
    del obj[position]

    for elem in obj[position:]:
        elem['position'] -= 1
    return obj


data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]

delete_item(data, 1)
print('1.Удаление элемента:')
print(data)
print('--------------------------------------')


def add_item(obj: list, name: str, position: int) -> list:
    obj.insert(position - 1, {'name': name, 'position': position})

    for elem in obj[position:]:
        elem['position'] += 1
    return obj


data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]
add_item(data, 'Test 4', 1)
print('2.Добавить элемент :')
print(data)
print('--------------------------------------')


def swap_item(obj: list, position_1: int, position_2: int) -> list:
    # arguments_validate(lst, pos_1, pos_2)

    obj[position_1 - 1]['name'], obj[position_2 - 1]['name'] = obj[position_2 - 1]['name'], obj[position_1 - 1]['name']

    return obj


data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]

swap_item(data, 1, 3)
print('Поменять элементы местами:')
print(data)
print('--------------------------------------')
