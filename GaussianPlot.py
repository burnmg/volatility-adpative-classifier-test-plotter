import csv
import matplotlib.pyplot as plt



x = []
y = []

with open('/Users/rl/Desktop/output/sampleoutput.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row['learning evaluation instances']))
        y.append(float(row['classifications correct (percent)']))


plt.subplot(3, 1, 1)
plt.plot(x, y, 'r')
plt.xlabel('instance')
plt.ylabel('percentage of correct')
plt.title('low volatility')
plt.grid(True)

plt.savefig('gaussian.png')
plt.show()
