
# Import libraries
# doing all the imports HERE
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read file into dataframe and print
df = pd.read_excel(r'https://www.ers.usda.gov/webdocs/DataFiles/50048/Feed%20Grains%20Yearbook%20Tables-Recent.xlsx?v=3387.1', sheet_name='FGYearbookTable01' )

df

#Rename the Column heads
df.rename({'Table 1--Corn, sorghum, barley, and oats: Planted acreage, harvested acreage, production, yield, and farm price' : 'Commodity', 'Unnamed: 1' : 'Marketing Year', 'Unnamed: 2' : 'Planted acreage\nMillion acres', 'Unnamed: 3' : 'Harvested for grain\nMillion acres', 'Unnamed: 4' : 'Production\nMillion bushels', 'Unnamed: 5' : 'Yield per harvested acre', 'Unnamed: 6' : 'Weighted-average farm price\nMillion bushels 2/', 'Unnamed: 7' : 'Loan rate\ndollars per bushel'}, axis=1, inplace=True)
df
#We need to extract the important datas needed
#extract corn from the data
corn = df.loc[[1,2,3,4,5,6,7,8], :]
corn

#Remove the first column to make the table neat
corn.drop('Commodity', axis=1, inplace=True)
corn


#Extract Sorghum data
sorghum = df.loc[10:17, :]
sorghum

#Refine Sorghum data
sorghum.drop('Commodity', axis=1, inplace=True)
sorghum

#Extract Barley data
Barley = df.loc[19:26, :]
Barley

#Refine Barley data
Barley.drop('Commodity', axis=1, inplace=True)
Barley

#Oats Barley data
Oats = df.loc[28:35, :]
Oats

#Refine Oats data
Oats.drop('Commodity', axis=1, inplace=True)
Oats 

#We want to make a line plot to show the Yield per harvested acre from 2015-2023 for each crop

#Define functions for line plots of the Yield per harvested acre from 2015-2023 for each crop 
def plt_plot(x_data, y_data, label, title, color, xaxes, yaxes):
    
    plt.figure(figsize=(12,8))
    
    for i in range(len(y_data)):
        plt.plot(x_data, y_data[i], label=label[i], color=color[i])
    
    plt.title(title)
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.savefig("plot.png")
    plt.legend(loc='best')
    plt.show()
    
    return
#Declaring the values for the Function
x_data = Oats["Marketing Year"]
y_data = [corn["Yield per harvested acre"], sorghum["Yield per harvested acre"], Barley["Yield per harvested acre"], Oats["Yield per harvested acre"]] 
title = "Yield of Crops in U.S.A from 2015-2022"
label = ["Corn", "Sorghum", "Barley", "Oats"]
color = ['red','blue','green','yellow']
x_label = "Marketing Year"
y_label = "Yield per harvested acre"

plt_plot(x_data, y_data, label, title, color, x_label, y_label)

#Calculate Harvest percent of each crop for each year and add it to the dataset

#Corn Harvest percent
corn["Corn Percent Harvested"] = 100.0 * corn["Harvested for grain\nMillion acres"] / corn["Planted acreage\nMillion acres"]

corn

#Sorghum Harvest percent 
sorghum["Sorghum Percent Harvested"] = 100.0 * sorghum["Harvested for grain\nMillion acres"] / sorghum["Planted acreage\nMillion acres"]

sorghum

#Barley Harvest percent
Barley["Barley Percent Harvested"] = 100.0 * Barley["Harvested for grain\nMillion acres"] / Barley["Planted acreage\nMillion acres"]

Barley

#Oats Harvest percent
Oats["Oats Percent Harvested"] = 100.0 * Oats["Harvested for grain\nMillion acres"] / Oats["Planted acreage\nMillion acres"]
Oats

#Next we show the crop with the highest Harvest Percent for each year using a line plot

#Define fuction of a line plot of the crops Harvest percent for each year
def plt_plot(A, B, label, title, color, xaxes, yaxes):
    
    plt.figure(figsize=(12,8))
    
    for i in range(len(y_data)):
        plt.plot(A, B[i], label=label[i], color=color[i])
    plt.title(title)
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.savefig("plot1.png")
    plt.legend(loc='best')
    plt.show()
    
    return

#Declare the variables for the functions

