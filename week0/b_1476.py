E, S, M = map(int, input().split())

X = 1 # 정답으로 낼 결과물
while(True):
    if((X-E) % 15 == 0 and (X-S)%28 == 0 and (X-M) % 19 == 0):
        break
    X += 1

print(X)