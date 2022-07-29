class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
            #This is when we can't divide the list in two equal halves
        ss=set()
        ss.add(0) #Base case 
        target=sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            metass=set()
            for t in ss:
                metass.add(t+nums[i])
                metass.add(t)
            ss = metass
        return True if target in ss else False
