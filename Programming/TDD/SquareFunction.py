#this program will ask the user if they want to add or multiply two numbers together

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print("Select operation.")
print ("1. Add")
print ("2. Multiply")

choice = input("Enter choice (1/2):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == '2':
    print(num1, "*", num2, "=", multiply(num1, num2))

else:
    print ("Invalid input")

    
