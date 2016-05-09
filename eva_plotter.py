import sys
import csv
import matplotlib.pyplot as plt


# 1: res dump file
# 2: volatility drift dump file
def main(args):
    x = []
    correct_rate = []
    vol_drift_positions = []
    plt.ylim([50, 100])

    with open(args[0], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            x.append(float(row['learning evaluation instances']))
            correct_rate.append(float(row['classifications correct (percent)']))
    plt.plot(x, correct_rate, 'r')

    with open(args[1], 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vol_drift_positions.append(float(row['VolatilityDriftInstance']))


    plt.axvline(vol_drift_positions, color='b')

    plt.xlabel('instance')
    plt.ylabel('percentage of correct')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])