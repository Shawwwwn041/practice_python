today_login = ["小王", "小李", "小王", "小陳", "小李"]
all_staff = {"小王", "小李", "小陳", "小林", "小張"}
#今天有登入的人共幾位？同一個人登入很多次只算一次
today_login_set =set(today_login)
all_staff_set = set(all_staff)
print(f"今天登入人數:{len(today_login_set)}人")
#找出今天沒登入的人，排序後印出
no_online_set = sorted(all_staff_set - today_login_set)
print(f"今日沒上線的人:{no_online_set}")
