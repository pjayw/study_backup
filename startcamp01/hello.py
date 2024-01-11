import random

user_input = int(input())
selected_numbers = []
sum_of_selected_numbers = 0

for count in range(user_input) :
    number = random.randint(1,10000)
    selected_numbers.append(number)
    if number % 2 != 0:
        sum_of_selected_numbers += number

print( sum_of_selected_numbers)

# ctrl + alt + 방향키 위, 아래 | 포커싱 증가
# ctrl + 왼쪽, 오른쪽 방향키
# alt + 방향키 | 포커싱 되어있는 줄 위치 이동
# alt + shift + 위 아래 방향키 | 포커싱 되어 있는 줄 복제
# 한줄 지우기 => home 누르고 shift+end