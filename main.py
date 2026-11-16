
from algorithms import bubble_sort

numbers = [7, 3, 5, 2, 9]

sorted_numbers, comparisons, swaps = bubble_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


from algorithms import selection_sort

numbers = [7, 3, 5, 2, 9]

sorted_numbers, comparisons, swaps = selection_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

from algorithms import bubble_sort, selection_sort, insertion_sort;

print("\n--- Insertion Sort ---")

numbers = [7, 3, 5, 2, 9]

sorted_numbers, comparisons, movements = insertion_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Comparisons:", comparisons)
print("Movements:", movements)
