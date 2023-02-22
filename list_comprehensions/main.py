list = [1, 2, 'a', 'b', 'c', 3, 4, 5, 6, 7, 8, 9, 10]

def filter_list(list):
    return [x for x in list if type(x) == int and x > 0]

print(filter_list(list))