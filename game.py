print("게임을 시작합니다")
print("테트리스 시작")
print("1. 오른쪽 2. 왼쪽 3. 블록 바꾸기")
number = input("숫자를 입력하세요: ")
print("당신이 입력한 숫자는 ", number)

#만약에 1번을 누르면 오른쪽
if number == 1:
    print("오른쪽으로 이동")
#만약에 2번을 누르면 왼쪽
if number == 2:
    print("왼쪽으로 이동")
#만약에 3번을 누르면 블록 바꾸기
if number == 3:
    print("블록 바꿈.")