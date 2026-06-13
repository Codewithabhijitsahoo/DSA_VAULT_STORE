arr = [16, 17, 4, 3, 5, 2]

leader=[2]

tillleader=arr[-1]

for right in range(len(arr)-2,-1,-1):
    if arr[right]>=tillleader:
        tillleader=arr[right]
        leader.append(tillleader)
  
print(arr[::-1])
        