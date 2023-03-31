import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/15058/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[0:1001:100,1]

#use boolean to correspond Afghanistan
Afgh = []
for a in covid_data["location"]:
    if a == "Afghanistan":
        Afgh.append(True)
    else: 
        Afgh.append(False) 
covid_data.loc[Afgh, "total_cases"]
covid_data.loc[covid_data["date"] == "2020-03-31", ["location", "new_cases", "new_deaths"]]

new_data = covid_data.loc[covid_data["date"] == "2020-03-31", ["new_cases", "new_deaths"]]
#code obtained from https://blog.csdn.net/weixin_42414714/article/details/117200550 
# axis=0 means by columns, axis=1 means by rows
np.average(new_data, axis=0)
#box plot of new cases and new deaths on 31 March 2020
plt.boxplot([new_data["new_cases"],new_data["new_deaths"]],labels=['new cases','new deaths'])
plt.show()

covid_data['date'] = pd.to_datetime(covid_data['date'])
world_data = covid_data[covid_data["location"] == "World"]
world_dates = world_data["date"]
world_new_cases = world_data["new_cases"]
world_new_deaths = world_data["new_deaths"]
plt.plot(world_dates, world_new_cases, 'r-')
plt.plot(world_dates, world_new_deaths, 'b-')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('New Cases and New Deaths')
plt.title('Worldwide New COVID-19 Cases and New COVID-19 Deaths Over Time')
plt.show()
#plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#b+ means symbol "+" in blue, r+ means symbol "+" in red, bo means dots in blue, ".","-" can work too
#plt.plot(world_dates.iloc[0:len(world_dates):4], world_new_cases, 'r-')

#question.txt (How have new cases and total cases developed over time in the UK)
uk_data = covid_data[covid_data["location"] == "United Kingdom"]
uk_new_cases = uk_data["new_cases"]
uk_total_cases = uk_data["total_cases"]
uk_dates = uk_data["date"]
plt.plot(uk_dates, uk_total_cases, 'r-', label="Total cases")
plt.plot(uk_dates, uk_new_cases, 'b-', label="New cases")
plt.xticks(uk_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('Date')
plt.ylabel('New Cases and Total Cases')
plt.title('New COVID-19 Cases and Total COVID-19 Cases Over Time in UK')
plt.legend()
plt.show()