x_data = Oats["Marketing Year"]
y_data = [corn["Corn Percent Harvested"], sorghum["Sorghum Percent Harvested"], Barley["Barley Percent Harvested"], Oats["Oats Percent Harvested"]] 
title = "Crops Harvest Percentage in U.S.A"
label = ["Corn", "Sorghum", "Barley", "Oats"]
color = ['red','blue','green','yellow']
x_label = "Marketing Year"
y_label = "Crop Harvested (%)"

plt_plot(x_data, y_data, label, title, color, x_label, y_label)

#Next we show the crop with the Highest yield rate for the past 4 years using a Bar chart
#Lets declare the year we will use for our Chart
Year = corn.loc[5:8, 'Marketing Year']
Year

#Yield for each crop

#Declaring yield for each crop
Corn_planted = corn.loc[5:8, 'Planted acreage\nMillion acres']
Sorghum_planted = sorghum.loc[14:17, 'Planted acreage\nMillion acres']
Barley_planted = Barley.loc[23:26, 'Planted acreage\nMillion acres']
Oats_planted = Oats.loc[32:35, 'Planted acreage\nMillion acres']

#Declare yield length
Yield = [corn.loc[5:8, 'Yield per harvested acre'], sorghum.loc[14:17, 'Yield per harvested acre'], Barley.loc[23:26, 'Yield per harvested acre'], Oats.loc[32:35, 'Yield per harvested acre']] 

#Define function for the Multiple Bar Chart
from matplotlib import style

style.use('ggplot')
plt.figure(figsize=(10,6))
barWidth = 0.2

bar1 = np.arange(len(Yield))

plt.bar(bar1, Corn_planted, color='red', width= barWidth, label="Corn")
plt.bar(bar1+0.2, Sorghum_planted, color='yellow', width= barWidth, label="Sorghum")
plt.bar(bar1+0.4, Barley_planted, color='purple', width= barWidth, label="Barley")
plt.bar(bar1+0.6, Oats_planted, color='blue', width= barWidth, label="Oats")
plt.xlabel("Year")
plt.ylabel("Land used per million acre")
plt.savefig("bar.png")
plt.xticks(bar1+0.3,Year)
plt.title('Crops Expanse of land used for planting per million acre for the past four years in U.S.A')
plt.legend()
plt.show()

#Next we will show a descriptive statistics of the Quartile ranges of the crops Harvest percent using a Box plot

#define boxplot function for Harvest percent of each crop  
def plt_boxplot(y_data, label, title, xaxes, yaxes):
    
    plt.figure(figsize=(10,6))
    plt.boxplot(y_data,labels=label)
    plt.title(title)
    plt.savefig("box.png")
    plt.xlabel(xaxes)
    plt.ylabel(yaxes)
    plt.show()
    
    return
#Declaring Variables for our functions

y_data = [corn["Corn Percent Harvested"], sorghum["Sorghum Percent Harvested"], Barley["Barley Percent Harvested"], Oats["Oats Percent Harvested"]] 
label = ["Corn", "Sorghum", "Barley", "Oats"]
title = "Statistics of Quartile ranges of the crops Harvest percent"
x_label = "Crops"
y_label = "Crop Harvested percent"

plt_boxplot(y_data, label, title, x_label, y_label)

#Next We will plot a pie chart to show the year with the Highest percentage Harvest for Oats grain

#Declare Oats percent harvested as Oat
Oat = Oats["Oats Percent Harvested"]

Oat

#Define pie chart function for Oats highest harvest percent marketing year
def piechart(data, labels, title, colors, autopct, shadow, startangle):
    plt.figure(figsize=(10,6))
    plt.pie(data, explode, labels=labels, colors=colors, autopct=autopct, shadow=True, startangle=90)
    plt.title(title)
    plt.show()
    return

#Declaring variables for the function

data = Oat
title = 'Oats Harvest Percentage Marketing Year'
labels = ["2015/16", "2016/17", "2017/18", "2018/19", "2019/20", "2020/21", "2021/22", "2022/23"]
color = ['red', 'green', 'purple', 'yellow', 'violet', 'pink', 'orange', 'blue']
# Creating explode data
explode = (0.2, 0, 0, 0, 0, 0, 0, 0)
autopct='%0.2f%%'
shadow=True
startangle=90
piechart(data, labels, title, color, autopct, shadow, startangle)