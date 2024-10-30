#
number=35 #an integer ,int
second=56.76 #float
text="hello there" #string ,
isPythonInteresting =True #boolean


#datastructure- multiple values stored in a single valuable
cars=["toyota","brado","BMW"]  #this ai a list,,the list is ordered and are changeable
fruits=("banana","orange","apple") #this is a tuple-ordered but unchangeable
counries={"kenya","lagos","algeria"}#this is a set-they are unordered and unchangeable
student={
    "firstname":"mary",
    "age":43,
    "course":"web development",
    "nationality":"kenyan",
}#key and value pair

print(cars)
print(fruits)
print(counries)
print(student["nationality"])





print(number)
print(second)
print(text)
print(isPythonInteresting)

#determining a datatype
print(type(counries))
print(type(student))



#typecasting-process of converting from one data type to another
print(float(number))
print(int(second))