def countIntegers(n, val, arr) -> list:
    """_summary_

    Args:
        n (int): _description_
        val1 (1): _description_
        arr (list): _description_

    Raises:
        RuntimeError: _description_

    Returns:
        list: _description_
    """
    resp = [0,0,0]
    
    for x in arr:
        if x < val: 
            resp[0] += 1
        elif x == val: 
            resp[1] += 1
        elif x > val: 
            resp[2] += 1
        else: raise RuntimeError("¿¿¿¿????")
    
    return resp

def countIntegers(n, val, arr) -> list:
    return []

n = int(input())
val = int(input())
# space separated numbers
arr = list(map(int, input().split()))

# [smaller, equal, greater]
response = [2,1,2]

result = countIntegers(n, val, arr)
print(' '.join(map(str, result)))
