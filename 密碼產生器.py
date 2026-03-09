#密碼產生器
import random
import string #提供整齊預先排列好的字元(123、abc)

num = string.digits #建立數字的字串
eng = string.ascii_letters #建立英文字母的字串
code_list = list(num+eng) #建立數字與字母的混合表
random.shuffle(code_list) #利用random.shuffle語法將混合表打亂

try:
    code_len = int(input("你需要多長的密碼？"))#詢問使用者需要幾位數密碼
    if code_len != 0:
        code = "".join(code_list[:6])
        print(f"已生成你所需的密碼：{code}")        
    
        
except ValueError:
    while True:
        try:
            code_len = int(input("你需要多長的密碼？")) #詢問使用者需要幾位數密碼
            if code_len > 0:
                break
            else:
                print("密碼長度不得為0！")
        except ValueError:
            print("請輸入有效的數字！")

code = "".join(code_list[:code_len])
print(f"已生成你所需的密碼：{code}")