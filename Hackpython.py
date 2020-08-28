#!/bin/python3
#This is print string
print("Hello")
print("This" + " This")
print("""This is a  multi
line script!""")
print ('\n')#new line
print('Math')
print (50 + 50)
print (50 - 50)
print (50 * 50)
print (50 / 50)
print (50 + 50 - 50 * 50 / 50)
print(50 ** 2) #exponent
print(50 % 6) #modulo
print(50 // 6)# number without leftovers

print ('\n')#new line

#Variables and Methods

print("Variables and Methods")
print('\n')
quote = "All Fair"
print (len(quote)) #length
print(quote.upper())
print(quote.lower())
print(quote.title())

name = 'james'
age = 53 #int int(29)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(53.8))


age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')

#functions
print("Functions")
print('\n')
def who_am_i():
    name = 'james'
    age = 53 #int int(29)
    gpa = 3.7 #float float(3.7)
    print("My name is " + name + " I am " +str(age+10) + " years old")
who_am_i()

#adding a parameter
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x +y)

add(123,345)
add(9,9)

#using return
def multiply(x,y):
    return x * y

print(multiply(7,7))

def square_root(x):
    return x ** .5

print(square_root(64))

def nl():
    print('\n')

nl()
print("Booleans")

#(true or False)

bool1 = True
bool2 =3*3 == 9
bool3 = False
bool4 = 3*3 !=9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

#conditional Statements

def soda(money):
    if money >= 2:
        return "You've got yourself a soda!"
    else:
        return "no soda for you!"

print(soda(1))
print(soda(5))

def drinks(age,money):
    if (age >= 21) and (money >= 5):
        return "Time to Party"
    elif (age >= 21) and (money < 5):
        return "Nope,Nada,Never"
    elif (age < 21 ) and (money >= 5):
        return "No Way Kid"
    else:
        return "Nothing works for you"

print(drinks(21,5))
print(drinks(21,4))
print(drinks(20,5))
print(drinks(20,3))

nl()
print("Lists")
nl()
movies = ["Silver Surfer", "Stripes", "Star wars","wedding crashers"]
print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[:1])
print(movies[-1])
print(len(movies))
movies.append("Jaws")
print(movies)

movies.pop()
print(movies)
movies.pop(1)
print(movies)

movies = ["Silver Surfer", "Stripes", "Star wars","wedding crashers"]
person = ["James", "Bob", "leah", "Joe"]
combined = zip(movies, person)
print(list(combined))
nl()
print("Tuples have parentheses and cannot change")
nl()
grades = ("A", "B", "C", "D", "F")
print(grades[1])

#Looping
nl()
print("Looping")
nl()
vegetables = ["carrot", "peas", "potatoes","Kale"]
for x in vegetables:
    print(x)

    nl()
    print("While Loops")
    nl()
    i = 1
    while i <= 10:
        print(i)
        i += 1
