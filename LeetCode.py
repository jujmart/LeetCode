# Problem 704
# def search(nums, target):
#     if target < nums[0] or target > nums[-1]:
#         return -1
#     stack = [nums]
#     result = 0
#     while len(stack):
#         current = stack.pop()
#         if len(current) == 0:
#             return -1
#         mid_idx = len(current) // 2
#         mid_num = current[mid_idx]
#         if mid_num == target:
#             return result + mid_idx
#         elif mid_num > target:
#             stack.append(current[:mid_idx])
#         else:
#             result += mid_idx + 1
#             stack.append(current[mid_idx + 1:])
#     return result


# print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
# print(search([-1, 0, 3, 5, 9, 12], 2))  # -1
# print(search([-1, 0, 3, 5, 9, 12], 3))  # 2
# print(search([-1, 0, 3, 5, 9, 12], 0))  # 1
# print(search([-1, 0, 3, 5, 9, 12], -1))  # 0
# print(search([-1, 0, 3, 5, 9, 12], -2))  # -1
# print(search([-1, 0, 3, 5, 9, 12], 13))  # -1
# print(search([-1, 0, 3, 5, 9, 12], 12))  # 5
# print(search([-1, 0, 3, 5, 9, 12], 5))  # 3
# print(search([-1, 0, 3, 5, 9, 12], 7))  # -1


# Problem 278
# def firstBadVersion(n):
#     if n == 1:
#         return 1
#     stack = [n // 2]
#     left = 1
#     right = n
#     while len(stack) and left < right:
#         current = stack.pop()
#         print(current, left, right)
#         if isBadVersion(current):
#             right = current
#             # if right == left:
#             #     return left
#             # if current == left + 1:
#             #     return current
#         else:
#             left = current + 1
#         stack.append((right + left) // 2)
#     return left


# def isBadVersion(n):
#     if n == 2:
#         return False
#     if n == 3:
#         return False
#     if n == 4:
#         return True
#     if n == 5:
#         return True


# print(firstBadVersion(5))
# print(firstBadVersion(1))
# print(firstBadVersion(4))

# Problem 35
# def searchInsert(nums, target):
#     if (target < nums[0]):
#         return 0
#     if (target > nums[-1]):
#         return len(nums)

#     mid_idx = len(nums) // 2
#     stack = [mid_idx]
#     result = 0
#     while len(stack):
#         current_idx = stack.pop()
#         current = nums[current_idx]
#         if target == current or (target < current and target > nums[current_idx - 1]):
#             return current_idx
#         if target < current:
#             stack.append((current_idx + result) // 2)
#         else:
#             result = current_idx
#             stack.append((current_idx + len(nums)) // 2)
#     return result


# print(searchInsert([1, 3, 5, 6], 5))
# print(searchInsert([1, 3, 5, 6], 2))
# print(searchInsert([1, 3, 5, 6], 7))
# print(searchInsert([1, 3, 5, 6], 0))
# print(searchInsert([1], 0))
# print(searchInsert([1, 3], 1))

# Problem 977
# def sortedSquares(nums):
#     def square(num):
#         return num ** 2
#     if nums[0] >= 0:
#         return list(map(square, nums))
#     elif nums[-1] < 0:
#         result = []
#         for i in range(len(nums) - 1, -1, -1):
#             result.append(square(nums[i]))
#         return result
#     else:
#         left_pointer = -1
#         idx = 1
#         while left_pointer == -1:
#             if nums[idx] >= 0:
#                 left_pointer = idx - 1
#             idx += 1

#         result = []
#         right_pointer = left_pointer + 1
#         while right_pointer < len(nums) or left_pointer >= 0:
#             if right_pointer >= len(nums):
#                 result.append(square(nums[left_pointer]))
#                 left_pointer -= 1
#             elif left_pointer < 0:
#                 result.append(square(nums[right_pointer]))
#                 right_pointer += 1
#             else:
#                 if (square(nums[left_pointer]) < square(nums[right_pointer])):
#                     result.append(square(nums[left_pointer]))
#                     left_pointer -= 1
#                 else:
#                     result.append(square(nums[right_pointer]))
#                     right_pointer += 1
#         return result


# print(sortedSquares([-4, -1, 0, 3, 10]))
# print(sortedSquares([-7, -3, 2, 3, 11]))
# print(sortedSquares([0, 3, 10]))
# print(sortedSquares([-13, -10, -5]))
# print(sortedSquares([-1, 1]))
