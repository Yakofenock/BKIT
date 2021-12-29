import random


def gen_random(num_count, begin, end):
    current = 0
    while current < num_count:
        current += 1
        yield random.randint(begin, end)
