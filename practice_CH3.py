#python教學手冊-第三章
import math
import random
# Q1:max,min的運用
"""
max1 = max(12,81,93,27)
min1 = min(12,81,93,27)

print(max1)
print(min1)

#Q2:pow的運用

ans1 = pow(2,64)
print(f"答案是:{ans1}")

#Q3
#<a>
ans3_a = math.sin(2.5) + math.exp(1.4)
print(f"Q3a答案是: {ans3_a}")
#<b>
ans3_b = math.ceil(pow(6.3,2)-0.5)
print(f"Q3b答案是: {ans3_b}")

#<c>
ans3_c = math.floor(math.cos(0.5*0.5) + math.sqrt(2))
print(f"Q3c答案是: {ans3_c}")

#<d>
ans3_d = math.gcd(6,8,12)
print(f"Q3d答案是: {ans3_d}")

#<e>
ans3_e = math.inf - math.inf*2
print(f"Q3e答案是: {ans3_e}")

#<f>
ans3_f = pow(3,0.5)
print(f"Q3f答案是: {ans3_f:.2f}")

#<g>
ans3_g = math.log2(1024)
print(f"Q3g答案是: {ans3_g}")

#<h>
ans3_h = math.log(7,pow(49,3))
print(f"Q3h答案是: {ans3_h:.2f}")

#<i>
ans3_i = math.asin(-0.7) + math.atan(pow(math.pi,2))
print(f"Q3i答案是: {ans3_i:.2f}")

#Q4
ans_q4 = math.radians(105)
print(f"Q4答案是: {ans_q4:.2f}")

#Q5
r = 3.2 #半徑
Volume = (4/3)*math.pi*pow(r,3)   #計算體積

Surface = 4*math.pi*pow(r,2)    #計算表面積
print(f"圓球體積:{Volume}，圓球表面積:{Surface}")

#Q6
#<a>
ans_q6a = random.random()
print(f"Q6 answer->{ans_q6a}")

#<b>
ans_q6b = random.choices('Signficant',k=3)
print(f"Q6b answers->{ans_q6b}")
#<c>
ans_q6c = random.randint(1,6)
print(f"q6c answer ->{ans_q6c}")

#<d>
ans_q6d = random.randrange(2,11,2)
print(f"q6d answer ->{ans_q6d}")

#<e>
ans_q6e = random.uniform(-1,1)
print(f"q6e answer ->{ans_q6e:.2f}")

#Q7
random.seed(37)
#<a>
ans_q7a = random.randint(1,100)
print(f"ans Q7<a>:{ans_q7a}")

#<b>
ans_q7b = random.choices('Halloween',k=4)
print(f"ans Q7<b>:{ans_q7b}")

#<c>
ans_q7c = random.sample([12,38,54,64,77,29],2)
print(f"ans Q7<c>:{ans_q7c}")

#<d>
my_list = [2,3,5,8,9]
random.shuffle(my_list)
print(f"newresult:{my_list}")

#Q8
random.seed(199)
#<a>
ans_q8a = random.choice('abcdefg')
print(f"ansQ8a result:{ans_q8a}")

#<b>
ans_q8b = random.sample([12,38,56,78,90],3)
print(f"ansQ8b result:{ans_q8b}")

#<c>
ans_q8c = [1, 2, 3, 4, 5]
random.shuffle(ans_q8c)
print(f"ansQ8c result:{ans_q8c}")

#<d>
ans_q8d = random.random()
print(f"ansQ8d result:{ans_q8d:.2f}")

#<e>
ans_q8e = random.choices('abcd',k=5)
print(f"ansQ8e result:{ans_q8e}")

#Q9
#<a>
print('charator:\u674e\u5764\u80b2')

#<b>
print(ord('\u674e'), ord('\u5764'), ord('\u80b2'))

#<c>
print(hex(ord('\u674e')), hex(ord('\u5764')), hex(ord('\u80b2')))

#Q10
s1 = '李'
s2 = '坤育'
print(f"我的名字是:{s1+s2}")

#Q11
s3 = '*^_^*'
print(s3 * 10)

#Q12
s1 = 'it is never too late to learn'

#<a>
ans12_a = s1.title()
print(ans12_a)

#<b>
ans12_b = s1.capitalize()
print(ans12_b)

#<c>
ans12_c = s1.isalpha()
print(ans12_c)

#<d>
ans12_d = s1.count('e')
print(ans12_d)

#<e>
ans12_e = s1.replace(' never '," ")
print(ans12_e)

#<f>
ans12_f = s1.replace('late','LATE')
print(ans12_f)

#Q14
s1 = 'cats and dogs'
ans_q14 = s1.title()
ans_q14_1 = ans_q14.replace()
print(ans_q14_1)

#Q15
s1 = '*^_^* python *w_w*'.strip('*^_^* , *w_w*')
print(s1)

#Q16
S1 = '  Peggy Chen  '.strip()
print(S1)

#Q17
data = [10,20,30,40,50,60,70,80]

#<a>
ans17_a = data[2:]
print(ans17_a)

#<b>
ans17_b = data[1:6]
print(ans17_b)

#<c>
ans17_c = data[:3]
print(ans17_c)

#<d>
ans17_d = data[-3:]
print(ans17_d)

#<e>
ans17_e = data[0:7:2]
print(ans17_e)

#<f>
ans17_f = data[0:3]
print(ans17_f)

#<g>
ans17_g = data[::-1]
print(ans17_g)

#<h>
ans17_h = data[1::2]
print(ans17_h)

#Q18

#<a>
range_a = range(0,5)
print(f"0~4(包含4的整數串列):{list(range_a)}")

#<b>
range_b = range(2,10)
print(f"2~9(包含9的整數串列):{list(range_b)}")

#<c>
range_c = range(1,10,2)
print(f"1~9(間隔2，包含9的整數串列):{list(range_c)}")

#<d>
range_d = range(10,0,-2)
print(f"10~1(間隔-2，包含1的整數串列):{list(range_d)}")

#<e>
range_e = range(3,15,3)
print(f"3~15(不包含15的整數串列):{list(range_e)}")

#<f>
range_f = range(-5,6,2)
print(f"-5~6(不包含6的整數串列):{list(range_f)}")

#<g>
range_g = range(20,11,-1)
print(f"20~11(不包含11的整數串列):{list(range_g)}")

#<h>
range_h = list(range(8,8))
print(range_h)

#Q19
items = []
#將筆記本加入串列
items.append('筆記本')
items.insert(0,'鉛筆')
items.append('橡皮擦')
print(f"目前清單:{items}")

#Q20
fruits = ['蘋果','香蕉','橘子','葡萄','香蕉']

#<a>
fruits.remove( '香蕉' )
fruits.remove( '橘子' )
last_fruits = fruits.pop()
print(f"取出的水果列表:{last_fruits}")
fruits.clear()
print(f"最後更新的水果列表為:{fruits}")

###完成練習###

#Gemini出的考題
#Q1
box = ['iPhone','iPad','Macbook']
get_price = random.sample(box,2)
print(get_price)

get_price1 = random.choices(box,k=2)
print(get_price1)
"""
#Q2
msg = "  I love Apple  "
m = msg.strip().replace('Apple','Python')
print(m)

#Q3
numbers = [10,20,30,40,50,60,70]
print(numbers[1:6:2])

#Q4
range_Q4 = range(10,0,-1)
print(list(range_Q4))

#Q5
my_list = ['A','B','C','D']
final_list = my_list.pop(2)
print(final_list)
print(my_list)
