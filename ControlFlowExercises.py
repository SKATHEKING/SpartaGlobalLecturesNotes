import math
print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print("\nQ1aansrs\n")
def return_five():
    print(x[0:5])

return_five()

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

def print_even():
    for i in x :
        if i % 2 == 0 :
            print(i)

print_even()



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
def samething_combined():
    for i in x[0:5] :
        if i % 2 == 0 :
            print(i)
samething_combined()

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

def print_ting():
    list =  []
    list = [item[0] for item in names]
    print(list)

print_ting()


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

def index_ting():
    list = []

    for i in names:
        list.append(i.index(' '))

    print(list)
index_ting()

#


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

list =  []
list = [item[0] for item in names]
print(list)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:




# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
def guessing_game():
    number = int(input('Enter a number please'))
    while number < 100:
        number = int(input('Enter a number please'))
        if number > 100:
            print(number)

guessing_game()

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

def guessing_game_prime_or_not():
    number = int(input('Enter a number please'))
    while number < 100:
        a = 2
        number = int(input('Enter a number please'))
        if number > 100:
            print(number)
        while a < math.sqrt(number):
            if number%a < 1:
                print('Not prime')
                break
            else:
                print('Prime')
                break


guessing_game_prime_or_not()





