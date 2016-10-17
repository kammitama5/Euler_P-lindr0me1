from math import sqrt


def Reverse():
    # since we are looking for 3 digit products, smallest palindrome
    # we are interested in has to be within range of multiple
    # of smallest three digit numbers

    for x in xrange(100000, 999999):
        temp = x;
        # reverse
        reversenum = int(str(temp)[::-1]);
        if temp == reversenum:
            print temp;
            # find product of 2 two digit numbers
            factors = set()
            for w in range(1, int(sqrt(temp)) + 1):
                if temp % w == 0:
                    factors.add(w)
                    factors.add(temp // w)
                    if sorted(factors) > 950:
                        print sorted(factors);


Reverse();

#I hacked my way through this one, but got it right: 906609