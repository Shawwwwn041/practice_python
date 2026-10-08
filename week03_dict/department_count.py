# 各部門設備數
# 日期：2026/10/7
# 練習重點：用字典數次數、.items()、邊走邊記最小值（不用 min）、len()

devices = [
    ("PC-01", "業務部"),
    ("PC-02", "會計部"),
    ("PC-03", "業務部"),
    ("PC-04", "倉儲部"),
    ("PC-05", "業務部"),
    ("PC-06", "會計部"),
    ("PC-07", "資訊部"),
    ("PC-08", "倉儲部"),
    ("PC-09", "業務部"),
]

# 第 1 題：統計每個部門有幾台設備
device_dict = {}
for pc, dept in devices:
    if dept in device_dict:
        device_dict[dept] += 1
    else:
        device_dict[dept] = 1

# 第 2 題：逐筆印出「部門：幾台」
for k, v in device_dict.items():
    print(f"{k}:{v}台")

# 第 3 題：找出設備最少的部門（不能用 min）
min_count = float('inf')
for dept, count in device_dict.items():
    if count < min_count:
        min_count = count
        min_devices_dep = dept
print(f"設備最少的部門：{min_devices_dep} {min_count}台")

# 第 4 題：印出總共有幾個部門
print(f"總共有{len(device_dict)}個部門")