
class stack:
    def __init__(self):  # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):   # 스택 요소 삭제 pop()
        return self.items.pop()

acc = stack()
str = input().split()
x = 0
for c in str:
    if c >= '0' and c <= '9':
        x = 10 * x + int(c)

print(x)