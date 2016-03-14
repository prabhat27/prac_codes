

def index_longest_one(arr):
    temp_arr = []
    temp_len = 0
    zero_idx = []
    for i in range(len(arr)):
        if(arr[i] == 0):
            temp_arr.append(temp_len)
            zero_idx.append(i)
            temp_len = 0
        else:
            temp_len += 1
    temp_arr.append(temp_len)
    print (temp_arr)
    print (zero_idx)
    
    res_idx = -1
    res_len = 0

    for i in range(len(zero_idx)):
        # print(temp_arr[i] + temp_arr[i+1])
        # print (res_len)
        if((temp_arr[i] + temp_arr[i+1]) > res_len):
            res_idx = zero_idx[i]
            res_len = temp_arr[i] + temp_arr[i+1]

    return res_idx

arr = [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,0]
print (index_longest_one(arr))
