class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(numbers) - 1
        while start != end:
            sumed = numbers[start] + numbers[end]
            if sumed < target:
                start += 1
            elif sumed > target:
                end -= 1
            else:
                return start + 1, end + 1
