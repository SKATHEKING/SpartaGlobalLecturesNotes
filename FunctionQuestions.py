print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisiors(n):
    divided = []
    for i in range(1,n+1):
        if n%i == 0:
            divided.append(i)
    print(divided)

divisiors(12)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor(n,m):
    if n%m == 0 :
        print(True)
        return  True
    else:
        print(False)
        return False

factor(8,2)




# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def position(n):
    for i in alphabet:
        if i == n:
            print(alphabet.index(n))
            return alphabet.index(n)
            break

position('m')

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def id_generator(name):
    id = ' '
    for char in name:
        id += str(position(char))

    print(id)
    return id
id_generator('mateus')


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password_gen(name):
    id = int(id_generator(name))
    pass_sum = 0
    while(id > 0):
        remainder = id % 10
        pass_sum = pass_sum + remainder
        id = id // 10
    password = 0
    password = int(id_generator(name)) - pass_sum
    print(password)

password_gen('mateus')



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime(number):
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            print(False)
            return False
    print(True)
    return True

prime(3)
prime(20)
prime(5)

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def prime_is_digit(number):
   if number > 0:
       for n in range(2, int(number ** 0.5) + 1):
           if number % n == 0:
               print(False)
               return False
       print(True)
       return True

prime_is_digit(7)
prime_is_digit(8)

# -------------------------------------------------------------------------------------- #






