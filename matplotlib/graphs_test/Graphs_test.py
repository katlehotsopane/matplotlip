import matplotlib.pyplot as plt

# first figure
#plt.figure()
#plt.axis([0, 6, 0, 20])
#plt.plot([1, 2, 3, 4], [3, 5, 9, 25])
#plt.show()

# second graph
#the difference when (object_orinted approach)
#figure = plt.figure()
#axes = figure.add_subplot()
#axes.set_title("A test line graph")
#axes.plot([1, 2, 3, 4], [3, 5, 9, 25])
#plt.show()

# When Importing multiple subplots
#figure = plt.figure()
#ax1 = figure.add_subplot(1, 2, 1)
#ax2 = figure.add_subplot(1, 2, 2)

#ax1.plot([1, 2, 3, 4], [3, 5, 9, 25])
#ax2.plot([1, 2, 3, 4], [5, 7, 12, 17])
#plt.show()

# Drawing the  pie chart sketch

option_votes = [63, 28, 8]
option_names = [
    "flask",
    "Django",
    "It depends"
]

figure = plt.figure()
axes = figure.add_subplot()

axes.pie(
    option_votes,
    labels=option_names,
    explode=[0.1, 0, 0],
   autopct="%1.1f%%"
)

plt.show()
