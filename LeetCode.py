import copy

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


# Problem 189
# def rotate(nums, k):
#     # Optimal Solution
#     new_k = k % len(nums)
#     nums[0:0] = nums[-new_k:]
#     nums[-new_k:] = []
#     return nums

#     # My Solution
#     # new_nums = nums[-new_k:] + nums[:-new_k]
#     # for i in range(len(nums)):
#     #     nums.pop()
#     # # Another Solution (only for Python3 I think)
#     # # nums.clear()
#     # nums.extend(new_nums)
#     # return nums


# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(rotate(numbers, 3))
# print(numbers)
# print(rotate([-1, -100, 3, 99], 2))

# Problem 283
# def moveZeroes(nums):
#     pointer = len(nums) - 1
#     idx = 0
#     while idx < pointer:
#         if nums[idx] == 0:
#             nums[idx:] = nums[idx + 1:]
#             nums.append(0)
#             pointer -= 1
#         else:
#             idx += 1


# arr = [0, 1, 0, 3, 12]
# moveZeroes(arr)
# print(arr)
# arr2 = [0]
# moveZeroes(arr2)
# print(arr2)

# Problem 167
# def twoSum(numbers, target):
#     obj = {}
#     for i in range(len(numbers)):
#         num = numbers[i]
#         obj[target - num] = i

#     for i in range(len(numbers)):
#         num = numbers[i]
#         if obj.get(num):
#             return [min(obj[num] + 1, i + 1), max(obj[num] + 1, i + 1)]


# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([2, 3, 4], 6))
# print(twoSum([-1, 0], -1))
# print(twoSum([5, 25, 75], 100))

# Problem 344
# def reverseString(s):
#     for i in range(len(s)):
#         s[i:i] = s.pop()


# str1 = ["h", "e", "l", "l", "o"]
# reverseString(str1)
# print(str1)
# str2 = ["H", "a", "n", "n", "a", "h"]
# reverseString(str2)
# print(str2)

# Problem 557
# def reverseWords(s):
#     split = s.split(" ")
#     for i in range(len(split)):
#         word = split[i]
#         word_arr = []
#         for j in range(len(word) - 1, -1, -1):
#             word_arr.append(word[j])
#         split[i] = "".join(word_arr)
#     return " ".join(split)


# str1 = "Let's take LeetCode contest"
# print(reverseWords(str1))
# str2 = "God Ding"
# print(reverseWords(str2))

# Problem 567
# def checkInclusion(s1, s2):
#     s1_len = len(s1)
#     s2_len = len(s2)

#     def letter_count(str):
#         obj = {}
#         for char in str:
#             if obj.get(char):
#                 obj[char] += 1
#             else:
#                 obj[char] = 1
#         return obj

#     c1 = letter_count(s1)
#     for i in range(s2_len - s1_len + 1):
#         c2 = letter_count(s2[i:i+s1_len])
#         if c1 == c2:
#             return True

#     return False


# print(checkInclusion("ab", "eidbaooo"))  # true
# print(checkInclusion("ab", "eidboaoo"))  # false
# print(checkInclusion("abc", "bbbca"))  # true

# Problem 733
# def floodFill(image, sr, sc, newColor):
#     stack = [[sc, sr]]
#     old_color = image[sr][sc]
#     row_len = len(image[0])
#     col_len = len(image)
#     visited = set()
#     while len(stack):
#         current = stack.pop()
#         x = current[0]
#         y = current[1]

#         if f"{x},{y}" in visited:
#             continue
#         visited.add(f"{x},{y}")

#         if image[y][x] == old_color:
#             image[y][x] = newColor
#             if x + 1 < row_len:
#                 stack.append([x + 1, y])
#             if x - 1 >= 0:
#                 stack.append([x - 1, y])
#             if y + 1 < col_len:
#                 stack.append([x, y + 1])
#             if y - 1 >= 0:
#                 stack.append([x, y - 1])
#     return image


# image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(floodFill(image1, 1, 1, 2))
# image2 = [[0, 0, 0], [0, 0, 0]]
# print(floodFill(image2, 0, 0, 2))

# Problem 695
# def maxAreaOfIsland(grid):
#     rows = len(grid)
#     cols = len(grid[0])

#     max_island = 0
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == 1:
#                 max_island = max(dfs(grid, i, j, rows, cols), max_island)
#     return max_island


