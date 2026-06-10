arr = [1,1,2,2,3]

left = 0

for right in range(1, len(arr)):

    if arr[right] != arr[left]:
        left += 1
        arr[left] = arr[right]

print(arr[:left+1])