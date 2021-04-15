from random import *
money = 1000000
while True:
    print("*"*50)
    print("A: 두개맞추기")
    print("B: Big or Small")
    print("C: 세개 맞추기")
    print("D: 두가지 주사위가 내가 정한 숫자로 통일돼서 나오기를 빌기")
    print("E: 세개의 주사위가 동일한 숫자가 나오기를 빌기")
    print("F: 그만하기")
    print("*"*50)
    section = input("구역 : ")
    dicelist = [randint(1,6) for i in range(3)]
    if section=="A":
        count1=0
        count2=0
        input1, input2 = map(int, input("숫자 : ").split())
        for i in dicelist:
            if i==input1:
                count1+=1
                break
        for i in dicelist:
            if i==input2:
                count2+=1
                break
        if count1==1 and count2==1:
            money+=50000
        else:
            money-=10000
        print("주사위 : {0} {1} {2}".format(dicelist[0], dicelist[1], dicelist[2]))
        print("내돈 : {0}".format(money))
    if section=="B":
        sum = dicelist[0]+dicelist[1]+dicelist[2]
        input1 = input("Big or Small: ")
        if input1 == "B":
            if sum>=11 and sum <=17:
                money += 10000
            else:
                money -= 10000
        elif input1 == "S":
            if sum>=4 and sum<=10:
                money += 10000
            else:
                money -= 10000
        print("주사위 합: {0}".format(sum))
        print("내돈 : {0}".format(money))
    if section=="C":
        num = 0
        input1, input2, input3 = map(int, input("숫자 : ").split())
        inputlist = [input1, input2, input3]
        for i in range(0,3):
            if inputlist[i] == dicelist[i]:   
                num+=1
        if num == 3:
            money+=1800000
        else:
            money-=10000

        print("주사위 : {0} {1} {2}".format(dicelist[0], dicelist[1], dicelist[2]))
        print("내돈 : {0}".format(money))

    if section=="D":
        input1 = int(input("한가지 숫자 입력: "))
        if input1 == dicelist[0] and input1 == dicelist[1]:
            money += 80000
        else:
            money -= 10000
        print("주사위 : {0} {1}".format(dicelist[0], dicelist[1]))
        print("내 돈: {0}".format(money))

    if section=="E":
        if dicelist[0] == dicelist[1] and dicelist[0] == dicelist[2]:
            money += 240000
        else:
            money -= 10000
        print("주사위 : {0} {1} {2}".format(dicelist[0], dicelist[1], dicelist[2]))
        print("내돈 : {0}".format(money))

    if section=="F":
        break