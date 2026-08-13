def capitalizer(arr):

    result = []
    if len(arr) == 0:
        return result   
    
    result.append(arr[0].upper()) + arr[0][1:]
    return result + capitalizer(arr[1:])

print(capitalizer(['car', 'banana', 'taco']))