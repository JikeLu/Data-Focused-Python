# This is a sample Python script.
import csv
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import cm


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_csv(file):
    daily_yield_curves = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            row_append = []
            for value in row:
                try:
                    row_append.append(float(value))
                except ValueError as e:
                    row_append.append(value)
            row_append.pop(4) # This Line only for the 2022 file
            daily_yield_curves.append(row_append)
    return daily_yield_curves

def write_data(file, data):
    with open(file, 'w') as fout:
        for row in data:
            fout.write('\t'.join(map(str, row)) + '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = 'daily-treasury-rates_2022.csv'
    daily_yield_curves = read_csv(file)
    for row in daily_yield_curves:
        print(row)
    write_data("daily_yield_curves_2022.txt", daily_yield_curves)

    data_without_header = daily_yield_curves[1:]
    dates = [datetime.strptime(row[0], '%m/%d/%Y') for row in data_without_header]
    interest_rates = np.array([row[1:] for row in data_without_header], dtype=float)

    # Calculate the number of days since the first date
    days_since_start = np.array([(date - dates[0]).days for date in dates])
    column_labels = daily_yield_curves[0][1:]
    months_to_maturity = [1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]

    cn_to_nm = dict(zip(column_labels, months_to_maturity))

    data_array = np.array(daily_yield_curves)

    X, Y = np.meshgrid(days_since_start, months_to_maturity)

    fig = plt.figure(figsize=(15, 6))

    # Create a 3D subplot for the Surface Plot
    ax_surface = fig.add_subplot(121, projection='3d')
    ax_surface.plot_surface(X, Y, interest_rates.T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax_surface.set_xlabel('Trading Days Since 01/03/2022')
    ax_surface.set_ylabel('Months to Maturity')
    ax_surface.set_zlabel('Rate')
    ax_surface.set_title('3D Surface Plot')

    # Create a 3D subplot for the Wireframe Plot
    ax_wireframe = fig.add_subplot(122, projection='3d')
    ax_wireframe.plot_wireframe(X, Y, interest_rates.T, cmap=cm.coolwarm)
    ax_wireframe.set_xlabel('Trading Days Since 01/03/2022')
    ax_wireframe.set_ylabel('Months to Maturity')
    ax_wireframe.set_zlabel('Rate')
    ax_wireframe.set_title('Wireframe Plot')

    # Show the plots
    plt.show()

    headers = daily_yield_curves.pop(0)
    headers = headers[1:]

    indexes_inner = []
    indexes = []
    for i in daily_yield_curves:
        for j in i:
            if isinstance(j, str):
                indexes_inner.append(j)
        indexes.extend(indexes_inner)
        indexes_inner = []

    for i in range(len(daily_yield_curves)):
        for j in range(len(daily_yield_curves[i])):
            if j == 0:
                daily_yield_curves[i].pop(j)

    yield_curve_df = pd.DataFrame(daily_yield_curves, columns=headers, index=indexes)

    ax = yield_curve_df.plot(title='Interest Rate Time Series, 2022')
    ax.legend(loc='center right', prop={'size': 8})
    plt.show()

    by_day_yield_curve_df = yield_curve_df.iloc[::20, :].copy()
    by_day_yield_curve_df.columns = months_to_maturity
    by_day_yield_curve_df = by_day_yield_curve_df.T

    ax = by_day_yield_curve_df.plot(title='2022 Yield Curves, 20 Day Intervals')
    ax.legend(loc='lower right', prop={'size': 8})
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
