def binary_search(numbers, value):
    if len(numbers) == 0:
        return str("Number {} is not in list".format(value))
    else:
        numbers = sorted(numbers)
        root_index = int(len(numbers) / 2)
        left_of_root = []
        right_of_root = []

        if numbers[root_index] == value:
            return str("Number {} is found in list".format(value))
        elif numbers[root_index] < value:
            right_of_root = numbers[root_index + 1:]
            return binary_search(right_of_root, value)
        elif numbers[root_index] > value:
            left_of_root = numbers[0: root_index]
            return binary_search(left_of_root, value)


print(binary_search([1, 4, 5, 2, 3, 2, 4], 0))