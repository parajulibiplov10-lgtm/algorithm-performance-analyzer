
##Bubble Sort Algorithm
def bubble_sort(arr):
    numbers = arr.copy()
    comparisons = 0
    swaps = 0

    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            comparisons += 1

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return numbers, comparisons, swaps

##Selection_sort


def selection_sort(arr):
    numbers = arr.copy()
    comparisons = 0
    swaps = 0

    n = len(numbers)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if numbers[j] < numbers[min_index]:
                min_index = j

        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            swaps += 1

    return numbers, comparisons, swaps

###Insertion Sort Algorithm

def insertion_sort(arr):
    numbers = arr.copy()
    comparisons = 0
    movements = 0

    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if numbers[j] > key:
                numbers[j + 1] = numbers[j]
                movements += 1
                j -= 1
            else:
                break

        numbers[j + 1] = key
        movements += 1

    return numbers, comparisons, movements

##Merger Sort Algorithm

def merge_sort(arr):
    numbers = arr.copy()
    comparisons = 0
    movements = 0

    def merge_sort_recursive(values):
        nonlocal comparisons, movements

        if len(values) <= 1:
            return values

        mid = len(values) // 2

        left = merge_sort_recursive(values[:mid])
        right = merge_sort_recursive(values[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            comparisons += 1

            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

            movements += 1

        while i < len(left):
            merged.append(left[i])
            movements += 1
            i += 1

        while j < len(right):
            merged.append(right[j])
            movements += 1
            j += 1

        return merged

    sorted_numbers = merge_sort_recursive(numbers)

    return sorted_numbers, comparisons, movements

# quick sort algorithm

def quick_sort(arr):
    numbers = arr.copy()
    comparisons = 0
    swaps = 0

    def partition(low, high):
        nonlocal comparisons, swaps

        pivot = numbers[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1

            if numbers[j] <= pivot:
                i += 1

                if i != j:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    swaps += 1

        pivot_index = i + 1

        if pivot_index != high:
            numbers[pivot_index], numbers[high] = (
                numbers[high], numbers[pivot_index]
            )
            swaps += 1

        return pivot_index

    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)

            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)

    quick_sort_recursive(0, len(numbers) - 1)

    return numbers, comparisons, swaps

