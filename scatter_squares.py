import matplotlib.pyplot as plt


x_values = list(range(1, 101))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=x_values, edgecolor=None, s=10, cmap=plt.cm.Blues)  # s is the size of the point
# Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square value", fontsize=10)
plt.tick_params(axis="both", labelsize=14)
"""
ticks are the small markings or indicators that appear on the axes to indicate specific values. 
There are two types of ticks: major and minor ticks. If major ticks are 1 and 10 than the minor ticks are between them.
"""
# Set range for each axis
plt.axis([0, 110, 0, 10001])
plt.show()
#plt.savefig('square_plot.png',bbox='tight') It saves the figure of the graph on after you run it on the same directory with the name in the argument


