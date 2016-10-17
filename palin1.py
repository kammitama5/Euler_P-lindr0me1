def Reverse():
	for  x in xrange(1, 999999):
		 temp = x;
		 ##figure out how to reverse dummy
		 reversenum = int(str(temp)[::-1]);
		 if temp == reversenum:
			print temp;
	
Reverse();