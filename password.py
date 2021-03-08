x = 3
password = 'a123456'
while x > 0 :
    x = x - 1
    pwd = input('請輸入密碼')
    if pwd == password :
        print('登入成功!')
        break
    elif pwd != password :
        if x != 0:
            print('密碼錯誤! 還有', x, '次機會')
        if x == 0:
            print('沒機會了!')
            break