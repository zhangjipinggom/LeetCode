class Solution(object):
    def findPairs(self, nums, k):
        """时间复杂度过高O(n**2),而且写得又长又臭
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        left, right = 0, len(nums)-1
        k_diff_num = 0
        searched = set()
        while left < right:
            for right in range(left+1, len(nums), 1):
                diff = nums[left] - nums[right]
                if diff == k or -diff == k:
                    if (nums[left], nums[right]) in searched or (nums[right], nums[left]) in searched:
                        continue
                    else:
                        k_diff_num += 1
                        searched.add((nums[left], nums[right]))
            left += 1
        return k_diff_num

    def findPairs2(self, nums, k):
        """这个判断者的很巧妙啊
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        result, lookup = set(), set()
        for num in nums:
            if num - k in lookup:
                result.add(num - k)
            if num + k in lookup:
                result.add(num)
            lookup.add(num)
        return len(result)


s = Solution()
a = s.findPairs([3,1,4,1,5], 2)
print(a)