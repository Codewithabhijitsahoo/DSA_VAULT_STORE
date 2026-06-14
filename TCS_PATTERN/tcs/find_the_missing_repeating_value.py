arr = [3,1,2,5,3]
n=len(arr)

has_array=[0]*(n+1)



for right in arr:
    has_array[right]+=1
    

for right in range(1,n+1):
    
    if has_array[right]==0:
        missing=right
    elif has_array[right]==2:
        repeating=right
        
        
print(missing,repeating)
