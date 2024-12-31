def calculate_structure_sum(values):
    sum_ = 0
    if isinstance(values, (int, float)):
        return values
    elif isinstance(values, str):
        return len(values)
    elif isinstance(values, (list, tuple, set)):
        for item in values:
            sum_ += calculate_structure_sum(item)
    elif isinstance(values, dict):
        for key, value in values.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)

    return sum_

data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
        ]

result = calculate_structure_sum(data_structure)
print(result)