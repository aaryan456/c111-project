import plotly.figure_factory as pf
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df = pd.read_csv("mediumdata.csv")
data = df["reading_time"].tolist()
dataMean = statistics.mean(data)
datastddev = statistics.stdev(data)
print("Mean of the data is {}".format(dataMean))
print("Standard Deviation of the data is {}".format(datastddev))

print("mean of population- ",statistics.mean(data))
def random_set_of_mean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataSet)
    return mean

meanlist = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    meanlist.append(set_of_means)

stddev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)

firststddevStart, firststddevEnd = mean - stddev, mean + stddev
secondstddevStart, secondstddevEnd = mean - (2*stddev), mean + (2*stddev)
thirdstddevStart, thirdstddevEnd = mean - (3*stddev), mean + (3*stddev)

df = pd.read_csv("mediumdata.csv")
data = df["id"].to_list()

meanofsample = statistics.mean(data)
print("Mean of Sampling Distribution", meanOfSample)

fig = pf.create_distplot([meanlist],["Population Mean"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[meanofsample, meanofsample], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
fig.add_trace(go.Scatter(x=[firststddevEnd,firststddevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
fig.show()

zscore = (meanofsample - mean)/stddev
print("z score is: ", zscore)
