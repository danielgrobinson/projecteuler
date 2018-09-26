# These are solutions and notes for problems 001 - 050

# Problem 001 

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Solution

My first attempt at this problem was to do a simple oount of numbers divisible by 3 adnd 5.
	for(ii = 0; ii < 1000; ii++) {
		if((ii % 3) == 0) sum++;
		else if((ii % 5) == 0) sum++;
	}

This is an O(n) solution.  Is there a O(1) solution?

The sum of integers from 1 -> n is (n * (n - 1)) / 2.

The sulution is to divide n by the divisors, 3 and 5 and find that sum, e.g., 

	ll = 1000/3;
	sum = ll * (ll -1) / 2;
	
	ll = 1000/5;
	sum += (ll * (ll -1) / 2);

Since those numbers have some duplicates, we need to remove one of them, e.g.,

	  11 = 1000/15
	  sum -= (ll * (ll -1) /  2);

