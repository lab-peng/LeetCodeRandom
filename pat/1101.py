# # 1101 Quick Sort
# # TODO: TIME EXCEEDED ERROR
# def get_pivots(width: int, nums: list) -> (int, list):
#     count = 0
#     pivots = []
#     sorted_nums = sorted(nums)
#     print(sorted_nums)
#
#     for i in range(width):
#         if nums[i] == sorted_nums[i]:
#             count += 1
#             pivots.append(nums[i])
#
#     return count, pivots
#
# def main():
#     # width = int(input(''))
#     # nums = [int(x) for x in input('').split()]
#     width = 5
#     nums = [1, 3, 2, 8, 5]
#
#     count, pivots = get_pivots(width, nums)
#     print(count)
#     print(' '.join([str(n) for n in pivots]))
#
#
# if __name__ == '__main__':
#     main()


def get_pivots(width, nums):
    count = 0
    pivots = []
    sorted_nums = sorted(nums)
    for i in range(width):
        if nums[i] == sorted_nums[i]:
            count += 1
            pivots.append(nums[i])
    return count, pivots


width = int(input(''))
nums = [int(x) for x in input('').split()]
count, pivots = get_pivots(width, nums)
print(count)
print(' '.join([str(n) for n in pivots]))
