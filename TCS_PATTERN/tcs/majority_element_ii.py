arr=[1, 1, 1, 3, 3, 2, 2, 2]

candidate1=None # 1
cabdidate2=None# 2
count1=0 # 1 
count2=0 # 1

for num in arr:
    if count1==0:
        candidate1=num
        count1=1
    elif num==candidate1:
        count1+=1
    elif count2==0:
        candidate2=num
        count2=1
    elif num==candidate2:
        count2+=1
    else:
        count1-=1
        count2-=1
        
print(candidate1,candidate2)
