def findIntoArray(array:list, value:int):
    s = 0
    e = len(array)
    
    while True:
        middle = int((e-s)/2) + s
        if value == array[middle]:
            return int(middle)
        elif value < array[middle]:
            e = middle
        else:
            s = middle
    
# 
l = [9, 18, 18, 19, 29, 42, 56, 61, 88, 95]


print(findIntoArray(l, 61))