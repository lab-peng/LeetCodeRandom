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
print()


def selection(arr):  # in place the current array
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]


array = [random.randint(1, 30) for i in range(10)]
print(array)
selection(array)
print(array)
print()


# 2 quick sort
def quick_sort(arr):
    if not arr:
        return []
    pivot = arr[0]
    lower = [i for i in arr[1:] if i < pivot]
    higher = [i for i in arr[1:] if i >= pivot]
    return [*quick_sort(lower), pivot, *quick_sort(higher)]


array = [random.randint(1, 30) for i in range(10)]
print(array)
print(quick_sort(array))
print()


# 3 bubble sort:
def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    # return arr


array = [random.randint(1, 30) for i in range(10)]
print(array)
bubble_sort(array)
print(array)
print()


# 4 merge sort
def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        merge_sort(left)
        merge_sort(right)

        l, r, i = 0, 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1


array = [random.randint(1, 30) for i in range(10)]
print(array)
merge_sort(array)
print(array)
print()


# 5 insertion sort   https://www.youtube.com/watch?v=byHi41L9vTM&list=PLc_Ps3DdrcTsizjAG5uMhpoDfhDmxpOzv&index=3
def insertion_sort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1


array = [random.randint(1, 30) for i in range(10)]
print(array)
insertion_sort(array)
print(array)
print()

# 6 counting sort 7 radix sort 8 bucket sort 9 heap sort 10 shell sort


