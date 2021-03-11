import matplotlib.pyplot as plt

X1 = [2, 5, 6]
Y1 = [1, 6, 8]
X2 = [4, 7, 9]
Y2 = [9, 3, 4]

plt.plot(X1, Y1, 'go-',
             X2, Y2, 'y*:')

plt.title("mygraph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(['line1', 'line2'])
plt.show()

