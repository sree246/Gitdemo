num = 10
str_num = str(num)
print(str_num)  # Output: '10'
print(type(str_num)) #stringconverted


str_num = '10'
num = int(str_num)
print(num)  # Output: 10

bool_val = True
str_bool = str(bool_val)
print(str_bool)  # Output: 'True'


str_bool = 'True'
bool_val = bool(str_bool)
print(bool_val)  # Output: True


#2
# Take inputs from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

# Print values along with their data types
print("Name: ", name, type(name))
print("Age: ", age, type(age))
print("Salary: ", salary, type(salary))

# Take inputs from user skills
skills = []
while True:
    skill = input("Enter a skills:")

    print(skill)



