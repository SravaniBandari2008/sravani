# Type Casting (done by the programmer)

num = "25"
number = int(num)   # Convert string to integer

print(number)
print(type(number))
# Type Conversion (done automatically by Python)

a = 10      # int
b = 2.5     # float

result = a + b

print(result)
print(type(result))
 
# input statement
name = input("enter your name:")
print ("welocome," + name + "!" )
age =input("enter your age:")
print ("you are " + age + "years old")