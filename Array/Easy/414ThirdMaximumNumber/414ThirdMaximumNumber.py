class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sort = sorted(list(set(nums)))
        if len(nums_sort) > 2:
            return nums_sort[-3]
        else:
            return nums_sort[-1]

    def thirdMax2(self, nums):
        max1, max2, max3 = None, None, None
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            elif max1 is None or num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 is None or num > max2:
                max3 = max2
                max2 = num
            elif max3 is None or num > max3:
                max3 = num
        return max3 if max3 is not None else max1
