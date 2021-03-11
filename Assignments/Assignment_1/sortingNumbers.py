def ascend(numbers):
    ascending_numbers = sorted(numbers)
    print("List of numbers in ascending order:")
    for number in ascending_numbers:
        print(number, end = " ")
    print('\n')

def descend(numbers):
    descending_numbers = sorted(numbers, reverse=True)
    print("List of numbers in descending order:")
    for number in descending_numbers:
        print(number, end = " ")
    print('\n')

numbers = []
for i in range(5):
    numbers.append(int(input("Please enter an integer: ")))
print("\nList of numbers unordered:")
for number in numbers:
    print(number, end = " ")
print('\n')
ascend(numbers)
descend(numbers)
