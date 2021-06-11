#https://www.acmicpc.net/problem/4659

def f(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        return 1
    else:
        return 2

while True:
    s = input()
    chk,chk2 = 0,0
    if s == "end": break;
    for i in range(len(s)-1):
        if (s[i] != 'e' and s[i] != 'o' and s[i] == s[i+1]):
            chk=1

    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            chk2=1
    for i in range(len(s)-2):
        if f(s[i]) == 1 and f(s[i+1]) == 1 and f(s[i+2]) == 1:
            chk=1
        elif f(s[i]) == 2 and f(s[i+1]) == 2 and f(s[i+2]) == 2:
            chk=1

    if chk == 1 or chk2 == 0:
        print("<" + s + "> is not acceptable." )
    else:
        print("<" + s + "> is acceptable." )
