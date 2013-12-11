def ab_count(str):
	result = []
	length = len(s)
	for i in range(0, length):
		#print str[i], str.count(str[i]), str.index(str[i])
		temp = str[i], str.count(str[i]), str.index(str[i])
		#print temp
		result.append(temp)	

	res = list(set(result))
	res.sort(key = result.index)
	print res

if __name__ == '__main__':
	s = 'abcdaabcffg'
	print 'char count index'
	ab_count(s)
