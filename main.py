init = [6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4 , -5, -6]

def move(n, arr):
    index = -1
    for i in range(0, len(arr)):
        if i == arr[i]:
            index = i
            break
    if index == -1:
        raise ValueError("Number must be in range.")
        
    direction = 0
    if arr[index] > 0:
        direction = 1
    elif arr[index] < 0:
        direction = -1
    
