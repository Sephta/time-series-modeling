"""
CIS 422 Winter 2021
University of Oregon
Bitwise Team
Project One: Time Series Analysis

Description: Statistics And Visualization. Module created
in order to plot time series in sereral representations (i.e
histograms, box & Whisker, etc.) as well as calculations % error(s).

Note: pandas, numpy, matplotlib, scipy, seaborn, & random
must be downloaded in order to use this
software.
"""
from numpy import genfromtxt  # if csv file is given as input, use it.
import random  # Used only when multiple TS are given (Change colors)
import math  # Used in error functions. Specifically pow & sqrt
import numpy as np
import pandas as pd  # Used in case TS object is passed.
from scipy.stats import shapiro, normaltest, anderson  # Normality tests
from statsmodels.graphics.gofplots import qqplot
import seaborn as sns  # represent statistical data
from matplotlib import pyplot as plt
# Currently using test_data. Comment out using other functions/libs.
# from test_data import ts1, ts2, ts3, ts1_test, ts1_pred


__authors__ = "Ronny Fuentes"
__version__ = "1.2.2"
__emails__ = "ronnyf@uoregon.edu"
__credits__ = "Stephanie Schofield, Kyra Novitzky, Alec Springel, Seth Tal"
__date__ = "01/21/2021"


def ts_to_list(ts):  # Completed
    """
    Helper function used to convert a pandas time
    series object back to a python list object.
    """
    if isinstance(ts, pd.core.series.Series):
        ts = ts.values.tolist()
    return ts


def list_to_ts(ts_list):
    """ Converts list to a time series object. """

    # converts ts_list to a Series
    ts = pd.Series(ts_list)

    return ts


def multi_plot_ts(ts_list):  # Completed
    """
    Helper function used to plot multiple
    time series.
    Input must be a list of time series
    """
    size = len(ts_list)
    # Creates a grid for a set of subplots.
    fig, ax = plt.subplots(size)
    fig.suptitle("Plots")  # Title
    # Plots each TS on it's own figure w/ random color.
    for i in range(size):
        ax[i].plot(ts_list[i], color=(random.uniform(0, 1),
                                      random.uniform(0, 1),
                                      random.uniform(0, 1)))
        plt.subplots_adjust(hspace=.5)
        ax[i].grid()
    plt.show()
    return
# multi_plot_ts([ts1, ts2])


def plot_ts(ts):  # Completed
    """
    Function that generically plots a single time
    series or multiple time series.
    Calls: multi_plot if multi-layer array is given.
    """
    # Check the dimension of input
    # Are we working with single/many TS?
    if isinstance(ts[0], list):
        return multi_plot_ts(ts)

    ts = ts_to_list(ts)  # Converts ts object to list object
    title = plt.subplots()  # return type: Tuple
    title[0].suptitle("Plots")
    # ax.set(xlabel='Days', ylabel='Temperature')
    plt.plot(ts, "g", linewidth=2.0)
    plt.grid()
    plt.show()

    ts = list_to_ts(ts)
    return ts
# plot_ts(ts1)


def histogram(ts):  # Completed
    """
    Computes and draws the histogram of the given
    time series. Plot the histogram vertically and
    side to side with a plot of the time series.
    """
    ts = ts_to_list(ts)
    data = ts
    datax = []
    for i in range(len(data)):
        # building the x-axis coordinates
        datax.append(i)
    sns.set()
    # JointGrid builds a grid of subplots (i.e multiple data reps.)
    g = sns.JointGrid(data=data, x=datax, y=data)
    g.ax_marg_y.set_axis_off()
    plt.subplots_adjust(top=.92)  # Buffer for title
    g.fig.suptitle("Histogram")   # Title
    # Plots a histogram and line representation.
    g.plot(sns.lineplot, sns.histplot, color="r")
    plt.grid()
    plt.show()

    ts = list_to_ts(ts)
    return ts
# histogram(ts1)


