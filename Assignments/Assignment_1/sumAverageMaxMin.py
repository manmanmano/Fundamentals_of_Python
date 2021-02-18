import statistics

def ArrayMaker():
    List = []
    while True:
        fill = float(input("Enter a float value: "))
        if fill < 0:
            break
        else:
            List.append(fill)
    return List

numbers = ArrayMaker()
print("\nCreated list: ", end = " ")
for number in numbers:
    print(number, end = "  ")
print("\n\nThe max value in the list is:", max(numbers))
print("The min value in the list is:", min(numbers))
print("The mean of the values in the list is:", statistics.mean(numbers))
print("The sum of the values in the list is:", sum(numbers))
