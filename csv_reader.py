#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
a = []
for i in range(0, 1):
    file_name = "Result_Latency#P1-0_P2-{0}.csv".format(i)
    with open(file_name,'r') as f:
        dataReader = csv.reader(f)
        for row in dataReader:
            print(row)
            a.append(row)
for i in range(0, len(a)):
    a[i][0] = int(a[i][0])
    a[i][1] = int(a[i][1])
#print(type(a[0][0]))
print(a)
