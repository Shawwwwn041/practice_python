#請寫一個程式，讓使用者輸入一個字串（代號），並依照下列順序進行檢查與處理：
#輸入：讓使用者輸入代號。
#1. 長度檢查：代號長度必須 大於等於 6 個字元。如果不符合，印出 錯誤：代號長度太短。
#2.空格檢查：代號中 不能包含空格。如果包含空格，印出 錯誤：代號不能包含空格。
#3.符號檢查：代號中 必須包含 至少一個 - (短橫線) 符號。如果沒有，印出 錯誤：代號必須包含短橫線。
#如果以上檢查都通過（進入 else）：
#1.將代號中的 - (短橫線) 全部替換成 * (星號)。
#2.將整串代號轉為 全大寫。

spy_code = input("請輸入代號")
length = len(spy_code)
space_finder = spy_code.find(" ")
dash_finder = spy_code.find("-")

if length < 6 :
    print("錯誤：代號長度太短")
elif space_finder != -1:
    print("錯誤：代號不能包含空格")
elif dash_finder ==-1:
    print("錯誤：代號必須包含短橫線")
else :
    name_replacer =  spy_code.replace("-","*").upper()
    print(f"驗證成功！你的加密代號為：{name_replacer}!")





