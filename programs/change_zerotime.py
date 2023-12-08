#!/usr/bin/python3
# encoding utf-8

INPUT_FILE = input("Input ATL file name: ")
OUTPUT_FILE = "rep{}".format(INPUT_FILE)
atl_file = open(INPUT_FILE, 'r')
zeros = []
data = []

for line in atl_file:
    line = line.strip()
    if "ZERO TIME....." in line.split(":"):
        zero_time = line.split(":")[1]
        zero_time_float = float(zero_time.split()[0])
        zeros.append(zero_time_float)
    if "DATA:" in line:
        data_line = float((atl_file.readline()).split()[0])
        data.append(data_line)
atl_file.close()
zero_JDs = []
for item in range(len(zeros)):
    JD = zeros[item] + data[item]
    if JD > 2500000:
        JD = JD - 50000
    zero_JD = JD - data[item]
    zero_JDs.append(zero_JD)
    item += 1

# print(zeros)  # raw zero time
# print(zero_JDs)  # corrected zero time
n = 0
with open(OUTPUT_FILE, 'w') as writedata:
    with open(INPUT_FILE, 'r') as filedata:
        for line in filedata:
            line = line.strip()
            zero_before = "ZERO TIME.....: {}".format(zeros[n])
            zero_after = "ZERO TIME.....: {}".format(zero_JDs[n])
            if "ZERO TIME.....:" in line:
                # print(n)
                new_line = line.replace(zero_before, zero_after)
                if n < len(zeros)-1:
                    n += 1
                else:
                    pass
                writedata.write(new_line+'\n')
            elif "ZERO TIME.....:" not in line:
                writedata.write(line+'\n')
