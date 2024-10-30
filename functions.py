#build in library functions
y=max(56,78,90,23,12)
print(y)

x=min(67,10,32,45)
print("the minimum value is",x)

z=pow(2,3)
print("the result is",z)


#user defined functions
def greetings():
    print("hello there")
greetings()#calling a function


def multiply():
    num1=12
    num=12
    print(num1*num)
multiply()

#parameter and arguements
#parameter are variables
def add():
    a=33
    b=4
    print(a+b)
add( )


def employee(fullname:,age,position,status):
    print(fullname,age,position,status)

employee(fullname:"ruth nyanchama" age:"23",position:"hr",status:"single")