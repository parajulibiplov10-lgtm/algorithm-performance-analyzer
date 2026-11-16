
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
