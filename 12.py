import random, time
random.seed(1000)


def slow_sum(array):
    if not array:
        return 0
    return array[0] + slow_sum(array[1:])


def fast_sum(array):
    return _fast_sum(array, 0)


def _fast_sum(array, idx):
    if idx == len(array):
        return 0
    return array[idx] + _fast_sum(array, idx+1)


arr = [random.randint(0, 30) for _ in range(990)]

start = time.time()
print(sum(arr))
print(time.time() - start)

print()

start = time.time()
print(slow_sum(arr))
print(time.time() - start)

print()

start = time.time()
print(fast_sum(arr))
print(time.time() - start)

