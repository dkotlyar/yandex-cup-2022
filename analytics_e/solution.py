import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 1000, 1_000)


def n(X, mean, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-1 / 2 * ((X - mean) / sigma) ** 2)


y1 = n(x, 150, 80)
y2 = n(x, 310, 60)
y3 = n(x, 450, 70)
y4 = n(x, 550, 70)
y5 = n(x, 730, 85)
y6 = n(x, 900, 90)

y = np.vstack((y1, y2, y3, y4, y5, y6)).max(axis=0)

fig = plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.plot(x, y6)
plt.plot(x, y)
plt.show()

best = None
for l1 in np.arange(0, 600 + 1):
    y_l1 = y[l1:l1+200].sum()
    for l2 in np.arange(l1 + 200, 800 + 1):
        y_l2 = y[l2:l2+200].sum()
        total = y_l1 + y_l2
        if best is None or best[0] < total:
            best = total, l1 + 100, l2 + 100

print(best)
