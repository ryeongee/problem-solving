def splitFile(file: str):
    head, number, tail = "", "", ""
    number_check = False
    for i in range(len(file)):
        if file[i].isdigit():
            number += file[i]
            number_check = True
        elif not number_check:
            head += file[i]
        else:
            tail = file[i:]
            break
    # ptr1 = 0
    # ptr2 = len(file)
    # for i in range(len(file)):
    #     if file[i].isdigit():
    #         ptr1 = i
    #         break
    # head = file[:ptr1]
    # for j in range(ptr1, len(file)):
    #     if not file[j].isdigit():
    #         ptr2 = j
    #         break
    # number = file[ptr1:ptr2]
    # tail = file[ptr2:]
    return head, number, tail


def solution(files):
    answer = []
    pre_answer = []
    for file in files:
        head, number, tail = splitFile(file)
        pre_answer.append((head, number, tail))
        pre_answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
    for ele in pre_answer:
        answer.append(''.join(ele))
    return answer


print(solution(["img12.png", "img10.png", "img02.png",
                "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress",
                "A-10 Thunderbolt II", "F-14 Tomcat"]))
