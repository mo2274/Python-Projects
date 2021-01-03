import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use("seaborn")
fig, ax = plt.subplots()
x_values = [i for i in range(0, 1001)]
y_values = [i**2 for i in range(1001)]
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=1)
'''
ax.plot(input_values, squares)
'''
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.axis([0, 1100, 0, 1100000])
'''
plt.show()
'''
plt.savefig('squares_plot.png', bbox_inches='tight')