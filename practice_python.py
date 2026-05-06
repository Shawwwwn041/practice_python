#python教學手冊-第三章
import math
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
#a
ans3_a = math.sin(2.5) + math.exp(1.4)
print(f"Q3a答案是: {ans3_a}")
#b 
ans3_b = math.ceil(pow(6.3,2)-0.5)
print(f"Q3b答案是: {ans3_b}")

#c
ans3_c = math.floor(math.cos(0.5*0.5) + math.sqrt(2))
print(f"Q3c答案是: {ans3_c}")

#d
ans3_d = math.gcd(6,8,12)
print(f"Q3d答案是: {ans3_d}")

#e
ans3_e = math.inf - math.inf*2
print(f"Q3e答案是: {ans3_e}")

#f
ans3_f = pow(3,0.5)
print(f"Q3f答案是: {ans3_f:.2f}")

#g
ans3_g = math.log2(1024)
print(f"Q3g答案是: {ans3_g}")

#h
ans3_h = math.log(7,pow(49,3))
print(f"Q3h答案是: {ans3_h:.2f}")

#i
ans3_i = math.asin(-0.7) + math.atan(pow(math.pi,2))
print(f"Q3i答案是: {ans3_i:.2f}")
"""
#Q4
ans_q4 = math.radians(105)
print(f"Q4答案是: {ans_q4:.2f}")

#Q5
r = 3.2 #半徑
Volume = (4/3)*math.pi*pow(r,3)   #計算體積

Surface = 4*math.pi*pow(r,2)    #計算表面積
print(f"圓球體積:{Volume}，圓球表面積:{Surface}")

# 
