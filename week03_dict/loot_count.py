# 掉寶統計
# 日期：2026/10/8
# 練習重點：用字典數次數、.items()、邊走邊記最大值（不用 max）

drops = ["史萊姆凝膠", "鐵礦", "史萊姆凝膠", "金幣", "鐵礦", "史萊姆凝膠"]

# 第 1 題：用字典統計每種寶物掉了幾個
drops_dict = {}
for treasure in drops:
    if treasure in drops_dict:
        drops_dict[treasure] += 1
    else:
        drops_dict[treasure] = 1

# 第 1 題：逐筆印出
# 第 2 題：同一個迴圈裡，邊走邊記掉最多的寶物（不能用 max）
drops_max = 0
drops_max_treasure = ""
for treasure, count in drops_dict.items():
    print(f"{treasure}：{count} 個")
    if count > drops_max:
        drops_max = count
        drops_max_treasure = treasure

print(f"掉最多：{drops_max_treasure}（{drops_max} 個）")


