from numpy import genfromtxt
import numpy as np
import matplotlib
import seaborn  # How to represent statistical data
from matplotlib import pyplot as plt
import pandas as pd

'''
File i/o methods
read: reads the entire file as a string
readline: reads a single line from a file
readlines: each element is stored in a list (return list)
'''


def data_to_graph(input_file):

    coordinates = []
    with open(input_file) as f:
        f.readline()  # skips the garbage at the beginning of the file
        for item in f:
            if isinstance(item, int):
                coordinates.append(int(item.rstrip('\n')))
            else:
                coordinates.append(float(item.rstrip('\n')))
    return coordinates
    """
    my_data = genfromtxt(input_file, delimiter=',')
    time_series_data = my_data[1:]
    # temps = pd.read_csv(input_file)
    # plt.bar(temps, align='center')
    return time_series_data
    """
    """
    f# or i in range(len(y_coord)):
        x_coord.append(i)
    """
    """
    Still toying with numpy. Numpy has really nice prebuilt
    functions for different dimensional arrays if needed.
    Building np array. Doesn't work yet
    for i in range(1, len(y_coord)):
        np.append(x, i) # i needs to be an array type too.
    """

    """
    First successful graph. Super ugly
    plt.bar(x_coord, y_coord, align='center')
    plt.title('Temperature Test')
    plt.ylabel('Temperature')
    plt.xlabel('Days')
    plt.show()
    """
    """
    # ***** Working basic line graph *****
    til, ax = plt.subplots()
    til.suptitle("Temperature Test")
    ax.set(xlabel='Days', ylabel='Temperature')
    plt.plot(y_coord, "g", linewidth=2.0)
    # plt.plot(y_coord, "bo", linewidth=.1)
    plt.grid()
    plt.show()
    """
    '''
    Hard coded example with bar graph.
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')
    plt.title('Bar graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()
    '''


# print(data_to_graph('Time Series Data/1_temperature_test.csv'))
# print(data_to_graph('Time Series Data/1_temperature_train.csv'))
# print(data_to_graph('Time Series Data/2_temperature_subsampled_test.csv'))
# print(data_to_graph('Time Series Data/2_temperature_subsampled_train.csv'))
# print(data_to_graph('Time Series Data/3_passengers_test.csv'))
# print(data_to_graph('Time Series Data/3_passengers_train.csv'))
# print(data_to_graph('Time Series Data/4_irradiance_test.csv'))
# print(data_to_graph('Time Series Data/4_irradiance_train.csv'))
# print(data_to_graph('Time Series Data/5_irradiance_subsampled_test.csv'))
# print(data_to_graph('Time Series Data/5_irradiance_subsampled_train.csv'))
# print(data_to_graph('Time Series Data/6_sunspots_test.csv'))
# print(data_to_graph('Time Series Data/6_sunspots_train.csv'))
# print(data_to_graph('Time Series Data/8_distribution_subsampled_test.csv'))
# print(data_to_graph('Time Series Data/8_distribution_subsampled_train.csv'))
