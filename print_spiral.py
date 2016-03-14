

def print_spiral(arr, M, N):

    count = 0;
    sr = 0;
    er = M-1;
    sc = 0;
    ec = N-1;
    
    print(M, N)
    while(count < M*N):
        for i in range(sc, ec+1):
            print arr[sr][i]
            count += 1
            if(count >= M*N):
                return
        for i in range(sr+1, er+1):
            print arr[i][ec]
            count += 1
            if(count >= M*N):
                return
        for i in range(ec-1, sc-1, -1):
            print arr[er][i]
            count += 1
            if(count >= M*N):
                return
        for i in range(er-1, sr, -1):
            print arr[i][sc]
            count += 1
            if(count >= M*N):
                return

        sr = sr + 1
        sc = sc + 1
        er = er - 1
        ec = ec - 1


arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]
      ]


print_spiral(arr, len(arr), len(arr[0]))