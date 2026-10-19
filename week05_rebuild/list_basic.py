devices = ["PC-01", "PC-02", "PC-03", "PC-04", "PC-05"]

#印出第一台和最後一台
devices_first = devices[0]
devices_last = devices[-1]
print(devices_first)
print(devices_last)
#把 "PC-03" 改成 "PC-03(維修中)"
devices[2] = "PC-03(維修中)"
print(devices[2])
#在最後面新增 "PC-06"，印出整個清單
devices.append("PC-06")
print(devices)
#印出總共幾台
print(len(devices))
#用切片印出最後三台
print(devices[-3:])