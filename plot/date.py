import matplotlib.pyplot as plt
from datetime import datetime

readFile = open('data.txt', 'r')
sepFile = readFile.read().split('\n')
readFile.close()

x = []
yz = []
ys = []
for idx, plotPair in enumerate(sepFile):
    time_format = '%d/%m/%Y'
    data = plotPair.split(' ')
    if (data[0] != ''):
        date = datetime.strptime(data[0], time_format).date()
        x.append(date)
        yz.append(data[1])
        ys.append(data[2])

plt.plot_date(x=x, y=yz)
plt.plot_date(x=x, y=ys)
plt.ylim(0, 200)
plt.axhline(135, color='r')
plt.axhline(85, color='b')
plt.show()