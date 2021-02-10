given_number = int(input("Type in an integer: "))
fact = 1
for i in range(given_number, 1, -2):
    fact *= i * (i - 1)
print("The factorial of the given number is: ", fact)
