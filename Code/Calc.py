#This is a fancy calc that will have many functions. The mail point is for me to practice what I have learned in my classes and build upon it
print("Welcome to your Fancy Calculator!")
print("I will call you by your name, because who doesnt love that?")
name = input("What is your wonderful name?")

print("Nice to meet you, %s!" % name)
print(name) #Showing myself input

oper = input("Enter Operator: ") #Requests simple operator

if oper == "add":  #checks to see what operator input was
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    result = (num1 + num2) #because oper was add the numbers are added and printed. SIMPLE!
    print(result)

if oper == "subtract": #subtraction ability
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))
    result = (num1 - num2)
    print(result)
