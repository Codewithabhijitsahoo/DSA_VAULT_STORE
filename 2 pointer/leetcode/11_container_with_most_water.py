height = [1,8,6,2,5,4,8,3,7]

left=0
area=1
right=len(height)-1
while left < right:
  width=right - left
  h=min(height[left],height[right])

  area=max(area,width*h)

  if heigt[left]<height[right]:
    left+=1
  else:
    right-=1