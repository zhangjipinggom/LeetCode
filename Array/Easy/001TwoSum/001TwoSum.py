class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        searched = {}
        for index, num in enumerate(nums):
            flag = searched.get(target-num)
            if flag is not None:
                return [searched.get(target-num), index]
            searched[num] = index
