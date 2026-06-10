nums = [-1, 0, 1, 2, -1, -4]
target = 0

nums.sort()
k = []

for i in range(len(nums) - 2):

    # skip duplicate values
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:

        summ = nums[i] + nums[left] + nums[right]

        if summ == target:

            k.append([nums[i], nums[left], nums[right]])

            left += 1
            right -= 1

            # skip duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif summ < target:
            left += 1

        else:
            right -= 1

print(k)