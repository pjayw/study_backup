import random

mushrooms = ['초록버섯', '주황버섯', '뿔버섯', '파란버섯', '좀비버섯', '머쉬맘' ]

random.shuffle(mushrooms)
#print(mushrooms)

# 코드는 명시적으로 작성 -> 남이 알아볼수 있게 변수 사용
for mushroom in mushrooms:
    print(mushroom)

for index in range(0, len(mushrooms), 2):
    for i in range(2):
        if i != 0 and i % 3 == 0 :
            print('     ', end='')
        print(mushrooms[index+i], end='')
    print()