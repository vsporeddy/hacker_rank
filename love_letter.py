T = int(input())
words = [list(input()) for i in range(T)]

for i, word in enumerate(words):
    count = 0
    length = len(word)-1
    for j in range(0, int((length+1)/2)):
        while word[j] != word[length-j]:
            if word[j] > word[length-j]: word[j] = chr(ord(word[j]) - 1)
            else: word[length-j] = chr(ord(word[length-j]) - 1)
            count += 1 
    print(count)
            
        

