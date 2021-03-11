num = int(input("Please type in a number: "))
print("The factors of ", str(num), " are: ")
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1
    
