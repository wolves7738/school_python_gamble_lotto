import random

my = [2,6,37,28,41,8]
per = 0
five = 0
four = 0
three = 0
one = 0
blank = 0

while True:
    per +=1
    number = random.sample(range(1,46),6)
    count = 0
    for i in range(6):
        if my[i] == number[i]:
            count +=1
    if count == 3:
        five += 1
        print(number)
        print("5등 당첨", (float(five)/per*100), "%")
        

    elif count == 4:
        four += 1
        print(number)
        print("4등 당첨", (float(four)/per*100), "%")
        break
    elif count == 5:
        three += 1
        print(number)
        print("3등 당첨", (float(three)/per*100), "%")

    elif count == 6:
        one += 1
        print(number)
        print("1등 당첨", (float(one)/per*100), "%")
        break

    else:
        blank += 1
        print(number)
        print("시간 낭비하셨네요")