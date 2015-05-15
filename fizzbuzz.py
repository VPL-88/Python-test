# Fizzbuzz implementation, just a simple test
# Print numbers 1-100, for a multiple of three print "Fizz" instead of the number.
# For a multiple of five print "Buzz" instead. For multiples of both 3 and 5 print "FizzBuzz"

for number in range ( 1, 101 ):
    if ( number % 3 == 0 and number % 5 != 0):
        print("Fizz")
    if ( number % 5 == 0 and number % 3 != 0):
        print("Buzz")
    if ( number % 5 == 0 and number % 3 == 0):
        print("FizzBuzz")
    else:
        print(number)