# def dfs(grid, i, j, rows, cols):
#     if(i >= rows or j >= cols or i < 0 or j < 0):
#         return 0
#     if(grid[i][j] != 1):
#         return 0
#     grid[i][j] = 2
#     return 1+dfs(grid, i+1, j, rows, cols)+dfs(grid, i-1, j, rows, cols)+dfs(grid, i, j+1, rows, cols)+dfs(grid, i, j-1, rows, cols)

#     # My NONWORKING Solution
#     # ****************************
#     # max_area = 0
#     # row_len = len(grid[0])
#     # col_len = len(grid)
#     # visited = set()
#     # stack = [[0, 0, 0]]
#     # while len(stack):
#     #     current = stack.pop()
#     #     x = current[0]
#     #     y = current[1]
#     #     total = current[2]

#     #     if f"{x},{y}" in visited:
#     #         continue
#     #     visited.add(f"{x},{y}")
#     #     print(f"{x},{y}")
#     #     if grid[y][x] == 1:
#     #         total += 1
#     #     else:
#     #         max_area = max(max_area, total)
#     #         total = 0

#     #     print(total)
#     #     if x + 1 < row_len:
#     #         stack.append([x + 1, y, total])
#     #     if x - 1 >= 0:
#     #         stack.append([x - 1, y, total])
#     #     if y + 1 < col_len:
#     #         stack.append([x, y + 1, total])
#     #     if y - 1 >= 0:
#     #         stack.append([x, y - 1, total])

#     # return max_area


# grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
# print(maxAreaOfIsland(grid1))  # 6
# grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
# print(maxAreaOfIsland(grid2))  # 0


# Problem 617
# def mergeTrees(root1, root2):
#     if not root1 and not root2:
#         return None
#     stack1 = [root1]
#     stack2 = [root2]
#     new_tree = TreeNode()
#     current_tree_stack = [new_tree]
#     while len(stack1) or len(stack2):
#         current1 = stack1.pop()
#         current2 = stack2.pop()
#         current_tree = current_tree_stack.pop()
#         if not current1 and not current2:
#             continue
#         elif not current1:
#             current_tree.val = current2.val
#             if current2.left:
#                 stack1.append(None)
#                 stack2.append(current2.left)
#                 current_tree.left = TreeNode()
#                 current_tree_stack.append(current_tree.left)
#             if current2.right:
#                 stack1.append(None)
#                 stack2.append(current2.right)
#                 current_tree.right = TreeNode()
#                 current_tree_stack.append(current_tree.right)
#         elif not current2:
#             current_tree.val = current1.val
#             if current1.left:
#                 stack2.append(None)
#                 stack1.append(current1.left)
#                 current_tree.left = TreeNode()
#                 current_tree_stack.append(current_tree.left)
#             if current1.right:
#                 stack2.append(None)
#                 stack1.append(current1.right)
#                 current_tree.right = TreeNode()
#                 current_tree_stack.append(current_tree.right)
#         else:
#             current_tree.val = current1.val + current2.val
#             if current1.left or current2.left:
#                 current_tree.left = TreeNode()
#             if current1.right or current2.right:
#                 current_tree.right = TreeNode()
#             stack1.extend([current1.left, current1.right])
#             stack2.extend([current2.left, current2.right])
#             current_tree_stack.extend([current_tree.left, current_tree.right])

#     return new_tree

# Problem 34
# def searchRange(nums, target):
#     result = [-1, -1]
#     stack = [[nums, 0]]
#     while len(stack):
#         current = stack.pop()
#         current_lst = current[0]
#         add_idx = current[1]

#         if len(current_lst) == 0:
#             continue

#         mid_idx = len(current_lst) // 2
#         total_idx = mid_idx + add_idx

#         if target == current_lst[mid_idx]:
#             if result[0] == -1:
#                 result[0] = total_idx
#             if result[1] == -1:
#                 result[1] = total_idx
#             result = [min(result[0], total_idx), max(result[1], total_idx)]
#             stack.extend([[current_lst[:mid_idx], add_idx], [
#                          current_lst[mid_idx + 1:], total_idx + 1]])
#         elif target < current_lst[mid_idx]:
#             stack.append([current_lst[:mid_idx], add_idx])
#         elif target > current_lst[mid_idx]:
#             stack.append([current_lst[mid_idx + 1:], total_idx + 1])

#     return result


# print(searchRange([5, 7, 7, 8, 8, 10], 8))
# print(searchRange([5, 7, 7, 8, 8, 10], 6))
# print(searchRange([], 0))


