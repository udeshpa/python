import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0,5,11)
y = x ** 2
plt.plot(x,y, 'r-')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.show()

plt.subplot(1,2,1)
plt.plot(x,y, 'r')
plt.subplot(1,2,2)
plt.plot(y,x, 'b')

plt.show()


#object oriented
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')
plt.show()


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes2.plot(y,x)
axes1.set_title('Larger')
axes2.set_title('Smaller')
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2)

for current_axe in axes:
    current_axe.plot(x,y)

plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(3,2), dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
plt.show()

fig, axes = plt.subplots(figsize=(8,2), nrows=2, ncols=1)
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
fig.savefig('my_picture.jpg', dpi=200)
plt.show()


fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x, x**2, label='X Squares')
axes.plot(x, x**3, label='X Cubed')
axes.legend(loc=10)
plt.show()


fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y, color='green')
plt.show()

fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y, color='#FF8C00', linewidth=10, alpha=0.5, linestyle='-.', marker='o', markersize=10,
          markerfacecolor='blue', markeredgewidth=3)
axes.set_xlim([0,4])
axes.set_ylim([0,7])
plt.show()


from random import sample
data = sample(range(1,1000), 100)
plt.hist(data)
plt.show()
