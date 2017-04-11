# Use the following data for this assignment:
%matplotlib notebook

import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(33500,150000,3650), 
                   np.random.normal(41000,90000,3650), 
                   np.random.normal(41000,120000,3650), 
                   np.random.normal(48000,55000,3650)], 
                  index=[1992,1993,1994,1995])
df = df.T


# first we need to get mean values and confidence intervals
means = []
intervalls = []
colors = []

ind = np.arange(len(df.columns))
yval = 39000;

for column in df:
    mu = np.mean(df[column])
    Cmin, Cmax = stats.norm.interval(0.95, loc=mu, scale=np.std(df[column])/np.sqrt(df[column].size))
    intervalls.append(mu - Cmin)
    means.append(np.mean(df[column]))
    if yval > Cmax:
        colors.append((0.0,0.0,0.5))
    elif yval < Cmin:
        colors.append((0.5,0.0,0.0))
    elif yval == mu:
        colors.append((0.0,0.0,0.0))
    elif yval > mu:
        cfactor = (yval - mu) / (mu - Cmin) 
        colors.append((0 ,0.0,1-cfactor*0.3))
    elif yval < mu:
        cfactor = (mu - yval)/ (mu - Cmin)
        colors.append((1-cfactor*0.3,0.0,0.0))

width = 0.6       # the width of the bars
fig, ax = plt.subplots()
meanplot = ax.bar(ind, means, width, color=colors, yerr=intervalls,capsize=20,ecolor ='k')
# add some text for labels, title and axes ticks
#ax.set_ylabel('Y values')
#ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
#ax.set_xticklabels( ('1992', '1993', '1994', '1995'))
ax.set_xticklabels(list(df))
lhor = plt.axhline(y=yval, color='k', linestyle='--')
plt.gca().set_title('Evaluation of probabalistic data with yval at {}'.format(yval))

def onclick(event):
    means = []
    intervalls = []
    colors = []
    #plt.axhline(y=event.ydata)
    yval = event.ydata
    lhor.set_ydata(event.ydata)
    for column in df:
        mu = np.mean(df[column])
        Cmin, Cmax = stats.norm.interval(0.95, loc=mu, scale=np.std(df[column])/np.sqrt(df[column].size))
        intervalls.append(mu - Cmin)
        means.append(np.mean(df[column]))
        if yval > Cmax:
            colors.append((0.0,0.0,0.5))
        elif yval < Cmin:
            colors.append((0.5,0.0,0.0))
        elif yval == mu:
            colors.append((0.0,0.0,0.0))
        elif yval > mu:
            cfactor = (yval - mu) / (mu - Cmin) 
            colors.append((0 ,0.0,1-cfactor*0.3))
        elif yval < mu:
            cfactor = (mu - yval)/ (mu - Cmin)
            colors.append((1-cfactor*0.3,0.0,0.0))
    plt.gca().set_title('Evaluation of probabalistic data with yval at {}'.format(yval))
    ax.bar(ind, means, width, color=colors, yerr=intervalls,capsize=20,ecolor ='k')
    plt.gcf().canvas.draw()
    

plt.gcf().canvas.mpl_connect('button_press_event', onclick)
#print(colors)