arr = [-10, -5, -20, -8]

larget=arr[0]
second_laregt=float('-inf')
for right in range(len(arr)):
    if arr[right]>larget:
        larget=arr[right]
        
for right in range(len(arr)):
    if second_laregt<= arr[right] < larget :
        second_laregt=arr[right]
        
print(larget)
print(second_laregt)
        