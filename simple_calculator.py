#simple calculator. just for testing inputs and outputs
first_number = int(input("first number: "))
second_number = int(input("entry second number: "))

operation = int(input("choose operation: \n 1- add \n 2- sub \n 3- mult \n 4- div "))
result = 0
if (operation == 1):
    result = first_number + second_number
    
elif (operation == 2):
    result = first_number - second_number
elif(operation == 3):
    result = first_number * second_number
elif(operation == 4):
    result = first_number/second_number
else:
    print("no valid operation, restart the calculator")

print(result)
