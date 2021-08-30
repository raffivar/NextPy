import matplotlib.pyplot as plt

labels = 'Bluffy', 'Amitloaf', 'Supercat'
sizes = [222, 111, 25]
colors = ['gold', 'yellowgreen', 'lightcoral']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.f%%')
plt.show()
