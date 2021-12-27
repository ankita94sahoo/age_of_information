import socket
import glob
import os

# pjme = pd.read_csv('PJME_hourly.csv',
#                    index_col=[0], parse_dates=[0])
# # print(pjme.iloc[[2]])
# pjme["delay"] = ""

s = socket.socket()

HOST='192.168.1.89'
PORT=8665

s.connect((HOST,PORT))

os.chdir("./client_files")

for i in glob.glob("*.csv"):

    f = open(i,"rb")
    l = f.read(1024)
    print("Sending data-point"+str(i))
    while(l):
        s.send(l)
        # time.sleep(10)
        l = f.read(1024)

s.close()

print("All sent")





