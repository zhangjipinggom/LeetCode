class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxs_k = [None for i in range(len(nums))]
        for num in nums:
            for i, max_k in enumerate(maxs_k):
                if max_k is None or num >= max_k:
                    for j in range(k - 1, i, -1):
                        maxs_k[j] = maxs_k[j - 1]
                    maxs_k[i] = num
                    break
        return maxs_k[k - 1]

