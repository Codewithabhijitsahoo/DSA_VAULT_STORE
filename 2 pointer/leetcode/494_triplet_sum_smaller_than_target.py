nums = [-1,2,1,-4]
target = 1

nums.sort()

closest = float('-inf')

for i in range(len(nums)-2):

    left = i + 1
    right = len(nums) - 1

    while left < right:

        sum_ = nums[i] + nums[left] + nums[right]

        if sum_ < target and sum_ > closest:
            closest = sum_

        if sum_ < target:
            left += 1
        else:
            right -= 1

print(closest)