# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

nums = [2, 7, 11, 15]
target = 9

#Brute Force O(n^2)

def twoSum(nums,target):
	for i in range(0,len(nums)):
		for j in range(i+1,len(nums)):
			if nums[i] + nums[j] is target:
				return [i,j]

print twoSum(nums,target)

#One-Pass Hash O(n)

def twoSum2(nums,target):
	h = {}
	for i in range(0,len(nums)):
		complement = target-nums[i]
		if complement in h:
			return [h[complement],i]
		h[nums[i]] = i

print twoSum2(nums,target)
