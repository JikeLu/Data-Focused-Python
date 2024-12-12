# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

# Q1a ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Open the file we wanna read
readFile = open('daily-treasury-rates.csv', 'r')
lines = readFile.readlines()

daily_yield_curves = []
# Append header: remove quotes, "4 mo", and \n
headerLine = lines[0][:-1].replace('"', '').split(",")
headerLine = headerLine[:4] + headerLine[5:]
daily_yield_curves.append(headerLine)

# Now parse the data lines
for line in lines[1:]:
    # Remove commas, "4 mo" col, and \n
    splitLine = line[:-1].split(",")
    splitLine = splitLine[:4] + splitLine[5:]
    # Convert all numeric values to float, add line to list
    toAdd = [splitLine[0]] + \
            [float(splitLine[i]) for i in range(1, len(splitLine))]
    daily_yield_curves.insert(1, toAdd)

# ~~~~~~~~~~
# Write daily_yield_curves as a formatted table in a new file
writeFile = open("daily_yield_curves_2022.txt", "w")

# Loop thru 2d list
for row in range(len(daily_yield_curves)):
    line = daily_yield_curves[row]
    # Add line divider after header
    if (row==1):
        writeFile.write(("-"*110)+"\n")
    
    # Write each cell in the line to the file
    for col in range(len(line)):
        cell = line[col]
        # Change len of date column to be longer than other cols
        if (col==0):
            writeFile.write(f"{str(cell):14}")
        else:
            writeFile.write(f"{str(cell):8}")
    writeFile.write("\n")

readFile.close()
writeFile.close()

# Q1b ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MONTH_DICT = {"1 Mo": 1, "2 Mo": 2, "3 Mo": 3, "6 Mo": 6, 
             "1 Yr": 12, "2 Yr": 24, "3 Yr": 36, "5 Yr": 60, "7 Yr": 84,
             "10 Yr": 120, "20 Yr": 240, "30 Yr": 360}

# Creating dataset
'''
X = days since 01/03/22
Y = Months to Maturity (1-360 months)
Z = rate 
'''
X = np.arange(249) #WRONG, FIX!!!!!
Y = np.array([val for val in MONTH_DICT.values()])
X, Y = np.meshgrid(X, Y)
Z = np.array([line[1:] for line in daily_yield_curves[1:]])

# Surface Plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_surface(X, Y, np.transpose(Z), cmap=cm.coolwarm)
fig.colorbar(surf, ax = ax, shrink = 0.5, aspect = 5, anchor= (1, .5))
# Adding labels
ax.set_xlabel('trading days since 01/03/22')
ax.set_ylabel('months to maturity')
ax.set_zlabel('rate')

# ~~~~~~~~~~

# Wireframe Plot
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1, projection='3d')
wire = ax2.plot_wireframe(X, Y, np.transpose(Z))
# Adding labels
ax2.set_xlabel('trading days since 01/03/22')
ax2.set_ylabel('months to maturity')
ax2.set_zlabel('rate')

# Q1c ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create first DF
dfData = [line[1:] for line in daily_yield_curves[1:]]
dfIndices = [line[0] for line in daily_yield_curves[1:]]
dfColumns = daily_yield_curves[0][1:]
yield_curve_df = pd.DataFrame(dfData, index=dfIndices, columns=dfColumns)
print(yield_curve_df)

# ~~~~~~~~~~

# Create second DF
by_day_yield_curve_df = yield_curve_df.T
# Remove all cols from the df whose index is not a factor of 20
colsToKeep = [dfIndices[i] for i in range(len(dfIndices)) if i%20==0]
by_day_yield_curve_df = by_day_yield_curve_df.loc[:, colsToKeep]
# Rename indexes to use number of months
by_day_yield_curve_df = by_day_yield_curve_df.set_axis(MONTH_DICT.values())
print(by_day_yield_curve_df)

# Plot both DFs
yield_curve_df.plot()
by_day_yield_curve_df.plot()
plt.show()