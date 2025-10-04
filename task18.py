def square_values(data: list) -> list:
    return [{'value': item['value'] ** 2} for item in data]

print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))
# [{'value': 4}, {'value': 9}, {'value': 16}]

print(square_values([{'value': -2}, {'value': 5}]))
# [{'value': 4}, {'value': 25}]