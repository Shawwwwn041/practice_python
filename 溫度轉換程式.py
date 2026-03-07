# python 溫度轉換器

unit = input("請輸入現在溫度的單位C/F").strip().upper()
temp = float(input("請輸入現在溫度"))

if unit == 'C':
    temp = temp*9/5+32
    new_unit = 'F'
elif unit == 'F':
    temp = (temp-32)*5/9
    new_unit = 'C'

else:
    print("你的輸入有誤!")
    exit()
print(f"轉換後的溫度{temp:.2f} {new_unit}")