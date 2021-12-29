import json
from print_result import print_result
import unique
from gen_random import gen_random
from cm_timer import cm_timer_1

# Сделаем другие необходимые импорты

path = "C:\\Users\\yakers\\Python_education_projects\\lab_3\\data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, "r", encoding='utf8') as f:
    data = json.load(f)
    args = (job["job-name"] for job in data)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(args):
    return sorted(unique.Unique(args, ignore_case=False).data)


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист") is True, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    add_1 = list(map(lambda x: x + ' с зарплатой ', arg))
    add_2 = list(zip(add_1, list(map(str, list(gen_random(len(arg), 100000, 200000))))))
    return list(map(lambda x: ''.join(x), add_2))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(args))))
