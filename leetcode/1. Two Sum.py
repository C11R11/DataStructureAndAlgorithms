"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
"""
from collections import defaultdict

#Time Limit Exceeded
"""class Solution(object):
    def twoSum(self, nums, target):
        d = defaultdict(list)
        indices = []
        
        for n in range(len(nums)):
            for j in range(len(nums)):
                if n != j:
                    d[nums[n]+nums[j]] = [n,j]

        return d[target]
"""

#5237 the worst
"""
class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for j in range(len(nums)):
                if n != j:
                    if nums[n]+nums[j] == target:
                        return [n,j]
"""

#3810 ms N**2
"""class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1
        while nums[i] + nums[j] != target and i < len(nums):
            if j == len(nums) - 1:
                i += 1     
                j = i + 1
            else:
                j += 1
            
        return [i,j]
"""

#ChatGpt 50ms
class Solution(object):
    def twoSum(self, nums, target):    
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i

test_cases = [
    # Basic test cases
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    
    # Edge cases
    ([1, 2, 3, 4, 5], 5, [0, 3]),
    ([1, 2, 3, 4, 5], 6, [1, 3]),
    ([1, 2, 3, 4, 5], 7, [2, 3]),
    
    # Negative numbers
    ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ([-1, -2, -3, -4, 1, 2, 3, 4], -1, [1, 6]),
    ([-10, 7, 19, 15], 5, [0, 1]),
    
    # Mixed positive and negative numbers
    ([1, -2, 3, 0], 1, [0, 3]),
    ([2, 7, 11, -15], -4, [1, 3]),
    ([10, 22, 12, -2, 15, 7], 20, [2, 3]),
    
    # Large numbers
    ([1000000, 2000000, 3000000], 5000000, [1, 2]),
    ([123456789, 987654321, 111111111], 111111110, [0, 2]),
    ([999999, 1, 500000, 500001], 1000000, [2, 3]),
    
    # Duplicates
    ([5, 75, 25, 75], 100, [1, 2]),
    ([3, 2, 95, 4, 7], 99, [2, 3]),
    ([0, 4, 3, 0], 0, [0, 3]),
    
    # Larger list
    ([1, 5, 6, 8, 2, 4, 10], 10, [2, 4]),
    ([3, 8, 12, 17, 4, 7, 20], 15, [0, 5]),
]

s = Solution()
for i in range(10):
    print(f"result: {i} ", s.twoSum(test_cases[i][0], test_cases[i][1]), s.twoSum(test_cases[i][0], test_cases[i][1]) == test_cases[i][2])
        