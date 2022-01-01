import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['auto', 'ball_tree', 'kd_tree', 'brute']
men_means = [75.3 , 75.7, 75.5, 75.3]
women_means = [74.5 , 78.1, 70.5, 74.7]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Manhattan')
rects2 = ax.bar(x + width/2, women_means, width, label='Euclidean')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Testing accuracy %')
ax.set_xlabel('Algorithm')
ax.set_title('The comparison of manhattan and euclidean distance')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()

        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
ax.set_xlim([-1,5])
plt.show()