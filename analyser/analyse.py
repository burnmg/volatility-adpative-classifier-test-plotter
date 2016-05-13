import csv
import matplotlib.pyplot as plt
import os.path
import numpy as np

instances_index = []
correct_rates = []
bytes = []
times = []

# correct rate plot
res_file = "res.csv"
if os.path.isfile(res_file):

    with open(res_file, 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            instances_index.append(float(row['learning evaluation instances']))
            correct_rates.append(float(row['classifications correct (percent)']))
            bytes.append(float(row['model serialized size (bytes)']))
            times.append(float(row['evaluation time (cpu seconds)']))
    plt.plot(instances_index, correct_rates, 'r')

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


# write avg correct_rates, time, byte
mean_correct_rates = np.mean(correct_rates)
mean_bytes = np.mean(bytes)

with open('summary.csv', 'w') as summary:
    fieldnames = ['mean correct rate', 'time', 'mean byte']
    writer = csv.DictWriter(summary, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({
        'mean correct rate': mean_correct_rates,
        'time': times[len(times)-1],
        'mean byte': mean_bytes

    })

plt.show()
