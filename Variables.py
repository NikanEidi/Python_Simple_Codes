# Variables in Python

# string variable
name = "Nik"
print(name)
# int variable
age = 20
print(age)

# boolean variable
bool1 = False
bool2 = True
print(bool1)
print(bool2)
print()

#float variable
random_number = 1343.5

# Combine
# Method 1
print("Hello my name is " + name + " and I am " + str(age) + " years old.")
# Method 2 => using f-string
print(f"Hello my name is {name} and I am {age} years old my random number is {random_number}")

#for checking data type we use type()
print(type(name)) #=> output : <class 'str'>

# combine 2 variables
first_name = "Nikan"
Last_name = "Eidi"
Full_name = first_name + Last_name
print(Full_name)
Full_name = first_name + " " + Last_name
print(Full_name)
print(f"Hello my name is {Full_name}")





