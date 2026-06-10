arr = [1,0,1,0,1,0,0,1]
left=0

i=0

while i < len(arr)-1:
  if arr[i]==0:

    arr[left],arr[i]=arr[i],arr[left]
    left+=1
    i+=1
  else:
    i+=1