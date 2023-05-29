import pyshark
import datetime

cap = pyshark.FileCapture('../http.cap')

# print(dir(cap)) # Prints all the fields that can be accessed

old_sniff_time = cap[0].sniff_time
time_diff_arr = []
for packet in cap:
    new_sniff_time = packet.sniff_time
    time_diff = (new_sniff_time - old_sniff_time).total_seconds()
    time_diff_arr.append(time_diff)
    print("Time difference between packets at {} and {} = {}".format(old_sniff_time, new_sniff_time, time_diff))
    old_sniff_time = new_sniff_time

print("Avg time between packets = {}".format(sum(time_diff_arr)/len(time_diff_arr)))
