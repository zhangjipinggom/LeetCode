class Solution:
    def checkPossibility(self, nums):
        decrease_num = 0  # 记录不满足条件的次数
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                decrease_num += 1
                if decrease_num > 1:
                    return False
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return True
