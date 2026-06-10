Input = [2,0,2,1,1,0]

left = 0
right = len(Input) - 1
i = 0

while i <= right:

    if Input[i] == 0:
        Input[left], Input[i] = Input[i], Input[left]
        left += 1
        i += 1

    elif Input[i] == 1:
        i += 1

    else:
        Input[right], Input[i] = Input[i], Input[right]
        right -= 1

print(Input)