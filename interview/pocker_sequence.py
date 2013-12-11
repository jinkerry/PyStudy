#pocker in 'spade, heart, club, diamond', and '1(A),2,3,4,5,6,7,8,9,10,11(J),12(Q),13(K)'

max_seq = [1,10,11,12,13]
min_seq = [1,2,3,4,5]

def pocker_sequence(suits, numbers):
	#drop duplicate suit
	suit = list(set(suits)) 
	if len(suit) > 1:
		print 'not same suit', suits
	else:
		numbers.sort()
		if numbers == max_seq or numbers == min_seq:
			print 'same suit sequence:', suits[0], numbers
		else:	
			num = len(numbers) - 1
			count = 0
			for i in range(0, num):
				if abs(numbers[i] - numbers[i+1]) <> 1:
					print 'not sequence', numbers
				else:
					count = count + 1
					continue
			#normal exit loop		
			if count == num:
				print 'same suit sequence:', suits[0], numbers	

if __name__ == '__main__':
	suits = ['red', 'red', 'red', 'red', 'red']
	numbers = [10,11,12,13,1]
	pocker_sequence(suits, numbers)
