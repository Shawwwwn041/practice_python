users = {"小王": "業務部", "小李": "會計部", "小陳": "業務部", "小林": "資訊部"}
#把所有業務部的人收集到 list，印出 list 和人數
dep_list = []
for name,dep in users.items():
    if dep =="業務部":
        dep_list.append(name)
print(f"有{dep_list}總共有{len(dep_list)}人")