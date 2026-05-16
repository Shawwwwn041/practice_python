#CH4 Practice

#<1>冷暖氣開關判斷
#氣溫高於28度可開冷氣
#氣溫低於15度可開暖氣
"""
temp = float(input("請輸入室內溫度："))
if temp >= 28:
    print("可開冷氣！")
elif temp <= 15:
    print("可開暖氣！")
else :
    print("不開冷暖氣！")

#<2> "判別奇偶數"
num = int(input("請輸入數字"))
if num % 2 != 0:
    print("這是奇數")
elif num % 2 == 0:
    print("這是偶數")
elif num == 0:
    print("數字不得為0")
else :
    print("請重新輸入！")

while True :
    try:
        num = int(input("請輸入數字："))
        if num == 0:
            print("數字不得為0")
        elif num % 2 != 0:
            print("這是奇數")
            break
        elif num % 2 == 0:
            print("這是偶數")
            break
        else :
            print("請重新輸入！")
    except ValueError:
        print("錯誤！請輸入純數字，不要輸入文字或其他符號。")


#<3> "閏年or平年"
#閏年：year能被400整除，或year能被4整除但不能被100整除
year_1 = int(input("輸入年分："))
if (year_1 % 400 == 0) or (year_1 % 4 == 0 and year_1 % 100 != 0):
    print(f"{year_1}是閏年")
else :
    print(f"{year_1}是平年")

#<4> "判別三角形是否成立"
#三角形成立條件：兩邊的和 > 第三邊
s1 = int(input("請輸入一邊長"))
s2 = int(input("請輸入一邊長"))
s3 = int(input("請輸入一邊長"))

if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print(f"({s1},{s2},{s3})是三角形")
else :
    print(f"({s1},{s2},{s3})不是三角形")

# <5>：成績等級
# 成績分為五個等級：
# grade >= 90：A
# 90 > grade >= 80 ： B
# 80 > grade >= 70 ： C
# 70 > grade >= 60 ： D
# grade < 60 ： F

grade = int(input("請輸入成績："))

if grade >= 90 :
    print(f"{grade}分，等級為 A！")
elif grade >= 80:
    print(f"{grade}分，等級為 B！")
elif grade >= 70:
    print(f"{grade}分，等級為 C！")
elif grade >= 60:
    print(f"{grade}分，等級為 D！")
elif grade < 60:
    print(f"{grade}分，等級為 F！")

# <6>： 三數比大小
#輸入三個數比大小，並按照大小順序排列
n1 = int(input("請輸入數字"))
n2 = int(input("請輸入數字"))
n3 = int(input("請輸入數字"))

if n1 > n2 :
     n1,n2 = n2,n1 
if n2 > n3 :
     n2,n3 = n3,n2
if n1 > n2 :
    n1,n2 = n2,n1  

print(f"由小排到大：{n1},{n2},{n3}")

#<7>

#<a>
print('5為奇數') if 5 % 2 == 1 else print('5為偶數')


#<b>
x,y = 6,3
z = x if x > y else y

#<c>
x = [5,6,4]
print('x is not empty') if x else print('x is empty')

#<d>
x = -x
x = -x if x < 0 else x


#<8>
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]

season = int(input("請輸入月份換算季節："))

if season in spring :
    print("現在是春季")
elif season in  summer :
    print("現在是夏季")
elif season in  autumn :
    print("現在是秋季")
elif season in  winter :
    print("現在是冬季")


#<9>
while True :
    try :
        sec = int(input("輸入秒數換算(上限86400秒)："))
        if sec > 86400 :
            print("輸入過大，請重新輸入")
        else :
            hours = sec // 3600
            mins = (sec%3600) // 60
            seconds = sec % 60 
            print(f"{sec}秒換算結果為->{hours}小時{mins}分鐘{seconds}秒")
            break
    except ValueError:
        print("輸入格式錯誤，請重新輸入!")


#<10>計算停車費
hour  = int(input("車子已停多久？"))
if hour <= 12 :
    parking_price = hour * 40
else :
    new_hour = hour - 12
    parking_price = (12 * 40) + (new_hour * 30)

print(f"停車{hour}小時，酌收{parking_price}元!")

#<11> 畢氏定理
#兩個短邊平方和等於斜邊平方

while True :
    try:
        a = int(input("請輸入a邊線長度："))
        b = int(input("請輸入b邊線長度："))
        c = int(input("請輸入斜邊長度："))
        if c < a and c < b :
            print("請重新輸入斜邊長。")
        elif (a*a + b*b) == (c*c) :
            print("為直角三角形!")
            break
        elif (a + b) > c :
            print("為三角形，但不是直角三角形")
            break
        else :
            print("不是三角形")
            break
    except(ValueError):
        print("偵測不是數字，請重新輸入")

#<12>找零錢
#
while True:
    pay = int(input("客人付款金額：")) 
    price  = int(input("購買商品價格："))
    if pay < price :
        lost_change = price - pay
        print(f"金額不足，需補{lost_change}元！")
    elif pay == price :
        print("金額足夠！謝謝光臨")
        break
    else :
        change = pay - price
        one_thousand_dollar = change // 1000
        change = change % 1000
        one_hundred_dollar = change // 100
        change = change % 100
        fifty_dollar = change // 50
        change  = change % 50
        ten_dollar = change //10
        change = change % 10
        five_dollar = change //5
        change = change % 5
        one_dollar = change
        print(f"需找{one_thousand_dollar}張1000元\n{one_hundred_dollar}張100元\n{fifty_dollar}個50元\n{ten_dollar}個10元\n{five_dollar}個5元\n{one_dollar}個1元")
        break

# 2.迴圈
#<13>階乘
# 5的階乘 = 1*2*3*4*5
n = int(input("請輸入要階乘的數字"))
total = 1
for i in range(1, n + 1):
    total = total * i

print(f"{n} 的階乘結果為：{total}")

 #<14> 多少個閏年

total = 0  

for i in range(1,2026):
    if i % 400 == 0 or i % 4 == 0 and i % 100 != 0  :
        total += 1

print(f"到今年為止有{total}個閏年") 

#<15>
while True :
    a = int(input("輸入一個數"))
    b = int(input("輸入一個數"))
    gcd = 0 
    if a >= b :
        print("輸入錯誤，請重新輸入")
    else :
            for c in range(1, a + 1) :
                if a % c ==0 and b % c == 0 :
                    gcd = c
            print(f"{a}和{b}的最大公因數為：{gcd}")
            break


#<16>

#(a)
row = 5

for i in range(1,row + 1) :
    for y in range(row,i - 1,-1): 
        print('*', end='')
    print()  # 換行
#另一種簡單的寫法

for i in range(5,0,-1):
    print('*' * i)

#<b>
row = 5 
for i in range(1,row+1) :
    for s in range(row - i):
        print(' ', end='')
    for y in range(1, i + 1):
        print('*',end= '')
    print()

for i in range(1, 6):

#<c>
row = 5
for i in range(1,row +1) :
    for s in range(1,i) :
        print(" ",end='')
    for y in range(row, i - 1,-1) :
        print('*',end='')
    print()

#<d>
row = 5
for i in range(1,row +1) :
    for s in range(1,i) :
        print("^",end='')
    for y in range(row, i - 1,-1) :
        print('*',end='')
    print()

#<e>
row = 5
for i in range(1,row + 1) :
    for y in range(1,i + 1) :
        print(y,end = "")
    print()

#<f>
row = 5
for i in range (1,row + 1) :
    for y in range (row,row - i,-1) :
        print(y,end ='')
    print()

# <g>
row = 5
for i in range(1,row + 1,1) :
    for y in range(1,i + 1) :
        print(i,end='')
    print()

#<h>
row = 5
count = 0
for i in range(1, row + 1 ) :
    for y in range(1 , i + 1) :
        print(f"{count:x}", end='')
        count += 1
    print()

#<17>
#<a>
row = 5

for i in range(row,0, -1) :
    for y in range(i,row + 1) :
        print(y,end='')
    print() 

#<b>
row = 5

for i in range(row,0, -1) :
    for y in range(1,i + 1) :
        print(y,end='')
    print()

#<c>
row = 5

for i in range(row,0,-1) :
    for y in range(1,i + 1) :
        print(i,end='')
    print()


#<d>
row = 5

for i in range(row,0,-1) :
    for y in range(i,0,-1) :
        print(y,end='')
    print()
#<e>
row = 5

for i in range(row,0,-1) :
    for y in range(i,row + 1) :
        print(i,end='')
    print()
#<f>
row = 5

for i in range(row,0,-1) :
    for s in range(i,row) :
        print(' ',end='')
    for y in range(1,i + 1) :
        print(y,end='')
    print()
#<g>
row = 5

for i  in range(0,row) :
    for s in range(0,i):
       print(' ',end='')  
    for y in range(row,i,-1):
        print(y,end='')
      
    print()
#<h>
row = 5

for i in range(1,row + 1) :
    for s in range(i,row) :
        print(' ',end='')
    for y in range(row,row - i,-1) :
        print(y,end='')
    print()

#<18>
num = int(input("請輸入整數："))
num_1 = list(str(num))
num_1.reverse()

for i in num_1 :
    print(i,end='')    

#<19>
data = [[2, 4, 5], [5, 8, None], [10, 3, 4]]
for i , group in enumerate(data,1) :
    if None in group :
        print(f"第{i}組：Incomplete data")
    else:
        print(f"第{i}組：總和為{sum(group)}")
#<20>

num = int(input("請輸入數字："))
cout = 0
orig_num = num
while num < 0 :
        num = -num
while num > 0 :
    num //= 10
    cout += 1

if orig_num < 0 :            
    print(f"{orig_num}是{cout}位的負整數")
elif orig_num >0 :
    print(f"{orig_num}是{cout}位的正整數")

#<21>
#解法1
num = str(input("請輸入數字："))
new_num = num.replace(',','')
num_2 = int(new_num)
print(num_2*2)

#解法2
num = str(input("請輸入數字："))

while ',' in num :
    num = num.replace(',','',1)
num_2 = int(num)
print(num_2 * 2)

#<22>
num = int(input("請輸入數字："))
cout = 0
n = 1
fac = []
if num > 0 :
        while n <= num :
            if num % n == 0:
                fac.append(n)
                cout += 1  # 只有在確認是因數時，計數器才 +1
            n += 1         # 每次迴圈結束前，要把 n 推進到下一個數字
print(f"{num}的因數有{cout}個，分別為：{fac}")

#<23>

num = int(input("請輸入數字："))
for i in range(2, num):
    if num % i == 0:
        print(f"{num}不是質數。")
        break   # 1. 將 break 縮排到 if 裡面，找到因數才跳出
else:
    print(f"{num}是質數") # 2. 將 else 對齊 for，代表「迴圈沒被 break 打斷」才會執行

#<24>
string_1 = 'machine_learning'
index = 0
while index < len(string_1) :
    char = string_1[index]
    if not char.isalpha():
        print(f"找到非英文字母了，是'{char}'")
    index += 1                 # 2. 把 index += 1 退出來，確保每次迴圈都會執行到
#<25>
nums = []
for i in range(1,11) :
    if i % 3 !=  0 :
        nums.append(i )

# 用 str(nums) 轉成字串，再用 [1:-1] 切掉頭尾的括號
print(f"不能被3整除的有:{str(nums)[1:-1]}")

#<26>
num = 1
total = 0
while True:
    total += num
    if total > 100:
        break
    num += 1
print(num)

#<27>
#students = x
# students <100
#students / 3  = x...2
#students / 5  = x...3
#students / 7  = x...2

for i in range(1,100):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        students = i
        break
print(f"學生人數為{students}個")
#<28>
students = [] 
i = 1
while True:
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        students.append(i)
        if len(students) == 3 :
            break
    i += 1
print(f"{str(students)[1:-1]}")
"""
#<29>
num = [47,89,12,-4,12,2,97]
num_1 = []
for i in num :
    if i > 0 :
        num_1.append(i)
    else :
       num_1.append(i)
       break
print(f"{str(num_1)[1:-1]}")

    
        
