def sum_digits(n):
    s = 0 				#result variable, starts at 0
    while n:			#until n reaches 0
        s += n % 10		#take the last digit of n with modulo and add it to s
        n //= 10		#get rid of the last digit of n with floor division
    return s			#and we're done