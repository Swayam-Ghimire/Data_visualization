"""
pyplot provides a convenient interface for creating common types of plots, such as line plots, scatter plots, histograms,
bar charts, and more. It also provides tools for customizing the appearance of plots, such as changing the colors, labels,
axes, and legends.

"""
import matplotlib.pyplot as plt

input_numbers = [1, 2, 3, 4, 5]  # x-values
squares = [1, 4, 9, 16, 25]  # y-values
plt.plot(input_numbers, squares, linewidth=1, color='red', marker='o', linestyle='dotted', markersize=12)
# color arg makes the line of desired coloured.
# linestyle="dotted", "dashed", "dashdot" is the syle of the drawn line.
# marker arg marks the x and y points which we put in this function as argument previously. "o" is circle,'D' is diamond
# markersize arg allocates the size of marker.
# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()
