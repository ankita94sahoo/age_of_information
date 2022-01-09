import pandas as pd
import os
import numpy as np

#Load dataframe

data = pd.read_csv('./dataset/coinbaseUSD_1-min_data_2014-12-01_to_2018-11-11.csv.zip',
                   index_col=[0], parse_dates=[0])
data["delay"] = ""
data= data.reset_index()
print(len(data))
print(os.getcwd())
# ========================================================================
#Implement Loss pattern using Gilber-Elliot Model

#If p is the probability of transferring from Good State to the bad state
#and if r is the probability of transferring from the bad state to the Good
#state,

# p = 0.02777
# r = 0.25
# p = 0.05
# r = 0.2

p = 0.3
r = 0.2

total_packs = len(data)
good = 1
good_packets = []
bad_packets = []
pack_no = 0
delay = 0

os.chdir("./server_client/client_files")

while pack_no <= (total_packs - 1):
    if good == 1:
        print("good packet, processed")
        good_packets.append(str(pack_no))
        data.loc[pack_no,'delay'] = delay
        data.iloc[[pack_no]].to_csv("row" + str(pack_no) + "+.csv")
        good = np.random.rand(1) > p
        pack_no = pack_no + 1
        print(pack_no)
        delay = delay + 1
        # i = i + 1
    else:
        bad_packets.append(str(pack_no))
        print("Bad packet, dropped")
        good = np.random.rand(1) > (1 - r)
        pack_no = pack_no + 1
        # i = i + 1

print("End Process")
print(len(bad_packets))
print(len(good_packets))
# print(bad_packets)
f = open("Loss_pattern.txt", 'wb')
f.writelines((j + "\n").encode("ascii") for j in bad_packets)
f.close()


# 1. change parameters such that more than half of the packets are dropped
# (both with delay and without delay)--> generate new received file on server
# 2. remove delay and get received file on server for 1. old values, 2. new values
