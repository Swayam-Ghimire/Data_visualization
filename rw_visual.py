import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk, and plot the points.
# Keep making new walks, as long as the program is active.
while True:
    # Create a new figure with the specified size and resolution
    plt.figure(figsize=(10, 6), dpi=128, facecolor='cyan') # 10 and 6 are inch 10*123 = 1000 pixels width. inch*dpi=pixels
    # The figure() function controls the width, height, resolution, and background color of the plot
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, edgecolor=None, cmap=plt.cm.BuGn, s=1)
    #plt.plot(rw.x_values,rw.y_values,color='black',linewidth=1, zorder=1)
    # all the points ie from 0 to 49999 are coloured no matter what is the x and y values.
    # the color of each point depends on its position in the list point_numbers
    plt.scatter(0, 0, c='green', edgecolors='none', s=10) # starting point
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10) # ending point
    plt.axis('off')
    plt.axis('off')
    plt.show()
    keep_running = input("Still wanna generate random walk?(y/n)\n")
    if keep_running == 'n':
        break