def box_plot(ts):  # Completed
    """
    Produces a Box and Whiskers plot of the time series.
    Also prints the 5-number summary of the data.
    """
    ts = ts_to_list(ts)
    # Array of Loaded functions for summary
    summary = [lambda x: f"Min: {np.min(x)}", lambda x: f"Max: {np.max(x)}",
               lambda x: f"SD: {np.std(x):.3f}",
               lambda x: f"Mean: {np.mean(x):.3f}",
               lambda x: f"Median: {np.median(x)}"]

    # Calculates 5-number summary of data
    for fun in summary:
        print(fun(ts))
    # Creating the grid for the boxplot, and plotting.
    sns.set_theme(style="whitegrid")
    sns.boxplot(x=ts, color="green")
    plt.show()

    ts = list_to_ts(ts)
    return ts
# box_plot(ts1)


def normality_test(ts):  # Completed
    """
    Performs a series of hypothesis tests about normality
    on the time series data distribution. Besides
    the result of the statistical test, this also includes
    a quantile plot of the data (qqplot).

    Note: Shapiro & Kolmogorov-Smirnov Tests can still produce
    inconsistencies if the data set (size) is to small to detect
    non-normality.
    """
    ts = ts_to_list(ts)
    data = np.array(ts)
    # Shapiro-Wilk test: Detects all departures from normality.
    # Rejects the hypothesis of normality when the p-value is <= to 0.05.
    # i.e not from a normal distribution.
    stat_sw, p_sw = shapiro(data)  # (1) Normality test
    # Kolmogorov-Smirnov: Tests the sample data against
    # another sample, to compare their distributions for
    # similarities, not just for normal distributions.
    # If p < .05 we can reject the null, meaning our sample
    # distribution is not identical to a normal distribution.
    stat_ks, p_ks = normaltest(data)  # (2) Normality test
    # Anderson-Darling: Test is the data comes from a particular
    # distribution (one of many). Modified version of the
    # Kolmogorov-Smirnov to check for normality. However, rather
    # Than a p-value, we're given an array of critical values
    # where the hypothesis can be rejected.
    stat_ad = anderson(data)  # (3) Normality test
    # Print results of all 3 tests
    print(f'\nShapiro-Wilk Statistic Test Result: {stat_sw:.3f}')
    print(f'P-value: {p_sw}: ', end='')
    # Check if (SW) from normal distribution or not.
    if p_sw < 0.05:
        print("Null Hypothesis Rejected. Not from normal distribution.\n")
    else:
        print("Accepted Null Hypothesis.\n")
    print(f'Kolmogorov-Smirnov Statistic Test Result: {stat_ks:.3f}')
    print(f'P-value: {p_ks}', end='')
    # Check if (KS) from normal distribution or not.
    if p_ks < 0.05:
        print("Null Hypothesis Rejected. Not from normal distribution.\n")
    else:
        print("Accepted Null Hypothesis. Can occurs if data set is too small.")
    print(f'Anderson-Darling Statistic Test Result: {stat_ad.statistic}')
    # Check if (AD) from normal distribution or not.
    for i in range(len(stat_ad.critical_values)):
        st, cv = stat_ad.significance_level[i], stat_ad.critical_values[i]
        if stat_ad.statistic < stat_ad.critical_values[i]:
            print(f'{st:.3f}: {cv:.3f}: Accepted. From normal distribution')
        else:
            print(f'{st:.3f}: {cv:.3f}: Rejected. Data not normal')
    # Plots a standardized line, scaled by the SD of the time series.
    qqplot(data, line='s')
    plt.show()

    ts = list_to_ts(ts)
    return ts
# normality_test(ts1)


######
# Error Functions
######


def mse(y_test, y_forecast):  # Completed
    """
    Computes the MSE error of two time series.
    """
    # Makes sure inputs are of the same length.
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
    return y_test
# mse(ts1, ts1_pred)


def mape(y_test, y_forecast):  # Completed
    """
    Computes the MAPE error of two time series.
    """
    # Makes sure inputs are of the same length.
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
    return y_test
# mape(ts1, ts1_pred)


def smape(y_test, y_forecast):  # Completed
    """
    Computes the SMAPE error of two time series.
    """
    # Makes sure inputs are of the same length.
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
    return y_test
# smape(ts1, ts1_pred)
