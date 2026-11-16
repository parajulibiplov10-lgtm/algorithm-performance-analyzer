
import random


# Generate random dataset
def generate_random_data(size):
    numbers = []

    for i in range(size):
        numbers.append(random.randint(1, 10000))

    return numbers


# Generate sorted dataset (ascending order)
def generate_sorted_data(size):
    numbers = []

    for i in range(1, size + 1):
        numbers.append(i)

    return numbers


# Generate reverse sorted dataset (descending order)
def generate_reverse_sorted_data(size):
    numbers = []

    for i in range(size, 0, -1):
        numbers.append(i)

    return numbers
