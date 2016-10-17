def Reverse():
	# since we are looking for 3 digit products, smallest palindrome 
	# we are interested in has to be within range of multiple
	# of smallest three digit numbers
	
	for  x in xrange(10000, 999999):
		 temp = x;
		 ##figure out how to reverse dummy
		 reversenum = int(str(temp)[::-1]);
		 if temp == reversenum:
			print temp;
	
Reverse();