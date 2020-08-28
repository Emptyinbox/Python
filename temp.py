print("Hello, World!")
if 5 > 2:
    print("Five is Awesome")
x = 5
# comment
y = "This is fantastic!"
print(y)
x, y, z = "red", "orange", "Yellow"
print(x)
print(y)
print(z)
x = 50
y = 100
print(x * y)
x = "jada is a dog"

def myfunc():
    global x
    x = "Kali"
    print("Who is my Dog")
    print(x)

myfunc()
x = memoryview(bytes(5))
print(x)
x = lambda a : a + 10
print(x(5))