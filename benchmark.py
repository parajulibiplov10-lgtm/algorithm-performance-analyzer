
import time


def benchmark_algorithm(algorithm, numbers):
    start_time = time.perf_counter()

    sorted_numbers, comparisons, operations = algorithm(numbers)

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    return sorted_numbers, execution_time, comparisons, operations
