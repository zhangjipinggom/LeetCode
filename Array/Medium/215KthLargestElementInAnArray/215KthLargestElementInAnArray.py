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

    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxs_k = []
        for i, num in enumerate(nums):
            if len(maxs_k) < 1:
                maxs_k.append(num)
            elif len(maxs_k) < k:
                for j, max_k in enumerate(maxs_k):
                    if num >= max_k:
                        maxs_k.insert(j+1, num)
                        break
                if j == len(maxs_k):
                    maxs_k.insert(0, num)
            else:
                for j, max_k in enumerate(maxs_k):
                    if num >= max_k:
                        maxs_k.insert(j + 1, num)
                        maxs_k.pop(0)
                        break
                if j == len(maxs_k):
                    maxs_k.insert(0, num)
                    maxs_k.pop(0)
        return maxs_k[-1]

