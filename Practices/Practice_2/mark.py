mark = int(input("Please type in your mark: "))
if mark >= 90 and mark <= 100:
    print("Your mark is A+.")
elif mark >= 80 and mark <= 89:
    print("Your mark is A.")
elif mark >= 70 and mark <= 79:
    print("Your mark is B.")
elif mark >= 60 and mark <= 69:
    print("Your mark is C.")
elif mark >= 50 and mark <= 59:
    print("Your mark is D.")
else:
    print("You failed!")
