import random

check = 1
sercet_number = random.randint(1,10)
while True:
    try:
        s = int(input("Mời cưng đoán số \n> "))
        if s == sercet_number:
            print("Ăn may trúng thôi, chúc mừng !!!")
            break
        elif s > sercet_number:
            print("Bạn đoán cao quá !!!")
        else:
            print("Bạn đoán bé rồi !!!")
        check += 1
    except:
        print("Bạn phải nhập vào là con số !!! ")
        
    if check >= 5:
        print("Cơ hội đã quá 5 lần, Vĩnh biệt !!!")
        break
