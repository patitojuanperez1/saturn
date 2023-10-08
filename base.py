# Random functions

import random


def random_percentage():
    return round(random.random() * 100, 2)


def print_percentage(x):
    print(f"{100 * x:.2f}%")
