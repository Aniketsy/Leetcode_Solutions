# -*- coding: utf-8 -*-
"""1331. Rank Transform of an Array.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eY07QIYpuBdAVvmyD075Chqi65kXMf-N

## 1331. Rank Transform of an Array

Easy

Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.

**Example 1:**

```
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
```

**Example 2:**

```
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

```

**Example 3:**

**Constraints:**

- `0 <= arr.length <= 105`
- `109 <= arr[i] <= 109`

## Solution

Given :

arr = […]

Rank of element starts from 1 . If elements are same rank same . Higher the element higher the rank.
"""



"""Approach :

Step 1: Sort the array

Step 2: Assign the rank

Step 3: Replace each element of the arr to its assigned rank as we need output an array which contains rank .
"""

########################  Solution #########################################
class Solution(object):
    def arrayRankTransform(self, arr):
        # Step 1
        sorted_arr = sorted(set(arr))

        # Step 2 we are using dictionary to map each element
        rank_dict = {num: rank +1 for rank, num in enumerate(sorted_arr)}

        # Step 3
        return [rank_dict[num] for num in arr]
