import csv
import matplotlib.pyplot as plt
import os.path


x = []
y = []

# correct rate plot
resfile = "res.csv"
if os.path.isfile(resfile):

    with open(resfile, 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            x.append(float(row['learning evaluation instances']))
            y.append(float(row['classifications correct (percent)']))
    plt.plot(x, y, 'r')

plt.xlabel('instance')
plt.ylabel('percentage of correct')

# change point plot
change_point_path = "changepoint.csv"
if os.path.isfile(change_point_path):
    change_points = []
    with open(change_point_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            change_points.append(float(row['ClassifierChangePoint']))
    for i in change_points:
        plt.axvline(i, color='b')
plt.grid(True)
plt.show()

# write avg correct_rate, time, byte

