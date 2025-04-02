class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = [0]*n
        right = [0]*n
        #left
        left[0] = nums[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])
        print (left)
        
        #right
        right[n - 1] = nums[n - 1]
        for j in range(n - 2, -1, -1):
            right[j] = max(right[j+1], nums[j])
        print (right)

        maxim = 0
        for k in range(1, n - 1):
            value = (left[k - 1] - nums[k]) * right[k + 1]
            maxim = max(maxim,value)

        print (maxim)

obj = Solution()
nums = [12,6,1,2,7]
obj.maximumTripletValue(nums)