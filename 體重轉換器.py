#python 體重轉換器

weight = float(input("請輸入你的實際體重: "))
unit = input("請輸入你體重單位 KG/LB: ").strip().upper()

if unit == 'KG':
    weight *= 2.2
    new_unit = 'LB'
elif unit == 'LB':
    weight /= 2.2
    new_unit = 'KG'
else:
    print("你的單位有誤!")
    exit()

print(f"換算結果為 {weight:.2f} {new_unit}")
