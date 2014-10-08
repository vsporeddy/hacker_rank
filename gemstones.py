#https://www.hackerrank.com/challenges/gem-stones

N = int(input())
elements = []
for i in range(0, N):
    elements.append(input())
    
gem_elements = list(set(elements[0]))
gems = list(set(elements[0]))
for i in range(1, N):
    for j, element in enumerate(gem_elements):
       if element not in elements[i]:
           if element in gems:
               gems.remove(element)
            
print(len(gems))
