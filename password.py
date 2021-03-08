x = 3
password = 'a123456'
while True:
    pwd = input('請輸入密碼')
    if pwd == password :
        print('登入成功!')
        break
    elif pwd != password :
        x = x - 1 
        print('密碼錯誤! 還有', x, '次機會')
        if x == 0:
            break