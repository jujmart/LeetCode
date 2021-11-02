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
def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_island = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_island = max(dfs(grid, i, j, rows, cols), max_island)
    return max_island


def dfs(grid, i, j, rows, cols):
    if(i >= rows or j >= cols or i < 0 or j < 0):
        return 0
    if(grid[i][j] != 1):
        return 0
    grid[i][j] = 2
    return 1+dfs(grid, i+1, j, rows, cols)+dfs(grid, i-1, j, rows, cols)+dfs(grid, i, j+1, rows, cols)+dfs(grid, i, j-1, rows, cols)

    # My NONWORKING Solution
    # ****************************
    # max_area = 0
    # row_len = len(grid[0])
    # col_len = len(grid)
    # visited = set()
    # stack = [[0, 0, 0]]
    # while len(stack):
    #     current = stack.pop()
    #     x = current[0]
    #     y = current[1]
    #     total = current[2]

    #     if f"{x},{y}" in visited:
    #         continue
    #     visited.add(f"{x},{y}")
    #     print(f"{x},{y}")
    #     if grid[y][x] == 1:
    #         total += 1
    #     else:
    #         max_area = max(max_area, total)
    #         total = 0

    #     print(total)
    #     if x + 1 < row_len:
    #         stack.append([x + 1, y, total])
    #     if x - 1 >= 0:
    #         stack.append([x - 1, y, total])
    #     if y + 1 < col_len:
    #         stack.append([x, y + 1, total])
    #     if y - 1 >= 0:
    #         stack.append([x, y - 1, total])

    # return max_area


grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(maxAreaOfIsland(grid1))  # 6
grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
print(maxAreaOfIsland(grid2))  # 0
