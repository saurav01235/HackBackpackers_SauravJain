def BitCompress(binary: str):
    le = len(binary)
    sum = 0
    index=0
    for i in range(le-1,-1, -1):
        sum = sum + int(binary[i]) * 2**index
        index = index+1
    return sum


