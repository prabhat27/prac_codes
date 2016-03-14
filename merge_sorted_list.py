def correctify(B):
    
    count = 0
    while(count < len(B) -1):
        if(B[count] > B[count + 1]):
            t = B[count+1]
            B[count+1] = B[count]
            B[count] = t
        count += 1
    
    return B

def merge_list(A, B):
    # print (len(A))

    idx1 = 0
    while(idx1 < len(A)):
        if(A[idx1] > B[0]):
            t = A[idx1]
            A[idx1] = B[0]
            B[0] = t
            B = correctify(B)
        idx1 += 1
    
    merged = A + B

    return merged


# A = [4,1,2,3]
# res = correctify(A)
res = merge_list([1,3,7,9,11], [2,4,5,13])
print (res)