# Sisu Problem
# data = [
#     {"age": 15, "gender": 'M', "time_of_day": 'morning',
#         "order_contents": 'Happy Meal'},
#     {"age": 21, "gender": 'F', "time_of_day": 'afternoon',
#         "order_contents": 'McFlurry'},
#     {"age": 22, "gender": 'F', "time_of_day": 'evening', "order_contents": 'Big Mac'},
#     {"age": 28, "gender": 'N/A', "time_of_day": 'morning',
#         "order_contents": 'Dollar Menu'}
# ]

# 15  M  morning  Happy Meal
# 15  M  morning  McFlurry
# 15  M  morning  Big Mac
# 15  M  morning  Dollar Menu
# 15  M  afternoon  Happy Meal
# 15  M  afternoon  McFlurry
# 15  M  afternoon  Big Mac
# 15  M  afternoon  Dollar Menu
# 15  M  evening  Happy Meal
# 15  M  evening  McFlurry
# 15  M  evening  Big Mac
# 15  M  evening  Dollar Menu
# 15  F  morning  Happy Meal
# 15  F  morning  McFlurry
# 15  F  morning  Big Mac
# 15  F  morning  Dollar Menu
# 15  F  afternoon  Happy Meal
# 15  F  afternoon  McFlurry
# 15  F  afternoon  Big Mac
# 15  F  afternoon  Dollar Menu
# 15  F  evening  Happy Meal
# 15  F  evening  McFlurry
# 15  F  evening  Big Mac
# 15  F  evening  Dollar Menu
# 15  N/A  morning  Happy Meal
# 15  N/A  morning  McFlurry
# 15  N/A  morning  Big Mac
# 15  N/A  morning  Dollar Menu
# 15  N/A  afternoon  Happy Meal
# 15  N/A  afternoon  McFlurry
# 15  N/A  afternoon  Big Mac
# 15  N/A  afternoon  Dollar Menu
# 15  N/A  evening  Happy Meal
# 15  N/A  evening  McFlurry
# 15  N/A  evening  Big Mac
# 15  N/A  evening  Dollar Menu
# 21  M  morning  Happy Meal
# 21  M  morning  McFlurry
# 21  M  morning  Big Mac
# 21  M  morning  Dollar Menu
# 21  M  afternoon  Happy Meal
# 21  M  afternoon  McFlurry
# 21  M  afternoon  Big Mac
# 21  M  afternoon  Dollar Menu
# 21  M  evening  Happy Meal
# 21  M  evening  McFlurry
# 21  M  evening  Big Mac
# 21  M  evening  Dollar Menu
# 21  F  morning  Happy Meal
# 21  F  morning  McFlurry
# 21  F  morning  Big Mac
# 21  F  morning  Dollar Menu
# 21  F  afternoon  Happy Meal
# 21  F  afternoon  McFlurry
# 21  F  afternoon  Big Mac
# 21  F  afternoon  Dollar Menu
# 21  F  evening  Happy Meal
# 21  F  evening  McFlurry
# 21  F  evening  Big Mac
# 21  F  evening  Dollar Menu
# 21  N/A  morning  Happy Meal
# 21  N/A  morning  McFlurry
# 21  N/A  morning  Big Mac
# 21  N/A  morning  Dollar Menu
# 21  N/A  afternoon  Happy Meal
# 21  N/A  afternoon  McFlurry
# 21  N/A  afternoon  Big Mac
# 21  N/A  afternoon  Dollar Menu
# 21  N/A  evening  Happy Meal
# 21  N/A  evening  McFlurry
# 21  N/A  evening  Big Mac
# 21  N/A  evening  Dollar Menu
# 22  M  morning  Happy Meal
# 22  M  morning  McFlurry
# 22  M  morning  Big Mac
# 22  M  morning  Dollar Menu
# 22  M  afternoon  Happy Meal
# 22  M  afternoon  McFlurry
# 22  M  afternoon  Big Mac
# 22  M  afternoon  Dollar Menu
# 22  M  evening  Happy Meal
# 22  M  evening  McFlurry
# 22  M  evening  Big Mac
# 22  M  evening  Dollar Menu
# 22  F  morning  Happy Meal
# 22  F  morning  McFlurry
# 22  F  morning  Big Mac
# 22  F  morning  Dollar Menu
# 22  F  afternoon  Happy Meal
# 22  F  afternoon  McFlurry
# 22  F  afternoon  Big Mac
# 22  F  afternoon  Dollar Menu
# 22  F  evening  Happy Meal
# 22  F  evening  McFlurry
# 22  F  evening  Big Mac
# 22  F  evening  Dollar Menu
# 22  N/A  morning  Happy Meal
# 22  N/A  morning  McFlurry
# 22  N/A  morning  Big Mac
# 22  N/A  morning  Dollar Menu
# 22  N/A  afternoon  Happy Meal
# 22  N/A  afternoon  McFlurry
# 22  N/A  afternoon  Big Mac
# 22  N/A  afternoon  Dollar Menu
# 22  N/A  evening  Happy Meal
# 22  N/A  evening  McFlurry
# 22  N/A  evening  Big Mac
# 22  N/A  evening  Dollar Menu
# 28  M  morning  Happy Meal
# 28  M  morning  McFlurry
# 28  M  morning  Big Mac
# 28  M  morning  Dollar Menu
# 28  M  afternoon  Happy Meal
# 28  M  afternoon  McFlurry
# 28  M  afternoon  Big Mac
# 28  M  afternoon  Dollar Menu
# 28  M  evening  Happy Meal
# 28  M  evening  McFlurry
# 28  M  evening  Big Mac
# 28  M  evening  Dollar Menu
# 28  F  morning  Happy Meal
# 28  F  morning  McFlurry
# 28  F  morning  Big Mac
# 28  F  morning  Dollar Menu
# 28  F  afternoon  Happy Meal
# 28  F  afternoon  McFlurry
# 28  F  afternoon  Big Mac
# 28  F  afternoon  Dollar Menu
# 28  F  evening  Happy Meal
# 28  F  evening  McFlurry
# 28  F  evening  Big Mac
# 28  F  evening  Dollar Menu
# 28  N/A  morning  Happy Meal
# 28  N/A  morning  McFlurry
# 28  N/A  morning  Big Mac
# 28  N/A  morning  Dollar Menu
# 28  N/A  afternoon  Happy Meal
# 28  N/A  afternoon  McFlurry
# 28  N/A  afternoon  Big Mac
# 28  N/A  afternoon  Dollar Menu
# 28  N/A  evening  Happy Meal
# 28  N/A  evening  McFlurry
# 28  N/A  evening  Big Mac
# 28  N/A  evening  Dollar Menu


