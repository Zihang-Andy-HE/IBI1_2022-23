import matplotlib.pyplot as plt
#create the dictionary which contain all the data
results_dic = {'Comedy':73,'Action':42,'Romance':38,'Fantasy':28,'Science-fiction':22,'Horror':19,'Crime':18,'Documentary':12,'History':8,'War':7}
# create a variable called genre of requested genre which can be modified
genre = 'Comedy'
# num store the numbers of students for which the given genre is their favorite
num = results_dic[genre]
print(num)
allgenres = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
allnum = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
#the pie plotting code obtained from https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
#function plt.subplots returns two variables figure and axes
fig, ax = plt.subplots()
#input numbers labels and display the percent value
ax.pie(allnum, labels=allgenres, autopct='%1.1f%%')

plt.show()
