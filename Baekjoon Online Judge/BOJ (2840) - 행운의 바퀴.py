n, k = map(int, input().split())
circle = ['?'] * n

for i in range(k):
    spin = input().split()
    # 한바퀴 넘어가는 경우에 기존 자리에서 바뀐 차이만큼을 구하기 위해 나머지 구함.
    s = int(spin[0]) % n
    s_char = str(spin[1])		# 문자

    # 큐가 아닌 리스트를 슬라이싱 한 후에 앞뒤 순서를 바꿔 다시 붙임.
    circle = circle[-s:] + circle[:-s]
    # 움직인 후에 화살표가 가리키는 자리(circle[0])이 '?'일 때
    if circle[0] == '?':
        # 입력된 문자가 이미 다른 자리에 존재하는 경우, 바퀴 존재하지 않음
        if s_char in circle:
            print('!')
            break
        # 처음 넣는 문자일 경우, 해당 자리에 문자 넣음.
        circle[0] = s_char
    # 화살표가 가리키는 자리가 현재 문자와 같은 경우 넘김.
    elif circle[0] == s_char:
        continue
    # 화살표가 가리키는 자리에 현재 문자와 다른 문자가 존재함. 자리가 겹치므로 바퀴 성립 X
    else:
        print('!')
        break
# 반복문이 모두 실행된 후에 바퀴 문자 출력
else:
    print("".join(circle))
