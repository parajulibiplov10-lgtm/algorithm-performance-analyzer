
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

