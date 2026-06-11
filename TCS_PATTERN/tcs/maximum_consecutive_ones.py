arr = [1, 1, 0,0,0,0,0 ,0, 1, 1, 1, 1]

left = 0
lengthh = 0

for right in range(len(arr)):
    if arr[right] == 0:
        left = right + 1

    lengthh = max(lengthh, right - left + 1)

print(lengthh)