# Problem 18
# def fourSum(nums, target):
#     nums.sort()
#     s = set()
#     for i in range(len(nums) - 3):
#         if i == 0 or nums[i] != nums[i - 1]:
#             for j in range(i + 1, len(nums)-2):
#                 k = j + 1
#                 l = len(nums) - 1
#                 while k < l:
#                     total = nums[i] + nums[j] + nums[k] + nums[l]
#                     if total < target:
#                         k += 1
#                     elif total > target:
#                         l -= 1
#                     else:
#                         s.add((nums[i], nums[j], nums[k], nums[l]))
#                         k += 1
#                         l -= 1

#     return s


# print(fourSum([1, 0, -1, 0, -2, 2], 0))
# print(fourSum([2, 2, 2, 2, 2], 8))

# Problem 21
# def mergeTwoLists(list1, list2):
#     head = ListNode()
#     if not list1:
#         return list2
#     if not list2:
#         return list1
#     if list1.val < list2.val:
#         head.val = list1.val
#         current_list1 = list1.next
#         current_list2 = list2
#     else:
#         head.val = list2.val
#         current_list1 = list1
#         current_list2 = list2.next
#     current = head
#     while current_list1 and current_list2:
#         if current_list1.val < current_list2.val:
#             current.next = ListNode(current_list1.val)
#             current = current.next
#             current_list1 = current_list1.next
#         else:
#             current.next = ListNode(current_list2.val)
#             current = current.next
#             current_list2 = current_list2.next

#     if current_list1:
#         current.next = current_list1
#     if current_list2:
#         current.next = current_list2
#     return head


# Problem 206
# def reverseList(head):
#     if not head:
#         return head
#     stack = []
#     current = head
#     while current:
#         stack.append(current.val)
#         current = current.next

#     new_head = ListNode(stack.pop())
#     current_head = new_head
#     while len(stack):
#         current_val = stack.pop()
#         current_head.next = ListNode(current_val)
#         current_head = current_head.next
#     return new_head


# Problem 77
# def combine(n, k):
#     current = []
#     result = set()

