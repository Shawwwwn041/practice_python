devices = {"PC-01": "業務部", "PC-02": "會計部", "PC-03": "倉儲部"}
queries = ["PC-02", "PC-07", "PC-01"]
none_queries = 0
for number in queries:
    if number in devices:
        print(f"{number}:{devices[number]}")
    else:
        print(f"{number}:查無此設備")
        none_queries +=1
print(f"查不到的設備：{none_queries} 台")