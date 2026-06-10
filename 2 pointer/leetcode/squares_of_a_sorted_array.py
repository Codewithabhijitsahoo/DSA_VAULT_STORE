Input:  [-4,-1,0,3,10]
Output: [0,1,9,16,100]

arr=[-4,-1,0,3,10]
sorted_array=[0]*len(arr)


left=0
right=len(arr)-1
k=len(sorted_array)-1
while left<right :

  if abs(arr[left]**2)< abs (arr[right]**2):
    sorted_array[k]=abs(arr[right]**2)
    right-=1
    k-=1

  else:
    sorted_array[k]=abs(arr[left]**2)
    left+=1
    k-=1


  
or 

arr = [-4, -1,5, 10]
if len(arr)%2==0:
    l=(len(arr)//2)-1
else:
    l=(len(arr)//2)-1
    
sorted_array=[arr[l]**2]*len(arr)


left=0
right=len(arr)-1
k=len(sorted_array)-1
while left <+ right :
    
    if abs(arr[left])< abs(arr[right]):
        sorted_array[k]=abs(arr[right]**2)
        k-=1
        right-=1
    else:
        sorted_array[k]=abs(arr[left]**2)
        k-=1
        left+=1
print(sorted_array)
