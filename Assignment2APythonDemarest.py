

for num in xrange(1,150):
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print "FizzBuzzWoof"
    elif num % 3 == 0 and num % 5 == 0:
        print "FizzBuzz"
    elif num % 5 == 0 and num % 7 == 0:
        print "BuzzWoof"        
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    elif num % 7 == 0:
        print "Buzz"    
    else:
        print num