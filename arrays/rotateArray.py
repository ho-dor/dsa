class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range((n - k)%n):
            ele = nums.pop(0)
            nums.append(ele)