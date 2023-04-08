import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([1, 3, 3, 2, 1])
a2 = np.array([1, 1, 2, 2, 1])

plt.plot(a1, a2, linewidth=0, marker=".", markersize=10, color='pink')
plt.ylim(ymin=0, ymax=4)
plt.xlim(xmin=0, xmax=4)
plt.xlabel('x-os')
plt.ylabel('y-os')
plt.title('prvi zadatak')
plt.show()
