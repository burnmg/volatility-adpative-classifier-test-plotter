import csv
import matplotlib.pyplot as plt



x = []
y = []

with open('/Users/rl/Desktop/output/low.csv', 'rb') as f:
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





x = []
y = []

with open('/Users/rl/Desktop/output/mid.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row['learning evaluation instances']))
        y.append(float(row['classifications correct (percent)']))
plt.subplot(3, 1, 2)
plt.plot(x, y, 'r')
plt.xlabel('instance')
plt.ylabel('percentage of correct')
plt.title('medium volatility')
plt.grid(True)




x = []
y = []

with open('/Users/rl/Desktop/output/high.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row['learning evaluation instances']))
        y.append(float(row['classifications correct (percent)']))
plt.subplot(3, 1, 3)
plt.plot(x, y, 'r')
plt.xlabel('instance')
plt.ylabel('percentage of correct')
plt.title('high volatility')
plt.grid(True)

plt.savefig("test.png")
plt.show()

