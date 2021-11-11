import random

# Michael Moreland - Smoothstack, Python basics 3; 11/11/2021

# Part 1
print("\nPart 1")

def divBy7And5():
    r = range(1500, 2701)
    results = []
    for n in r:
        if n % 7 == 0:
            if n % 5 == 0:
                results.append(n)
    return results

print(divBy7And5())

# Part 2: Write a Python program to convert temperatures to and from celsius, fahrenheit.
print("\nPart 2")
def convertToFahrenheit(num):
    return num*(9/5)+32
def convertToCelsius(num):
    return (num-32)*(5/9)
print(f"60 Celsius is {int(convertToFahrenheit(60))} in Fahrenheit")
print(f"45 Fahrenheit is {int(convertToCelsius(45))} in Celsius")

# Part 3: Write a Python program to guess a number between 1 to 9. 
print("\nPart 3")
correct = random.randrange(1, 10)
userGuess = int(input("Guess a number between 1 - 9: "))
if(userGuess == correct):
    print("Correct! Good guess!")
else:
    print(f"Incorrect guess. Correct answer was {correct}")

# Part 4: Write a Python program to construct the following pattern, using a nested for loop.
print("\nPart 4")
i = 1
for y in range(1, 10):
    for x in range(1, i+1):
        print("*", end='')
    print()
    i += 1
    if(y >= 5):
        i -= 2

# Part 5: Write a Python program that accepts a word from the user and reverse it. 
print("\nPart 5")
word = input("Enter a string to be reversed: ")
print(word[::-1])

# Part 6: Write a Python program to count the number of even and odd numbers from a series of numbers 
print("\nPart 6")
userNums = [ int(i) for i in input("Enter a list of numbers separated by a comma: ").split(',') ]
evens = 0
odds = 0
for x in userNums:
    if(x % 2 == 0):
        evens += 1
    else:
        odds += 1
print(f"{userNums}\nAmount of evens: {evens}\nAmount of odds: {odds}")

# Part 7: Write a Python program that prints each item and its corresponding type from the following list.
print("\nPart 7")
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
print(f"From the provided list {datalist}")
for dl in datalist:
    print(f"{dl} is type {type(dl)}")

# Part 8: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement.
print("\nPart 8")
for x in range(0,7):
    if(x == 3 or x == 6):
        continue
    else:
        print(x)