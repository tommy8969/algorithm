C=int(input()) 

for i in range(C):
    Score=list(map(int, input().split())) 
    Average=sum(Score[1:])/Score[0] #평균 구하기 / Score[1:] : 학생 점수, Score[0] : 학생 수
    Count=0 #평균을 넘는 학생 수

    for j in Score[1:]:
        if Average<j: #평균보다 점수가 높을 때
            Count+=1 #평균을 넘는 학생 수 +1

    Rate=(Count/Score[0])*100 #평균을 넘는 학생들의 비율
    print(f'{Rate:.3f}%') #소수 셋째 자리까지 출력