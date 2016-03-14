
def count_inc_subarray(A):

    inc_count = 1
    total = 0
    last_num = A[0]
    for i in range(1, len(A)):
        if(A[i] > last_num):
            inc_count += 1
            last_num = A[i]
        else:
            total += ((inc_count)*(inc_count-1)/2)
            last_num = A[i]
            inc_count = 1
    
    total += ((inc_count)*(inc_count-1)/2)

    return total

A = [1,2,7,3]

res = count_inc_subarray(A)
print (res)