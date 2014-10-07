N = int(input())
balls = [int(input()) for i in range(N)]
total = 0.0
for i, ball in enumerate(balls):
    total += ball
    
print(total/2.0)
