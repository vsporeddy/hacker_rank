#https://www.hackerrank.com/challenges/runningtime/submissions/code/10390067

N = int(input())
arr = [int(s) for s in input().split()]
count = 0

for i in range(1, N):
	moved = 0
	x = arr[i]
	j = i
	while j > 0 and arr[j-1] > x:
		moved += 1
		arr[j] = arr[j-1]
		j = j - 1
	count += moved
	arr[j] = x

print(count)
