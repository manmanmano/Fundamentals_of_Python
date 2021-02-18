import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 9, 2]
plt.plot(x, y, 'y*-')

#graph title must be "mygraph"
plt.title("mygraph")

#xlabel must be "x-axis"
plt.xlabel("x-axis")

#ylabel must be "y-axis"
plt.ylabel("y-axis")

plt.show()
