#密碼產生器
import random
import string #提供整齊預先排列好的字元(123、abc)

num = string.digits #建立數字的字串
eng = string.ascii_letters #建立英文字母的字串
code_list = list(num+eng) #建立數字與字母的混合表
random.shuffle(code_list) #利用random.shuffle語法將混合表打亂

while True:
    try:
        code_len = int(input("你需要多長的密碼？"))#詢問使用者需要幾位數密碼
        if code_len > 0:
                code = "".join(code_list[:code_len])
                print(f"已生成你所需的密碼：{code}")
            else code_len <= 0:
            print("輸入大於0的數字!")

    except ValueError:
        print("你輸入的格式錯誤!")
