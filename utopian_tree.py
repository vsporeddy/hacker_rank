def growth(height, cycle):
    if cycle == 0: return height
    elif height%2 == 0: return growth(height+1, cycle-1)
    else: return growth(2*height, cycle-1)

T = int(input())
N = []
for i in range(T):
    cycles = int(input())
    N.append(growth(1, cycles))
    
for i in range(T):
    print(N[i])
