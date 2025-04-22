#l = [2,3,5,2,9]

l = [2,2,2,3,5]
k = []

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] != l[j]:
            k.append(l[j])
        

print(k)
