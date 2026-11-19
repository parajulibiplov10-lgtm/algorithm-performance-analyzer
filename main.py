
from algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
numbers = [7, 3, 5, 2, 9]

# Bubble Sort
print("\n--- Bubble Sort ---")

sorted_numbers, comparisons, swaps = bubble_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


# Selection Sort
print("\n--- Selection Sort ---")

sorted_numbers, comparisons, swaps = selection_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


# Insertion Sort
print("\n--- Insertion Sort ---")

sorted_numbers, comparisons, movements = insertion_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Movements:", movements)


# Merge Sort
print("\n--- Merge Sort ---")

sorted_numbers, comparisons, movements = merge_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Movements:", movements)

# Quick Sort
print("\n--- Quick Sort ---")

sorted_numbers, comparisons, swaps = quick_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

##Test the Dataset Generator


from dataset_generator import (
    generate_random_data,
    generate_sorted_data,
    generate_reverse_sorted_data
)

print("\n--- Dataset Generator Test ---")

random_data = generate_random_data(10)
sorted_data = generate_sorted_data(random_data)
reverse_data = generate_reverse_sorted_data(random_data)

print("Random:", random_data)
print("Sorted:", sorted_data)
print("Reverse Sorted:", reverse_data)


from benchmark import benchmark_algorithm

print("\n--- Benchmark Test ---")

test_numbers = generate_random_data(100)

sorted_numbers, execution_time, comparisons, operations = (
    benchmark_algorithm(bubble_sort, test_numbers)
)

print("Algorithm: Bubble Sort")
print("Dataset Size:", len(test_numbers))
print("Execution Time:", round(execution_time, 4), "ms")
print("Comparisons:", comparisons)
print("Swaps:", operations)
