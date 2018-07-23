#三个无重叠子数组的最大和
'''
给定数组 nums 由正整数组成，找到三个互不重叠的子数组的最大和。

每个子数组的长度为k，我们要使这3*k个项的和最大化。

返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。

示例:

输入: [1,2,1,2,6,7,5,1], 2
输出: [0, 3, 5]
解释: 子数组 [1, 2], [2, 6], [7, 5] 对应的起始索引为 [0, 3, 5]。
我们也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
'''


'''
解题思路：
区域可被划分为三部分，假设A被划分为了A_sub1,A_sub2,A_sub3.我们令len(A_sub2)的长度为k，滑动该窗口，计算三部分的最大值，只需一次遍历。
'''
#动态规划

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_ = 0
        out = []
        for i in range(k, len(nums) - 2 * k + 1):
            windows = [i, i + k]
            idx0, max0 = self.find_max(nums, 0, i, k)
            max1 = sum(nums[i:i + k])
            idx1 = i
            idx2, max2 = self.find_max(nums, i + k, len(nums), k)
            if max0 + max1 + max2 > max_:
                out = [idx0, idx1, idx2]
                max_ = max0 + max1 + max2
        return out

    def find_max(self, s, i, j, k):
        max_ = 0
        idx = i
        # print(i,j)
        for ii in range(i, j - k + 1):
            tmp = sum(s[ii:ii + k])
            if tmp > max_:
                max_ = tmp
                idx = ii
            # print(s[ii])
        return idx, max_


A=[4,5,10,6,11,17,4,11,1,3]
k=1
s=Solution()
print(s.maxSumOfThreeSubarrays(A,k))


