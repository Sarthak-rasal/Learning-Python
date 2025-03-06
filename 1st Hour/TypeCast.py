#Process of converting one variable from one datatype to another 

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


print("Typecasting")

#Typecasting
print("age")
age = float(age)
print(type(age))
age = str(age)
print(type(age))

print("gpa")
gpa = int(gpa)
print(type(gpa))

print("name to bool")
print (name)
name = ""
print(name)
