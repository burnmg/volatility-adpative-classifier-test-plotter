import csv
import matplotlib.pyplot as plt
import os.path
import numpy as np
import sys


def analyse(res_file, drift_point_file, to_summary_file, to_figure_file):
    instances_index = []
    correct_rates = []
    bytes = []
    times = []

    # correct rate plot
    if os.path.isfile(res_file):

        with open(res_file, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                instances_index.append(float(row['learning evaluation instances']))
                correct_rates.append(float(row['classifications correct (percent)']))
                bytes.append(float(row['model serialized size (bytes)']))
                times.append(float(row['evaluation time (cpu seconds)']))
        plt.plot(instances_index, correct_rates, 'r')

        # write avg correct_rates, time, byte
        mean_correct_rates = np.mean(correct_rates)
        mean_bytes = np.mean(bytes)

        with open(to_summary_file, 'w') as summary:
            fieldnames = ['mean correct rate', 'time', 'mean byte']
            writer = csv.DictWriter(summary, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({
                'mean correct rate': mean_correct_rates,
                'time': times[len(times)-1],
                'mean byte': mean_bytes

            })

    plt.xlabel('instance')
    plt.ylabel('percentage of correct')

    # change point plot
    # if os.path.isfile(drift_point_file):
    #     change_points = []
    #     with open(drift_point_file, 'r') as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             change_points.append(float(row['ClassifierChangePoint']))
    #     for i in change_points:
    #         plt.axvline(i, color='b')
    #
    plt.grid(True)
    plt.savefig(to_figure_file)


def main(argv):
    analyse(argv[0], argv[1], argv[2], argv[3])


if __name__ == "__main__":
   main(sys.argv[1:])

