from numpy import genfromtxt
import random  # Color change if mult TS given
import math
import numpy as np
from scipy.stats import shapiro
from numpy.random import seed
from sklearn.metrics import mean_squared_error  # might not need
import matplotlib
from statsmodels.graphics.gofplots import qqplot
import seaborn as sns  # represent statistical data
from matplotlib import pyplot as plt
import pandas as pd
from test_data import ts1, ts2, ts3, ts1_test, ts1_pred
from scipy import stats


def multi_plot_ts(ts_list):  # Completed
    """
    Helper function used to plot multiple
    time series.
    """
    size = len(ts_list)
    fig, ax = plt.subplots(size)
    fig.suptitle("Plots")
    for i in range(size):
        ax[i].plot(ts_list[i], color=(random.uniform(0, 1),
                                      random.uniform(0, 1),
                                      random.uniform(0, 1)))
        plt.subplots_adjust(hspace=.5)

    plt.show()
    return
# multi_plot_ts([ts1, ts2])


def plot_ts(ts):  # Completed
    """
    Function that generically plots a single time
    series or multiple time series.
    Calls: multi_plot if multi-layer array is given.

    Note: Might need to edit this to accept a tuple
    rather than a n-dim list.
    """
    # Check the dimension of input
    if isinstance(ts[0], list):
        return multi_plot_ts(ts)

    title, ax = plt.subplots()
    # Title, ylabel, and possibly xlabel will need to reflect
    # the file in which the data is coming from. Maybe alter
    # incoming data?
    # Potential idea: Pass a tuple? Ex: ([ts], "file_info")
    title.suptitle("Plots")
    ax.set(xlabel='Days', ylabel='Temperature')
    plt.plot(ts, "g", linewidth=2.0)
    plt.show()
    return
# plot_ts(ts1)


def histogram(ts):  # Completed
    """
    Computes and draws the histogram of the given
    time series. Plot the histogram vertically and
    side to side with a plot of the time series.
    """
    data = ts
    datax = []
    for i in range(len(data)):
        # building the x-axis
        datax.append(i)
    sns.set()
    # JointGrid builds a grid of subplots (i.e multiple data)
    g = sns.JointGrid(data=data, x=datax, y=data)
    g.ax_marg_y.set_axis_off()
    plt.subplots_adjust(top=.92)  # Buffer for title
    g.fig.suptitle("Histogram")
    g.plot(sns.lineplot, sns.histplot, color="r")  # hue idea?
    plt.grid()
    plt.show()
    return
# histogram(ts1)


def box_plot(ts):  # Completed
    """
    Produces a Box and Whiskers plot of the time series.
    Also prints the 5-number summary of the data.
    """
    # Array of Loaded functions for summary
    summary = [lambda x: f"Min: {np.min(x)}", lambda x: f"Max: {np.max(x)}",
               lambda x: f"SD: {np.std(x):.3f}",
               lambda x: f"Mean: {np.mean(x):.3f}",
               lambda x: f"Median: {np.median(x)}"]

    # Calculates 5-number summary of data
    for fun in summary:
        print(fun(ts))

    sns.set_theme(style="whitegrid")
    sns.boxplot(x=ts, color="green")
    plt.show()
    return
# box_plot(ts1)


def normality_test(ts):  # 99% Complete Specify Stats tests.
    """
    Performs a hypothesis test about normality
    on the time series data distribution. Besides
    the result of the statistical test, you may want to
    include a quantile plot of the data. Scipy contains
    the Shapiro-Wilkinson and other normality tests
    """
    data = np.array(ts)
    stat = shapiro(data)  # returns tuple. Might need place holder var
    print(f'Statistics = {stat[0]:.3f}')
    # Plots a standardized line, scaled by the SD of the time series.
    qqplot(data, line='s')
    plt.show()
    return
# normality_test(ts1)


def mse(y_test, y_forecast):  # Completed
    """
    Computes the MSE error of two time series.
    """
    try:
        assert len(y_test) == len(y_forecast)
    except AssertionError:
        raise NotImplementedError(
            "Tried to call MSE function with unbalanced data.")
    total = 0
    n = len(y_test)
    # Computes MSE using equation from lecture slide.
    for i in range(n):
        total += pow((y_test[i] - y_forecast[i]), 2)
    result = total/(n)
    print(f"Mean Square Error: {result:.2f}")
    return
# mse(ts1, ts1_pred)


def mape(y_test, y_forecast):  # Completed
    """
    Computes the MAPE error of two time series.
    """
    try:
        assert len(y_test) == len(y_forecast)
    except AssertionError:
        raise NotImplementedError(
            "Tried to call MAPE function with unbalanced data.")
    total = 0
    n = len(y_test)
    # Calculates MAPE using equation from lecture slide.
    for i in range(n):
        total += abs((y_test[i] - y_forecast[i]) / y_test[i]) * 100
    result = total/n
    print(f"Mean Absolute Precentage Error: {result:.2f}")
    return
# mape(ts1, ts1_pred)


def smape(y_test, y_forecast):  # Completed
    """
    Computes the SMAPE error of two time series.
    """
    try:
        assert len(y_test) == len(y_forecast)
    except AssertionError:
        raise NotImplementedError(
            "Tried to call SMAPE function with unbalanced data.")
    total = 0
    n = len(y_test)
    # Calculates SMAPE using equation from lecture slide.
    for i in range(n):
        total += abs((y_forecast[i]-y_test[i])/(y_test[i]+y_forecast[i]))
    result = 100/n * total
    print(f"Symmetric Mean Absolute Precentage Error: {result:.2f}")
    return
# smape(ts1, ts1_pred)


print("change")
