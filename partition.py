def sums(target, summands):
     if summands == 1:
         return 1
     else:
         return sum(sums(target-i, summands-1) for i in range(target+1))

def my_comb(total, segment):
	if(segment == 1):
		return 1
	else:
		res = 0
		for i in range(total+1):
			res += my_comb(total - i, segment-1)
		return res

print(sums(20,4))
print(my_comb(20,4))
print(my_comb(1,4))