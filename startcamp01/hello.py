while True:
    N = int(input())

    if 9 <= N <= 199 and N % 2 != 0:
        break

scores = list(map(int, input().split))
scores.sort()

middle_number = N // 2
median = scores[middle_number]
print(median)
# ctrl + alt + 방향키 위, 아래 | 포커싱 증가
# ctrl + 왼쪽, 오른쪽 방향키
# alt + 방향키 | 포커싱 되어있는 줄 위치 이동
# alt + shift + 위 아래 방향키 | 포커싱 되어 있는 줄 복제
# 한줄 지우기 => home 누르고 shift+end
