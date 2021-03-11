import matplotlib.pyplot as plt

people = ['Adam', 'Eve', 'Paul', 'Rassel', 'Kate', 'Peter']
ages = [45, 25, 67, 70, 21, 34]

plt.bar(range(len(people)), ages, tick_label=people)

plt.ylabel("Ages")
plt.title("People's ages")
plt.show()
