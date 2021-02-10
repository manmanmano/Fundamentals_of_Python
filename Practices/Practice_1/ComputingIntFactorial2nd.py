given_number = int(input("Type in an integer: "))
fact = 1
for i in range (1, given_number + 1):
    fact *= i;
print("The factorial of the given number is: ", fact)
