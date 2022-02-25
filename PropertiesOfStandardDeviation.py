import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

diceResult = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1+dice2)

mean = sum(diceResult)/len(diceResult)
print("Mean of the data is {} ".format(mean))

median = statistics.median(diceResult)
print("Median of the data is {} ".format(median))

mode = statistics.mode(diceResult)
print("Mode of the data is {} ".format(mode))

standardDeviation = statistics.stdev(diceResult)
print("Standard Deviation is {}".format(standardDeviation))

first_std_dev_start,first_std_dev_end = mean-standardDeviation,mean+standardDeviation
second_std_dev_start,second_std_dev_end = mean-(2*standardDeviation),mean+(2*standardDeviation)
third_std_dev_start,third_std_dev_end = mean-(3*standardDeviation),mean+(3*standardDeviation)

list_of_data_within_1std_dev=[result for result in diceResult if result > first_std_dev_start and result < first_std_dev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1std_dev)*100.0/len(diceResult)))

list_of_data_within_2std_dev=[result for result in diceResult if result > second_std_dev_start and result < second_std_dev_end]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2std_dev)*100.0/len(diceResult)))

list_of_data_within_3std_dev=[result for result in diceResult if result > third_std_dev_start and result < third_std_dev_end]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3std_dev)*100.0/len(diceResult)))

fig = ff.create_distplot([diceResult],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()