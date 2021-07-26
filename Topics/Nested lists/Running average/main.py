nums = [int(x) for x in input()]
print([(nums[i] + nums[i + 1]) / 2 for i in range(len(nums) - 1)])
