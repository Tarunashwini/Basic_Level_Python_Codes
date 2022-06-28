l1 = [1,0,2,5,0,6,0,0,9]
l2 = []
count = 0
for i in range(len(l1)):
    if l1[i] != 0:
        count += 1
        l2.append(l1[i])

print(l2+[0]*(count-1))