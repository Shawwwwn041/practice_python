bag = {"藥水": 3, "鐵劍": 1}
loot = ["藥水", "木盾", "藥水", "金幣", "木盾"]
bag_list = []
for equip in loot:
    if equip in bag:
        bag[equip] += 1
    else:
        bag[equip] = 1

bag["藥水"] -= 2 #戰鬥使用掉

print(bag) #印出背包
for k,v in bag.items():
    if v >= 2:
        bag_list.append(k)
print(sorted(bag_list))