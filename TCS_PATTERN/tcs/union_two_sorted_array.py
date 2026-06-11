arr1 = [1, 1, 2, 3, 4]
arr2 = [2, 2, 4, 5, 6]

sorted_array = [0] * 10
i = 0
j = 0
k = 0
list = []

while i < len(arr1) and j < len(arr2):

    if arr1[i] < arr2[j] and arr1[i] not in list:

        sorted_array[k] = arr1[i]
        list.append(arr1[i])
        i += 1
        k += 1

    elif arr1[i] > arr2[j] and arr2[j] not in list:

        sorted_array[k] = arr2[j]
        list.append(arr2[j])
        j += 1
        k += 1

    else:
        if arr1[i] not in list:
            sorted_array[k]=arr1[i]
            list.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr2[j] not in list:
            sorted_array[k]=arr2[j]
            list.append(arr2[j])
            j+=1
            k+=1
            i+=1
        else:
            i+=1
            j+=1
            
while i < len(arr1):
    if arr1[i] not in list:
        sorted_array[k]=arr1[i]
        list.append(arr1[i])
        k+=1
    i+=1
    
while j < len(arr2):
    if arr2[j] not in list:
        sorted_array[k]=arr2[j]
        list.append(arr2[j])
        k+=1
    j+=1
print(sorted_array[:k])