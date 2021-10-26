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
