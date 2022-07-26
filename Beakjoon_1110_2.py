N=int(input()) #N 입력
CycleN=N
Cycle=0 #사이클 수

while True:
    A=CycleN//10 #10의자리 숫자
    B=CycleN%10 #1의자리 숫자
    C=(A+B)%10 #합의 가장 오른쪽 자리 수
    CycleN=(B*10)+C #주어진 수의 가장 오른쪽 자리 수 + 합의 가장 오른쪽 자리 수
    
    Cycle+=1 #사이클 수 증가
    
    if CycleN==N: #처음 입력한 N과 CycleN이 같아질 때
        print(Cycle)
        break

    
    
    
        