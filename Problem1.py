# Solving the five basic problems presented by Santiago L. Valdarrama on his blog:
# https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
# Resources used as reference:
# http://www.tutorialspoint.com/python/python_loops.htm
# http://interactivepython.org/courselib/static/pythonds/Recursion/recursionsimple.html

# Problem 1:
# Write three functions that compute the sum of the numbers in a given list
# using a for-loop, a while-loop, and recursion.

# List of numbers
numbers = [ 22, 6, 124, 1, 22, 14, 9, 88]

# Print the list
print (numbers)

# For-loop
numbertotal = 0
for number in numbers:
    numbertotal += number
print ("For-loop total:", numbertotal)

# While-loop
numbertotal = 0
counter = 0
while (counter < len(numbers)):
    numbertotal += numbers[counter]
    counter += 1
print ("While-loop total:", numbertotal)

# Recursion
def summer(numberlist):
    # If list is only one number long, no need for any summing!
    if len(numberlist) == 1:
        return numberlist[0]
    # Else do this shizzle
    else:
        return numberlist[0] + summer(numberlist[1:])
print("Recursion total:",summer(numbers))
