N=int(input())
Score=list(map(int, input().split()))
Max_Score=max(Score) #최대 점수

for i in range(N):
    Score[i]=Score[i]/Max_Score*100 #새로 계산한 점수

print(sum(Score)/N) #새로 계산한 점수의 평균