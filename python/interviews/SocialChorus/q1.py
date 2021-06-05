def tuple_slice(startIndex, endIndex, tup):
    return ','.join(str(num) for num in tup[startIndex:endIndex]) 

print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))