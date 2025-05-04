def get_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

print(get_indices([1, 2, 3, 2, 4], 2))  
