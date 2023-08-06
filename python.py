import pandas as pd
import random
import statistics 
import csv
import plotly.figure_factory as ff

data=pd.read_csv("class110.csv")
list_data=data["average"].tolist()

list_set=[]
mean=0
stdv=0
def random_numbers_data():
    for i in range(0,100):
        random_number=random.randint(0,len(data))
        value=list_data[random_number]
        list_set.append(value)


random_numbers_data()

def statistics_function():
   mean=statistics.mean(list_set)
   
   stdv=statistics.stdev(list_set)
   

statistics_function()  

def graph_of_sample():
    fig=ff.create_distplot([data], ['average'], show_hist=False)
    fig.show()
graph_of_sample()