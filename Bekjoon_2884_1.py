Hour, Min = map(int, input().split()) #띄어쓰기로 입력받기

if Min>=45: #분단위가 45분 이상일 때
    print(Hour, Min-45)
elif Min<45: #분단위가 45분 미만일 때
    Hour-=1
    Min+=60
    if Hour<0: #0시보다 작을 때
        Hour=23
    print(Hour, Min-45)
    

