shop = {"回復藥水": 50, "鐵劍": 300, "皮甲": 180, "火把": 20}
total_price = 0
#價格 ≥ 100 的商品打九折，結果用 int() 取整數，存回字典
for commodity,price in shop.items():
    if price >= 100:
        shop[commodity] = int(price*0.9)
#逐筆印出新價格
print(f"商店滿100，打九折！")
for commodity,price in shop.items():
    print(f"{commodity}:{price}元！")
    total_price += price
#印出全部商品的總價
print(f"整間商店所有價格總和:{total_price}")