#     def checkCurrent(num, k):
#         length = len(current)
#         for i in range(length):
#             new_arr = current[i][:]
#             new_arr.append(num)
#             if len(new_arr) < k:
#                 current.append(new_arr)
#             elif len(new_arr) == k:
#                 result.add(tuple(new_arr))
#         current.append([num])

#     if k == 1:
#         for i in range(n):
#             result.add(tuple([i + 1]))
#         return result
#     for i in range(n):
#         checkCurrent(i + 1, k)
#     return result


# print(combine(4, 2))  # [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
# print(combine(1, 1))  # [[1]]


# Problem 1
# def twoSum(nums, target):
#     differences = {}
#     for i, num in enumerate(nums):
#         if target - num not in differences:
#             differences[target - num] = [i]
#         else:
#             differences[target - num].append(i)
#     for i, num in enumerate(nums):
#         difference_list = None
#         if num in differences:
#             difference_list = differences[num]
#         if difference_list != None:
#             for difference in difference_list:
#                 if difference != i:
#                     return [difference, i]


# print(twoSum([2, 7, 11, 15], 9))  # [0,1]

# Problem 15
# def threeSum(nums):
#     if not nums or len(nums) < 3:
#         return []
#     result = set()
#     nums_sorted = sorted(nums)
#     length = len(nums_sorted)
#     for i, num in enumerate(nums_sorted):
#         left = i + 1
#         right = length - 1
#         while left < right:
#             sum = num + nums_sorted[left] + nums_sorted[right]
#             if sum == 0:
#                 result.add(tuple([num, nums_sorted[left], nums_sorted[right]]))
#                 right -= 1
#             elif sum > 0:
#                 right -= 1
#             elif sum < 0:
#                 left += 1
#     return result


# print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2], [-1,0,1]]
# print(threeSum([]))  # []
# print(threeSum([0]))  # []


# Problem 116
# def connect(root):
#     if not root or not root.left:
#         return root
#     queue = [root.left, root.right]
#     level_queue = [2, 2]
#     while len(queue):
#         current_level = level_queue.pop(0)
#         current_node = queue.pop(0)
#         if not len(queue):
#             return root

#         if not current_node.left:
#             current_node.next = queue[0]
#             continue

#         queue.extend([current_node.left, current_node.right])
#         level_queue.extend([current_level + 1, current_level + 1])

#         if current_level == level_queue[0]:
#             current_node.next = queue[0]

#     return root


# Problem 542 works but time limit exceeded
def nearestZeroMoves(mat, x, y):
    queue = [[x, y, 0]]
    min_move = float('Inf')
    visited = set()
    while len(queue):
        new_x = queue[0][0]
        new_y = queue[0][1]
        move = queue.pop(0)[2]

        if (new_x, new_y) in visited:
            continue
        visited.add((new_x, new_y))

        if mat[new_y][new_x] == 0:
            return min(move, min_move)

        if mat[new_y][new_x] != 'x':
            min_move = min(min_move, move + mat[new_y][new_x])
        else:
            if new_x + 1 < len(mat[0]):
                queue.append([new_x + 1, new_y, move + 1])
            if new_x - 1 >= 0:
                queue.append([new_x - 1, new_y, move + 1])
            if new_y + 1 < len(mat):
                queue.append([new_x, new_y + 1, move + 1])
            if new_y - 1 >= 0:
                queue.append([new_x, new_y - 1, move + 1])

    return min_move


def updateMatrix(mat):
    new_mat = copy.deepcopy(mat)
    for y in range(len(new_mat)):
        for x in range(len(new_mat[0])):
            if new_mat[y][x] != 0:
                new_mat[y][x] = 'x'

    for y in range(len(new_mat)):
        for x in range(len(new_mat[0])):
            if new_mat[y][x] != 0:
                new_mat[y][x] = nearestZeroMoves(new_mat, x, y)
    return new_mat


# [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
# [[0,0,0],[0,1,0],[1,2,1]]
print(updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
# [[1,0,1,1,0,0,1,0,0,1],
# [0,1,1,0,1,0,1,0,1,1],
# [0,0,1,0,1,0,0,1,0,0],
# [1,0,1,0,1,1,1,1,1,1],
# [0,1,0,1,1,0,0,0,0,1],
# [0,0,1,0,1,1,1,0,1,0],
# [0,1,0,1,0,1,0,0,1,1],
# [1,0,0,0,1,2,1,1,0,1],
# [2,1,1,1,1,2,1,0,1,0],
# [3,2,2,1,0,1,0,0,1,1]]
print(updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                    [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))
