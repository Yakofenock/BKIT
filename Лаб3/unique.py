from lab_python_fp.gen_random import gen_random
import types
import re


def sort(element):
    # curr = True
    # value_1 = re.split('\W', element.lower())
    # for data in Unique.DATA:
        # value_2 = re.split('\W', data.lower())
    if element.lower() not in Unique.DATA:
        Unique.DATA.add(element.lower())
        return element
    #     curr = False
    # if curr:
    #     Unique.DATA.add(element.lower())
    #     return element


class Unique(object):
    DATA = set()

    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.data = []
        if not self.ignore_case:
            [self.data.append(x) for x in items if sort(x) is not None]
        else:
            self.data = list(set(items))

        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False

    def __getitem__(self, index):
        return self.data[index]


if __name__ == '__main__':

    data = ['A', 'A', 'a', 'a', 'b', 'c']

    c = Unique(data, ignore_case=False)
    for value in c:
        print(value)