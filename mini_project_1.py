# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:04:23 2023

@author: 91931
"""

""". Problem Statement:
Find all the subsets from a set of numbers whose sum is zero.
Constraint: Subset size must be 5
Set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}"""
def find_zero_sum_subsets(nums):
    n = len(nums)
    subsets = []

    def backtrack(curr_set, start, target):
        if len(curr_set) == 5 and sum(curr_set) == target:
            subsets.append(curr_set)
            return
        if len(curr_set) > 5:
            return
        for i in range(start, n):
            backtrack(curr_set + [nums[i]], i + 1, target)

    backtrack([], 0, 0)
    return subsets


# Test the function
nums = [-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4]
zero_sum_subsets = find_zero_sum_subsets(nums)

# Print the subsets
for subset in zero_sum_subsets:
    print(subset)
