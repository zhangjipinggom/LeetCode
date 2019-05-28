class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = [None for _ in range(len(nums))]        # 最终从达到小排列
        for num in nums:
            for i, max_k in enumerate(sorted_nums):
                if max_k is None or num >= max_k:
                    for j in range(k - 1, i, -1):
                        sorted_nums[j] = sorted_nums[j - 1]
                    sorted_nums[i] = num
                    break
        return sorted_nums[k - 1]

    def findKthLargest11(self, nums, k):
        """
        第一种方法的改进，在修改list的时候用insert和pop组合的方式，而不是用循环遍历的方式
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = [None for _ in range(len(nums))]        # 最终从大到小排列
        for num in nums:
            for i, max_k in enumerate(sorted_nums):
                if max_k is None or num >= max_k:
                    sorted_nums.insert(i, num)
                    sorted_nums.pop(-1)
                    break
        return sorted_nums[k - 1]

    def findKthLargest2(self, nums, k):
        """基于优先队列
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxs_k = []
        for i, num in enumerate(nums):
            maxs_k_length = len(maxs_k)
            if maxs_k_length < 1:
                maxs_k.append(num)
            elif maxs_k_length < k:
                for j in range(maxs_k_length-1, -1, -1):
                    max_k = maxs_k[j]
                    if num >= max_k:
                        maxs_k.insert(j+1, num)
                        break
                    if j == 0:
                        maxs_k.insert(0, num)
            else:
                for j in range(maxs_k_length-1, -1, -1):
                    max_k = maxs_k[j]
                    if num >= max_k:
                        maxs_k.insert(j + 1, num)
                        maxs_k.pop(0)
                        break
        return maxs_k[0]

    def findKthLargest3(self, nums, k):
        """基于快速排序
        :type nums: List[int]
        :type k: int
        :rtype: int
        其实这样做会加大难度，尤其在判断顺序的时候"""
        left, right = 0, len(nums)-1
        k_target = len(nums)-k
        while left < right:   # 类似于二分法，不断逼近那个区间
            pivot_index = self.partition(nums, left, right)
            if pivot_index == k_target:
                return nums[pivot_index]
            if pivot_index < k_target:
                left = pivot_index+1
            else:
                right = pivot_index-1

    def swap(self, nums, m, n):
        tmp = nums[m]
        nums[m] = nums[n]
        nums[n] = tmp

    def partition(self, nums, left, right):
        pivot_index_pre = left-1    # 这个值标记的是比pivot小的值得分界点的index
        for i in range(left, right):
            if nums[i] <= nums[right]:    # 小于等于会有区别吗？
                pivot_index_pre += 1      # 这个值是比pivot大的的index
                self.swap(nums, pivot_index_pre, i)
        pivot_index_pre += 1
        self.swap(nums, pivot_index_pre, right)      # 最后再把pivot移到它改在的位置
        return pivot_index_pre

    # 这是更骚的，导入了不明所以的库，这个之后再学习吧
    def findKthLargest4(self, nums, k):
        import heapq
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def quicksort(self, nums, left, right):
        # 真的是要递归，递归前半段和后半段
        if left <= right:      # 这里的等于只会影响len(nums)=1的时候吗，这里又用到了递归
            pivot_index = self.partition(nums, left, right)
            self.quicksort(nums, left, pivot_index-1)
            self.quicksort(nums, pivot_index+1, right)
        return nums




s = Solution()
mylist = [3,2,3,1,2,4,5,5,6]
# a = s.findKthLargest3([3,2,3,1,2,4,5,5,6], 4)
b = s.quicksort(mylist, 0, len(mylist)-1)
print(b)