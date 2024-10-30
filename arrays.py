courses=["MIT","CYBERSECURITY","DATA SCIENCE"]
print(courses)

#accessing lements in an array
print(courses[1])

#looping through an array
for y in courses:
    print("course is",y)

#adding new elements to an array
courses.append("android development")
print(courses)


#removing an element from an array
courses.remove("MIT")
print(courses)