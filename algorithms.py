
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
