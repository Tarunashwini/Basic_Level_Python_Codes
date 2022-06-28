input1 = input().split()
n = len(input1)

s = ""
i = n
while(i>0):
    s = s + input1[i-1] + " "
    i = i -1
print(s)