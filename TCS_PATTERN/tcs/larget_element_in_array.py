arr = [10, 5, 20, 8, 15]

larget=0

for right in range(len(arr)):
    if arr[right]>larget:
        larget=arr[right]
        
print(larget)