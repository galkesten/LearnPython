x = int(input("please select a number:"))
y = int(input("please select a number:"))
z = int(input("please select a number:"))
total = x+y+z
print(type(x))
avg = total/3

if x % 2 == 0:
    print('your number is even')
else:
    print('your number is odd')

name = input("enter your name")
str = 'welcome' if len(name) > 5 else 'bye'
print(str)
