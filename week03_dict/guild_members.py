guild = {"阿光": 25, "小美": 32, "大熊": 40, "胖虎": 18}
#阿光升了 6 級
guild["阿光"] += 6
#新成員「靜香」加入，等級 1
guild["靜香"] = 1
#胖虎退出公會，從字典刪掉
del guild["胖虎"]
#印出等級 ≥ 30 的成員和等級
for member,level in guild.items():
    if level >= 30:
       print(f"{member}:{level}級")
#印出公會現在有幾個人
print(f"共有{len(guild)}位")