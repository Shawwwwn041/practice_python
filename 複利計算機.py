#複利計算機
#總金額 = 本金(1 + (利率 / 100)) ** 時間

amount = 0
amount =  float(input("請輸入本金金額："))
#本金
while amount <= 0:
    print("本金不得為0。")
    amount =  float(input("請輸入本金金額："))

print(f"你的本金為{amount}")

#利率
rate = 0  #利率 = rate
rate = float(input("請輸入銀行的利率"))
while rate <= 0:
    print("利率不得為0。")
    rate = float(input("請輸入銀行的利率"))

print(f"你的利率為:{rate}。")

#時間
time = 0
time =  float(input("請輸入你想要的存放時間："))
while time <= 0:
    print("時間不得為0。")
    time =  float(input("請輸入你想要的存放時間："))
print(f"你的時間為:{time}。")
#總額
total = amount*(1 + (rate / 100)) ** time
print(f"你的定存金額預估為:{round(total)}")