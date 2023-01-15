import random

random.seed(10)


# 1 selection sort
def selection_sort(arr):
    def find_smallest(lst):
        smallest = float('inf')
        for a in lst:
            if a < smallest:
                smallest = a
        return smallest

    res = []
    for i in range(len(arr)):
        current = find_smallest(arr)
        res.append(current)
        arr.remove(current)
    return res


array = [random.randint(1, 30) for i in range(10)]
print(array)
print(selection_sort(array))


# quick sort
def quicksort(arr):
    if not arr:
        return []
    pivot = arr[0]
    lower = [i for i in arr[1:] if i < pivot]
    higher = [i for i in arr[1:] if i >= pivot]
    return [*quicksort(lower), pivot, *quicksort(higher)]


array = [random.randint(1, 30) for i in range(10)]
print(array)
print(quicksort(array))
