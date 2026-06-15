arr=str(1241)

left=0

right=len(arr)-1
bool=True
while left< right :
  if arr[left]!=arr[right]:
 
    bool=False
    break

  left+=1
  right-=1
if bool==True:
    print('palin')
else:
    print("not palin")