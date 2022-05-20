class MinStack:

    def __init__(self):
        # 일반 스택
        self.arr = []

        # 최소값 스택
        self.min_arr = []

    def push(self, val: int) -> None:
        # 일반 스택에 추가
        self.arr.append(val)

        if len(self.min_arr) == 0:
            # 최소값 스택에 비어 있으므로 그냥 추가
            self.min_arr.append(val)
        else:
            # 가장 상단의 값과 현재 추가되는 값의 최소값을 최소값 스택에 추가
            self.min_arr.append(min(val, self.min_arr[-1]))

    def pop(self) -> None:
        self.min_arr.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        # 최소값 스택의 상단을 리턴
        return self.min_arr[-1]
