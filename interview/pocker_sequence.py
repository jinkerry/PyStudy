#pocker in 'spade, heart, club, diamond, joke', and '0(joke),1(A),2,3,4,5,6,7,8,9,10,11(J),12(Q),13(K)'

max_seq = [1,10,11,12,13]
min_seq = [1,2,3,4,5]

def pocker_sequence(suits, numbers):
	#drop duplicate suit
	suit = list(set(suits)) 
	if len(suit) > 2:
		print 'not same suit sequence', suits
	elif len(suit) == 2 and suit.index('joke') == -1:
		print 'not same suit sequence', suits
	else:
		numbers.sort()
		if numbers == max_seq or numbers == min_seq:
			print 'same suit sequence:', suits[0], numbers
		else:
			#has a joke, or two jokes
			start = 0
			if numbers[0] == 0:
				start = start + 1
			if numbers[1] == 0:
				start = start + 1
			num = len(numbers) - 1
			sum = 0
			for i in range(start, num):
				diff = numbers[i+1] - numbers[i] - 1
				#if has joke, and first is A
				if (numbers[i] == 1) and (diff >= 8):
					diff = diff - 8
				sum = sum + diff
			#normal exit loop, jokes more euqal than sum of diff		
			if start >= sum:
				print 'same suit sequence:', suits[0], numbers
			else:
				print 'not same suit sequence:', suits[0], numbers		

if __name__ == '__main__':
	suits = ['heart', 'heart', 'heart', 'joke', 'joke']
	numbers = [1,11,13,0,0]
	pocker_sequence(suits, numbers)
