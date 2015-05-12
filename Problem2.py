# Solving the five basic problems presented by Santiago L. Valdarrama on his blog:
# https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
# Resources used as reference:
# http://www.tutorialspoint.com/python/python_functions.htm

# Problem 2:
# Write a function that combines two lists by alternatingly taking elements. For example:
# given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].

listone = [ "green", "brown", "blue", "yellow", "red" ]
listtwo = [ "cat", "dog", "dolphin", "sheep", "alpaca" ]

def listcombiner(listone, listtwo):
    "Combines two lists into one, alternatingly taking elements."
    counter = 0
    combinedlist = []
    while ( counter < len(listone) ):
        combinedlist.append(listone[counter])
        combinedlist.append(listtwo[counter])
        counter += 1
    return combinedlist

print(listcombiner(listone, listtwo))
