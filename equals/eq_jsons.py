import json


class NotEqualValueException(BaseException):
    pass


def _walk_trees(l_tree, r_tree):
    if isinstance(l_tree, dict) or isinstance(l_tree, list):
        if type(l_tree) != type(r_tree):
            raise NotEqualValueException

        if isinstance(l_tree, dict):
            for key, value in l_tree.items():
                if key not in r_tree:
                    raise NotEqualValueException
                _walk_trees(value, r_tree[key])

        if isinstance(l_tree, list):
            if len(l_tree) != len(r_tree):
                raise NotEqualValueException

            try:
                l_tree = sorted(l_tree)
                r_tree = sorted(r_tree)
            except TypeError:
                # Если массив объектов сортируем по первому попавшемуся ключу
                first_key = list(l_tree[0])[0]
                l_tree = sorted(l_tree, key=lambda x: x[first_key])
                r_tree = sorted(r_tree, key=lambda x: x[first_key])

            for index, _ in enumerate(l_tree):
                _walk_trees(l_tree[index], r_tree[index])
    else:
        if isinstance(l_tree, float):
            l_tree = round(l_tree, 5)
        if isinstance(r_tree, float):
            r_tree = round(r_tree, 5)

        if l_tree != r_tree:
            raise NotEqualValueException


def is_equal(left: str, right: str) -> bool:
    """
    equal(left: str, right: str)
    Функция принимает два объекта json и возвращает True, если объекты одинаковые.
    """
    l_left = json.loads(left)
    l_right = json.loads(right)

    try:
        if len(l_left) > len(l_right):
            raise NotEqualValueException
        if len(l_left) < len(l_right):
            raise NotEqualValueException

        _walk_trees(l_left, l_right)

    except NotEqualValueException:
        return False
    else:
        return True
