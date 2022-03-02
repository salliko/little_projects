

def chunked(iterable, size):
    """
    Функция разбивает переданный список элементов
    на кортежи размером от 1 до <size> и возвращает их
    """
    res = []
    tmp = []
    for i in iterable:
        if len(tmp) == size:
            res.append(tuple(tmp))
            tmp = []
        tmp.append(i)
    if tmp:
        res.append(tuple(tmp))
    return res


result = list(chunked((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 5))
print(result)
assert [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)] == result

result = list(chunked(range(7), 3))
assert [(0, 1, 2), (3, 4, 5), (6,)] == result

result = list(chunked((i for i in range(7)), 3))
assert [(0, 1, 2), (3, 4, 5), (6,)] == result

result = list(chunked([1, 2], 100))
assert [(1, 2)] == result

result = list(chunked([1, 2, 3], 1))
assert [(1,), (2,), (3,)] == result

result = list(chunked([], 100))
assert [] == result

print('ok')
