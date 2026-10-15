scores = [("阿光", 88), ("小美", 95), ("大熊", 72), ("靜香", 95), ("胖虎", 60)]
#用切片印出最後兩筆資料
print(scores[-2:])
#找出分數最高的人，不能用 max()。如果同分，取先出現的那個
max_score = 0
max_score_person = ""
for name,score in scores:
    if score > max_score:
        max_score = score
        max_score_person = name
print(f"最高分：{max_score_person} {max_score}分")
#把所有分數收集到 list，由小到大排序後印出
score_all = []
for name,score in scores:
    score_all.append(score)
print(f"{sorted(score_all)}")