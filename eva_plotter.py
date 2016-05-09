import sys
import csv
import matplotlib.pyplot as plt


# 1: res dump file
# 2: volatility drift dump file
def main(args):
    x = []
    correct_rate = []
    vol_drift_positions = []
    with open(args[0], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            x.append(float(row['learning evaluation instances']))
            correct_rate.append(float(row['classifications correct (percent)']))

    with open(args[1], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vol_drift_positions.append(float(row['VolatilityDriftInstance']))

    plt.plot(x, correct_rate, 'r')
    plt.axvline(vol_drift_positions, color='b', linestyle="---")

    plt.xlabel('instance')
    plt.ylabel('percentage of correct')
    plt.grid(True)


if __name__ == "__main__":
    main(sys.argv[1:])