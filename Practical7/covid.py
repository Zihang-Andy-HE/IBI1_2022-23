import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/15058/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[0:1001:100,1]
covid_data.loc[covid_data["location"] == "Afghanistan", "total_cases"]
covid_data.loc[covid_data["date"] == "2020-03-31", ["location", "new_cases", "new_deaths"]]
new_data = covid_data.loc[covid_data["date"] == "2020-03-31", ["new_cases", "new_deaths"]]
#code obtained from https://blog.csdn.net/weixin_42414714/article/details/117200550 
# axis=0 means by columns, axis=1 means by rows
np.average(new_data, axis=0)
#box plot
plt.boxplot([new_data["new_cases"],new_data['new_deaths']],labels=['new cases','new deaths'])
plt.show()
world_dates = covid_data.loc[:,"date"]
world_new_cases = covid_data.loc[:,"new_cases"]
plt.xticks(rotation=90)
#b+ means symbol "+" in blue, r+ means symbol "+" in red, bo means dots in blue
plt.plot(world_dates, world_new_cases, 'b+')
