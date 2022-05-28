from asyncore import read
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print(population_mean)

def random_set_of_mean():
    dataset = []
    for i in range(0,30):
        random_index=random.randint(1,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

mean_list = []
for i in range(0,100):
    set_of_means=random_set_of_mean()
    mean_list.append(set_of_means)

std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_dev)

first_std_deviation_start, first_std_deviation_end = mean-std_dev, mean+std_dev
second_std_deviation_start, second_std_deviation_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_dev), mean+(3*std_dev)

df = pd.read_csv("sample_2.csv")
data = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)

fig = ff.create_distplot([mean_list],["reading time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.4], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0,1.4], mode="lines", name="MEAN OF STUDENTS WITH NEW READING TIME"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 1.4], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


z_score = (mean - mean_of_sample2)/std_dev
print("The z score is = ",z_score)