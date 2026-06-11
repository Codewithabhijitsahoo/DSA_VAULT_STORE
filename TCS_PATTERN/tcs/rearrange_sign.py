arr = [3, 1, -2, -5, 2, -4,-6]

sign_array=[]
find=[]
k=0
boolean= True 
while k < len(arr):
    
    # search +ve num
    if boolean==True:
        for right in range(len(arr)):
            if arr[right]>0 and arr[right] != 0:
                sign_array.append(arr[right])
                arr[right]=0
                boolean=False
                break
        
            
            
    elif boolean==False :
        for right in range(len(arr)):
            if arr[right]<0 and arr[right] !=0:
                sign_array.append(arr[right])
                arr[right]=0
                boolean=True
                break
            
    
    else :
        if boolean==True:
            for right in range(len(arr)):
                if arr[right] !=0:
                    sign_array.append(arr[right])
            break
        else:
            for right in range(len(arr)):
                if arr[right] != 0:
                    sign_array.append(arr[right])
                
                
    k+=1
print(sign_array)