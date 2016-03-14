class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        rotated90 = zip(*A[::-1])
        return rotated90


matr_= [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10,11,12]]

# s = Solution()
# rotated90 = s.rotate(matr_)

# print (matr_[::-1])
# print zip(*matr_[::-1])
# print zip(matr_[::-1])
print zip(*matr_)

# print (rotated90)