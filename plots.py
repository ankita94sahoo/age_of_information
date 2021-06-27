# -*- coding: utf-8 -*-
"""Plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nx1U7k4vI19Yu-k3vIFCFarKUNEkl6Y3
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# df= pd.read_excel("/content/drive/MyDrive/Matrix.xlsx")

# df.head()

data = {
    "Random_delay_interval":['0','10','17','24','30'],
    "Mean_absolute_error":['16.51','17.94','19.01','18.32','22.67']
}
df = pd.DataFrame (data, columns = ['Random_delay_interval','Mean_absolute_error'])

df.head()

df.dtypes

data_1 = {
    "Random_delay_interval":['0','10','17','24','30'],
    "Mean_absolute_error":['16.51','21.79','23.86','23.97','17.42']
}
df_1 = pd.DataFrame (data_1, columns = ['Random_delay_interval','Mean_absolute_error'])

df_1.head()

x = df['Random_delay_interval'].astype(int)
y = df['Mean_absolute_error'].astype(float)

y2 = df_1['Mean_absolute_error'].astype(float)



plt.figure(figsize=(10,10))
plt.xlabel("Delay_interval")
plt.ylabel("Mean_absolute_error")

plt.title("Random Delay effects on Dataset")

# plt.plot(x,y,".--",color="red")
plt.plot(x, y, color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
plt.plot(x,y2, color="blue", marker='*', linestyle='dashed',linewidth=2, markersize=16)

plt.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"]) #training with delayed dataset and testing with fresh dataset

data_2 = {
    "Static_delay_interval":['5','10','20','30'],
    "Mean_absolute_error":['19.13','23.79','20.96','20.39'] 
}
df_2 = pd.DataFrame (data_2, columns = ['Static_delay_interval','Mean_absolute_error'])

df_2.head()

data_3 = {
    "Static_delay_interval":['5','10','20','30'],
    "Mean_absolute_error":['22.08','24.28','17.58','22.71'] 
}
df_3 = pd.DataFrame (data_3, columns = ['Static_delay_interval','Mean_absolute_error'])

df_3.head()

x1 = df_2['Static_delay_interval'].astype(int)
y1 = df_2['Mean_absolute_error'].astype(float)

y3 = df_3['Mean_absolute_error'].astype(float)

plt.figure(figsize=(10,10))
plt.xlabel("Delay_interval")
plt.ylabel("Mean_absolute_error")

plt.title("Static Delay effects on Dataset")



# plt.plot(x1,y1,".--",color="red")
# plt.plot(x1,y3,"+--",color="blue")


plt.plot(x1,y1,color="green", marker='*', linestyle='dashed',linewidth=2, markersize=16)
plt.plot(x1,y3,color="brown", marker='+', linestyle='dashed',linewidth=2, markersize=18)


plt.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"]) #training with delayed dataset and testing with fresh dataset

data_4 = {
    "Uniform_delay_interval":['0','5','10','20'],
    "Mean_absolute_error":['16.5','16.52','17.96','18.94'] 
}
df_4 = pd.DataFrame (data_4, columns = ['Uniform_delay_interval','Mean_absolute_error'])

data_5 = {
    "Uniform_delay_interval":['0','5','10','20'],
    "Mean_absolute_error":['16.5','19.07','21.92','24.12'] 
}
df_5 = pd.DataFrame (data_5, columns = ['Uniform_delay_interval','Mean_absolute_error'])

x4 = df_4['Uniform_delay_interval'].astype(int)
y4 = df_4['Mean_absolute_error'].astype(float)

y5 = df_5['Mean_absolute_error'].astype(float)

plt.figure(figsize=(10,10))
plt.xlabel("Delay_interval")
plt.ylabel("Mean_absolute_error")

plt.title("Uniform Delay effects on Dataset")



# plt.plot(x1,y1,".--",color="red")
# plt.plot(x1,y3,"+--",color="blue")


plt.plot(x4,y4,color="blue", marker='*', linestyle='dashed',linewidth=2, markersize=16)
plt.plot(x4,y5,color="red", marker='+', linestyle='dashed',linewidth=2, markersize=18)


plt.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"]) #training with delayed dataset and testing with fresh dataset

f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True,figsize=(15,15))


ax1.plot(x, y, color='red', marker='o', linestyle='dashed',linewidth=2, markersize=12)
ax1.plot(x,y2, color="blue", marker='*', linestyle='dashed',linewidth=2, markersize=16)
ax1.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"])
ax1.set_title("Random Delay effects on Dataset")

ax2.plot(x1,y1,color="red", marker='*', linestyle='dashed',linewidth=2, markersize=16)
ax2.plot(x1,y3,color="blue", marker='+', linestyle='dashed',linewidth=2, markersize=18)
ax2.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"])
ax2.set_title("Static Delay effects on Dataset")

ax3.plot(x4,y4,color="red", marker='*', linestyle='dashed',linewidth=2, markersize=16)
ax3.plot(x4,y5,color="blue", marker='+', linestyle='dashed',linewidth=2, markersize=18)
ax3.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"])
ax3.set_title("Uniform Delay effects on Dataset")

# plt.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"]) #training with delayed dataset and testing with fresh dataset

# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=0.5)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

data_6 = {
    "Number_of_packets_dropped":['0','13952','29412','73172'],
    "Mean_absolute_error":['16.51','21.47','21.66','21.80'] 
}
df_6 = pd.DataFrame (data_6, columns = ['Number_of_packets_dropped','Mean_absolute_error'])

x6 = df_6['Number_of_packets_dropped'].astype(int)
y6 = df_6['Mean_absolute_error'].astype(float)

# y3 = df_3['Mean_absolute_error'].astype(float)

plt.figure(figsize=(10,10))
plt.xlabel("Number_of_packets_dropped")
plt.ylabel("Mean_absolute_error")

plt.title("Performance of Model when packets are dropped")



# plt.plot(x1,y1,".--",color="red")
# plt.plot(x1,y3,"+--",color="blue")


plt.plot(x6,y6,color="green", marker='*', linestyle='dashed',linewidth=2, markersize=16)
# plt.plot(x1,y3,color="brown", marker='+', linestyle='dashed',linewidth=2, markersize=18)


# plt.legend(["Train:Delayed Test:Fresh","Train:Fresh Test:Delayed"]) #training with delayed dataset and testing with fresh dataset

#case 1 - Train delayed and test delayed
total_packets = 145367
data_ms_1 = {
    "Percentage_of_packets_dropped":[14440*100/total_packets,29340*100/total_packets,72240*100/total_packets],
    "Mean_absolute_error":[21.54,21.66,21.66] 
}
df_ms_1 = pd.DataFrame (data_ms_1, columns = ['Percentage_of_packets_dropped','Mean_absolute_error'])

df_ms_1.head()

data_sec_1 = {
    "Percentage_of_packets_dropped":[14440*100/total_packets,29340*100/total_packets,72240*100/total_packets],
    "Mean_absolute_error":[21.60,21.66,21.66] 
}
df_sec_1 = pd.DataFrame (data_sec_1, columns = ['Percentage_of_packets_dropped','Mean_absolute_error'])

df_sec_1.head()

f, (ax1) = plt.subplots(1, sharex=True, sharey=True,figsize=(10,10))

plt.yticks(np.arange(min(y_sec_1)-1, max(y_sec_1)+1, 0.01))

x_ms_1 = df_ms_1['Percentage_of_packets_dropped']
y_ms_1 = df_ms_1['Mean_absolute_error']

y_sec_1 = df_sec_1['Mean_absolute_error']

plt.xlabel("Percentage of packets dropped")
plt.ylabel("Mean_absolute_error")

ax1.bar(x_ms_1+0.00, y_ms_1, color='red', width=2.5)
ax1.bar(x_ms_1+2.5,y_sec_1, color="blue", width=2.5)
ax1.set(ylim=[21.4, 21.69])
ax1.legend(["Delay in MilliSeconds","Delay in Seconds"],loc="upper right",)
ax1.set_title("Train on Delayed and Test on Delayed")

#case 2 - Train delayed and test fresh
total_packets = 145367
data_ms_2 = {
    "Percentage_of_packets_dropped":[14440*100/total_packets,29340*100/total_packets,72240*100/total_packets],
    "Mean_absolute_error":[16.49,16.55,16.62] 
}
df_ms_2 = pd.DataFrame (data_ms_2, columns = ['Percentage_of_packets_dropped','Mean_absolute_error'])

df_ms_2.head()

data_sec_2 = {
    "Percentage_of_packets_dropped":[14440*100/total_packets,29340*100/total_packets,72240*100/total_packets],
    "Mean_absolute_error":[16.52,16.56,16.59] 
}
df_sec_2 = pd.DataFrame (data_sec_2, columns = ['Percentage_of_packets_dropped','Mean_absolute_error'])

df_sec_2.head()

f, (ax1) = plt.subplots(1, sharex=True, sharey=True,figsize=(10,10))

plt.yticks(np.arange(min(y_sec_2)-1, max(y_sec_2)+1, 0.01))

ax1.set(ylim=[16.45, 16.65])

x_ms_2 = df_ms_2['Percentage_of_packets_dropped']
y_ms_2 = df_ms_2['Mean_absolute_error']

y_sec_2 = df_sec_2['Mean_absolute_error']

plt.xlabel("Percentage of packets dropped")
plt.ylabel("Mean_absolute_error")

ax1.bar(x_ms_2+0.00, y_ms_2, color='red', width=2.5)
ax1.bar(x_ms_2+2.5,y_sec_2, color="blue", width=2.5)

ax1.legend(["Delay in MilliSeconds","Delay in Seconds"],loc="upper right",)
ax1.set_title("Train on Delayed and Test on Delayed")

#case 3 - Train Fresh and Test Delayed
total_packets = 145367
data_ms_3 = {
    "Percentage_of_packets_dropped":[14440*100/total_packets,29340*100/total_packets,72240*100/total_packets],
    "Mean_absolute_error":[21.52,21.56,21.45] 
}
df_ms_3 = pd.DataFrame (data_ms_3, columns = ['Percentage_of_packets_dropped','Mean_absolute_error'])
df_ms_3.head()

data_sec_3 = {
    "Percentage_of_packets_dropped":[14440*100/total_packets,29340*100/total_packets,72240*100/total_packets],
    "Mean_absolute_error":[21.54,21.56,21.46] 
}
df_sec_3 = pd.DataFrame (data_sec_3, columns = ['Percentage_of_packets_dropped','Mean_absolute_error'])
df_sec_3.head()

f, (ax1) = plt.subplots(1, sharex=True, sharey=True,figsize=(10,10))

ax1.set(ylim=[21.44, 21.57])

x_ms_3 = df_ms_3['Percentage_of_packets_dropped']
y_ms_3 = df_ms_3['Mean_absolute_error']

y_sec_3 = df_sec_3['Mean_absolute_error']
plt.yticks(np.arange(min(y_ms_3)-1, max(y_ms_3)+1, 0.01))

plt.xlabel("Percentage of packets dropped")
plt.ylabel("Mean_absolute_error")

ax1.bar(x_ms_3+0.00, y_ms_3, color='red', width=2.5)
ax1.bar(x_ms_3+2.5,y_sec_3, color="blue", width=2.5)

ax1.legend(["Delay in MilliSeconds","Delay in Seconds"],loc="upper right",)
ax1.set_title("Train on Fresh and Test on Delayed")











