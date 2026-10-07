# 字典暖身 10 題
# 日期：2026/10/7
# 練習重點：查值、修改、新增、in、迴圈、.items()、加總、篩選、len()

stock = {"木頭": 10, "石頭": 5, "鐵礦": 2}

# 第 1 題：印出石頭的數量
print(stock["石頭"])

# 第 2 題：木頭用掉 3 個
stock["木頭"] -= 3

# 第 3 題：鐵礦多挖到 1 個
stock["鐵礦"] += 1

# 第 4 題：新增金礦 1 個
stock["金礦"] = 1

# 第 5 題：判斷背包裡有沒有鑽石
if "鑽石" in stock:
    print("有鑽石")
else:
    print("沒有鑽石")

# 第 6 題：印出所有物品名稱
for k in stock:
    print(k)

# 第 7 題：用「名稱:數量」的格式印出每樣物品
for k, v in stock.items():
    print(f"{k}:{v}")

# 第 8 題：計算所有物品的總數量
total = 0
for k, v in stock.items():
    total += v
print(total)

# 第 9 題：找出數量少於 5 的物品，排序後印出
stock_list = []
for k, v in stock.items():
    if v < 5:
        stock_list.append(k)
print(sorted(stock_list))

# 第 10 題：印出總共有幾種物品
stock_count = []
for k in stock:
    stock_count.append(k)
print(f"總共有{len(stock_count)}種")