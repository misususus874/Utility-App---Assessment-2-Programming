from matplotlib import pyplot as plt


def main():
    # Create lists with the X and Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Build the line graph.
    plt.xlim(xmin= 0, xmax=5)
    plt.ylim(ymin=0, ymax=5)

    plt.plot(x_coords, y_coords, marker='')

    # Display the line graph.
    plt.show()
# Call the main function.
if __name__== '__main__':
    main()
