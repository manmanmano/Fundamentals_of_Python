import matplotlib.pyplot as plt

labels = ['Comedy', 'Action', 'Romance', 'Drama', 'SciFi']
colors = ['yellow', 'orange', 'red', 'blue', 'green']
visions = [4, 5, 6, 1, 4]

plt.pie(visions, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()
