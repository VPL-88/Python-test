# Solving the five basic problems presented by Santiago L. Valdarrama on his blog:
# https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

# Problem 3: Write a function that computes the list of the first 100 Fibonacci numbers.
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each
# subsequent number is the sum of the previous two. As an example, here are the first 10
# Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

numbers = [ 0, 1 ]
for x in range(2,103):
    numbers.append(numbers[x-1] + numbers[x-2])
print (numbers)
