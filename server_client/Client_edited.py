import socket
import glob
import os

# pjme = pd.read_csv('PJME_hourly.csv',
#                    index_col=[0], parse_dates=[0])
# # print(pjme.iloc[[2]])
# pjme["delay"] = ""

s = socket.socket()

s.connect(("localhost", 9995))
# print(os.getcwd())
# os.chdir("/Users/arnab/Downloads/SemProject/client_files")
#
# #========================================================================
#
#
# p = 0.02777
# r = 0.25
# total_packs = len(pjme)
# # check = 10
# # while check >= 10:
# # print(np.random.rand(1))
# good = 1
# good_packets = []
# bad_packets = []
# pack_no = 0
# delay = 0
os.chdir("/Users/arnab/Downloads/SemProject/client_files")
#
# while pack_no <= (total_packs-1):
#     if good == 1:
#         print("good packet, processed")
#         good_packets.append(str(pack_no))
#         pjme['delay'][pack_no] = delay
#         pjme.iloc[[pack_no]].to_csv("row" + str(pack_no) + "+.csv")
#         good = np.random.rand(1) > p
#         pack_no = pack_no + 1
#         print(delay)
#         delay = delay + 1
#         # i = i + 1
#     else:
#         bad_packets.append(str(pack_no))
#         print("Bad packet, dropped")
#         good = np.random.rand(1) > (1-r)
#         pack_no = pack_no + 1
#         # i = i + 1
#
# print("End Process")
# print(len(bad_packets))
# print(len(good_packets))
# print(bad_packets)
# f = open("Loss_pattern.txt", 'wb')
# f.writelines((j+"\n").encode("ascii") for j in bad_packets)
# f.close()

for i in glob.glob("*.csv"):

    f = open(i,"rb")
    l = f.read(1024)
    print("Sending data-point"+str(i))
    while(l):
        s.send(l)
        # time.sleep(10)
        l = f.read(1024)

s.close()





