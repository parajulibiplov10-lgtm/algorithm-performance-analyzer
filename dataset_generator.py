
import random
from algorithms import merge_sort


# Generate random dataset
def generate_random_data(size):
    numbers = []

    for i in range(size):
        numbers.append(random.randint(1, 10000))

    return numbers


# Generate sorted dataset using the same values
def generate_sorted_data(numbers):
    sorted_numbers, comparisons, movements = merge_sort(numbers)

    return sorted_numbers


# Generate reverse sorted dataset using the same values
def generate_reverse_sorted_data(numbers):
    sorted_numbers = generate_sorted_data(numbers)

    reversed_numbers = []

    for i in range(len(sorted_numbers) - 1, -1, -1):
        reversed_numbers.append(sorted_numbers[i])

    return reversed_numbers
