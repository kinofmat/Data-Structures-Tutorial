"""
Kai Matkin

I've included this file so you can run the example code I used throughout
the tutorial. Not all of it is the best, so just be prepared for a lot of
outputs. 
"""

#This is the example code from the discussion on Stacks
n = 50
m = 100
cd1 = 20
cd2 = 57
for c in range(n):
    if c == cd1 or c == cd2:
        print("You found it!", c)
for d in range(n, m):
    if d == cd1 or d == cd2:
        print("You found it!", d)

cd_case = []
for i in range(100):
    cd_case.append(i)
for cd in cd_case:
    for second in cd_case:
        burned_disc = cd + second
        #This if statement is solely for if you decide to run the code.
        if second//5 == 0:
            print(burned_disc)

print("")

#Here we initialize with escaped chickens
escaped_chickens = []
for i in range(4):
    escaped_chickens.append(i)

#More chickens escaped
escaped_chickens.append(4)
escaped_chickens.append(5)

#Gotta catch them all! Chickens!
for c in range(7):
    if len(escaped_chickens) > 0:
        chicken = escaped_chickens.pop()
        print("Congrats, you caught chicken number", chicken)
    else:
        print("You caught all of the chickens! Good job!")

print("\n")

#This is code from the discussion on Sets
graph1 = []
graph2 = []
for i in range(-5, 6):
    graph1.append("({},{})".format(i, i))
for i in range(-4, 1):
    graph2.append("({},{})".format(2*i+2, i))

intersect = set()
for i in graph1:
    intersect.add(i)
"""for i in graph2:
    intersect.add(i)
for i in intersect:
    print(i)"""
for i in graph2:
    if i in intersect:
        print("\nThe intersect of the two graphs are:", i)
    else:
        intersect.add(i)

print("\n")

#This is code from the discussion on Trees
def recursion(numbers):
    if numbers <= 0:
        print("This is a base case")
    else:
        print("This is the", 10-numbers , "recursive call")
        recursion(numbers-1)

recursion(10)

def memoization(num, dictionary = None):
    if dictionary is None:
        dictionary = dict()
    if num <= 1:
        return 1
    # If you were to remove this if statement, it would take a long time to calculate
    if num in dictionary:
        return dictionary[num] 
    
    calc = (memoization(num-1, dictionary))^num + (memoization(num-1, dictionary))^(num-1)
    dictionary[num] = calc
    return calc

print(memoization(100))