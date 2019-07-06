import matplotlib.pyplot as plt
import numpy as np
#data = np.arange(10)
#print(data)

#plt.plot([1.5,3.5,-2,1.6])


fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.plot(np.random.randn(100).cumsum(),'k--')

_=ax1.hist(np.random.randn(100),bins=20,color='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
ax3.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
plt.show()