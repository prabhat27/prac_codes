
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        numbers = [None, None, None]
        counts = [0, 0, 0]
        # print len(A)
        # counter=collections.Counter(A)
        # print (counter)

        for i in range(0, len(A)):
            
            if(numbers[0] == A[i]):
                counts[0] += 1

            elif(counts[0] == 0):
                numbers[0] = A[i]
                counts[0] = 1

            elif(numbers[1] == A[i]):
                counts[1] += 1

            elif(counts[1] == 0):
                numbers[1] = A[i]
                counts[1] = 1

            elif(numbers[2] == A[i]):
                counts[2] += 1

            elif(counts[2] == 0):
                numbers[2] = A[i]
                counts[2] = 1

            else:
                counts[0] = counts[0] - 1
                counts[1] = counts[1] - 1
                counts[2] = counts[2] - 1

            # print A[i]
            # print numbers
            # print counts
            # print "--------------------"
        count1 = count2 = count3 = 0
        # print (count1,count2)
        # print (numbers[0], numbers[1])
        for each in A:
           if each == numbers[0]:
               count1 += 1
           elif each == numbers[1]:
               count2 += 1
           elif each == numbers[1]:
               count3 += 1
        
        # print (count1, count2)        
        if count1 > len(A)/3:
            return numbers[0]
            
        if count2 > len(A)/3:
            return numbers[1]
        
        return -1

test = Solution()

A = (1000727, 1000727, 1000641, 1000517, 1000212, 1000532, 1000727, 1001000, 1000254, 1000106, 1000405, 1000100, 1000736, 1000727, 1000727, 1000787, 1000105, 1000713, 1000727, 1000333, 1000069, 1000727, 1000877, 1000222, 1000727, 1000505, 1000641, 1000533, 1000727, 1000727, 1000727, 1000508, 1000475, 1000727, 1000573, 1000727, 1000618, 1000727, 1000309, 1000486, 1000792, 1000727, 1000727, 1000426, 1000547, 1000727, 1000972, 1000575, 1000303, 1000727, 1000533, 1000669, 1000489, 1000727, 1000329, 1000727, 1000050, 1000209, 1000109)
# A = (1,1,3,4,2)
res = test.repeatedNumber(A)

print (res)