#store the costs in a list
costs = [1, 8, 15, 7, 5, 14, 43, 40]
#store the name of olympic name
games = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']
print(costs)

#the bar plotting code was obtained from https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
#set the x and y axis
ax.bar(games, costs)
#set the label of y and the title of the figure
ax.set_ylabel('Cost in $ billions')
ax.set_title('The costs of hosting the Summer Olympic Games from 1984 to 2012')

plt.show()
