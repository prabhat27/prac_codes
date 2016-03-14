class Solution:
    # @param A : integer
    # @return a list of list of integers
    def create_spiral_array(self, M, N):
        count = 0;
        sr = 0;
        er = M-1;
        sc = 0;
        ec = N-1;
        # new_array = []
        new_array = [[0 for i in range(M)] for j in range(N)]
        
        while(count < M*N):
            for i in range(sc, ec+1):
                new_array[sr][i] = count + 1
                count += 1
                if(count >= M*N):
                    return new_array
            for i in range(sr+1, er+1):
                new_array[i][ec] = count + 1
                count += 1
                if(count >= M*N):
                    return new_array
            for i in range(ec-1, sc-1, -1):
                new_array[er][i] = count + 1
                count += 1
                if(count >= M*N):
                    return new_array
            for i in range(er-1, sr, -1):
                new_array[i][sc] = count + 1
                count += 1
                if(count >= M*N):
                    return new_array
    
            sr = sr + 1
            sc = sc + 1
            er = er - 1
            ec = ec - 1
        return new_array
        
    def generateMatrix(self, A):
        
        res_2d_arr = self.create_spiral_array(A, A)
        
        return res_2d_arr
