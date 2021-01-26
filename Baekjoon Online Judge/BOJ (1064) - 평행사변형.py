import math
A, B, C = [0,0], [0,0], [0,0]
A[0],A[1],B[0],B[1],C[0],C[1] = map(int,(input().split()))

if (A[0] == B[0] and A[0] == C[0]) or (A[1] == B[1] and A[1] == C[1]): # x= a y = b 인 경우
    print(-1)
elif (C[0]-A[0])*(B[1]-A[1]) == (C[1]-A[1])*(B[0]-A[0]): # 기울기가 같은 경우
    print(-1)
else: # 일반적인 경우
    r1 = math.sqrt(pow(A[0]-B[0],2)+pow(A[1]-B[1],2))
    r2 = math.sqrt(pow(A[0]-C[0],2)+pow(A[1]-C[1],2))
    r3 = math.sqrt(pow(B[0]-C[0],2)+pow(B[1]-C[1],2))

    l_list = [2*(r1+r2), 2*(r1+r3), 2*(r2+r3)]
    print(max(l_list) - min(l_list))
