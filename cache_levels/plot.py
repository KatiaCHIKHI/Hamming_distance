import matplotlib.pyplot as plt
import numpy as np
import csv

def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.
        
        courtesy of @pascscha stackoverflow
        https://stackoverflow.com/a/60270421
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())


#MAIN
if __name__ == "__main__":

    levels = ["L1","L2","L3"]

    gcc_gib={"L1":0.0,"L2":0.0,"L3":0.0}
    icc_gib={"L1":0.0,"L2":0.0,"L3":0.0}
    icx_gib={"L1":0.0,"L2":0.0,"L3":0.0}

    gcc_ns={"L1":0.0,"L2":0.0,"L3":0.0}
    icc_ns={"L1":0.0,"L2":0.0,"L3":0.0}
    icx_ns={"L1":0.0,"L2":0.0,"L3":0.0}

    for lvl in levels:
        with open('gcc/result'+lvl+'.csv','r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for row in lines:
                if row[0] == "bandwidth(GiB/s)":
                    gcc_gib[lvl] = float(row[1])
                elif row[0] == "elapsed_time(ns)":
                    gcc_ns[lvl] = float(row[1])

        with open('icc/result'+lvl+'.csv','r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for row in lines:
                if row[0] == "bandwidth(GiB/s)":
                    icc_gib[lvl] = float(row[1])
                elif row[0] == "elapsed_time(ns)":
                    icc_ns[lvl] = float(row[1])

        with open('icx/result'+lvl+'.csv','r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for row in lines:
                if row[0] == "bandwidth(GiB/s)":
                    icx_gib[lvl] = float(row[1])
                elif row[0] == "elapsed_time(ns)":
                    icx_ns[lvl] = float(row[1])


    data_gib={"L1":[gcc_gib["L1"],icc_gib["L1"],icx_gib["L1"]],
              "L2":[gcc_gib["L2"],icc_gib["L2"],icx_gib["L2"]],
              "L3":[gcc_gib["L3"],icc_gib["L3"],icx_gib["L3"]]}
    
    data_ns={"L1":[gcc_ns["L1"],icc_ns["L1"],icx_ns["L1"]],
              "L2":[gcc_ns["L2"],icc_ns["L2"],icx_ns["L2"]],
              "L3":[gcc_ns["L3"],icc_ns["L3"],icx_ns["L3"]]}
    
    fig = plt.figure(figsize = (10, 8))
    plt.suptitle("Performance des differents compilateurs C pour calculer la distance Hamming des séquences ADN")


    ax1 = plt.subplot(1,2,2)
    bar_plot(ax1, data_gib, total_width=.8, single_width=.9)

    plt.xticks(range(3), ["gcc", "icc", "icx"])
    plt.xlabel("Compilers")
    plt.ylabel("GiB/s")


    ax2 = plt.subplot(1,2,1)
    bar_plot(ax2, data_ns, total_width=.8, single_width=.9)
    
    plt.xticks(range(3), ["gcc", "icc", "icx"])
    plt.xlabel("Compilers")
    plt.ylabel("nanoseconds")


    plt.savefig("results.png")