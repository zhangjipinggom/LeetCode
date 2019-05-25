1. 问题在于如何自己实现排序，并且在排序的过程中不要加入相等的元素。

2. 解法1用自带的函数，相当于作弊了

3. 用三个值依次来记录第一大，第二大，第三大的值，且对于困难的初始化问题，机智地将他们初始化为None,
后面地判断条件也就方便多了


4. 假如把题目中的3变成任意一个[0, n-1]的值K,则代码可以改为：
class Solution(object):
    def KthMaximum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxs_k = [None for i in range(k)]
        for num in nums:
            if num in maxs_k:
                    continue
            for i, max_k in enumerate(maxs_k):
                if max_k is None or num > max_k:
                    for j in range(k-1, i, -1):
                        maxs_k[j] = maxs_k[j-1]
                    maxs_k[i] = num
                    break
        return maxs_k[-1]

