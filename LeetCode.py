# Problem 704
def search(nums, target):
    if target < nums[0] or target > nums[-1]:
        return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
