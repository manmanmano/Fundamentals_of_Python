num = int(input("Type in a number: "))
print("The odd numbers in the given range are:")
i = 1
while i <= num:
    if i % 2 != 0:
        print(i)
    i += 1
