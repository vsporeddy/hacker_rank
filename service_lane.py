user_input = input()
T, N = [int(i) for i in user_input.split(' ')] 
user_input = input()
width = [int(i) for i in user_input.split(' ')] 
results = []
    
for i in range(N):
    min = 3
    user_input = input()
    start, end = [int(k) for k in user_input.split(' ')]
    for j in range(start, end+1):
        if width[j] < min: min = width[j]
    results.append(min)
    
for i, result in enumerate(results):
    print(result)
    

