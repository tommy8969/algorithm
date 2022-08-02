Num = []
for i in range(10) :
  a = int(input())
  Num.append(a % 42) #42로 나눈 나머지

Num = set(Num) #중복 값 제거
print(len(Num))