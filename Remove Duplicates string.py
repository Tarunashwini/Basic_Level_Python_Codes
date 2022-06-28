s1 = "geeksforgeeks" #"Tarun Ashwini"

s1 = s1.lower()
s = ''
dic = {}
for i in range(len(s1)):
    if s1[i] not in dic:
        dic[s1[i]] = 1
        s += s1[i]
    else:
        dic[s1[i]] += 1
print(s)
#print(dic)