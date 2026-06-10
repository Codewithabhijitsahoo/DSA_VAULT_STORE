nums = [-1,2,1,-4]
target = 1

nums.sort()

closest = nums[0] + nums[1] + nums[2]

for i in range(len(nums)-2):

    left = i + 1
    right = len(nums) - 1

    while left < right:

        sum_ = nums[i] + nums[left] + nums[right]

        # update closest
        if abs(target - sum_) < abs(target - closest):
            closest = sum_

        # move pointers
        if sum_ < target:
            left += 1
        else:
            right -= 1

print(closest)