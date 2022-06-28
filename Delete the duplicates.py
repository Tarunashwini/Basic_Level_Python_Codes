l = [1,3,2,2,1,2,3,1]
dic = {}
del_i = []

print("The Original list:   ", end = "  " )
print(l)

for i in range(len(l)):
    if l[i] not in dic:
        dic[l[i]] = 1
    else:
        dic[l[i]] = dic[l[i]] + 1

    if dic[l[i]] >= 3:
        del_i.append(l[i])
        l[i] = None

print("The element after flaging: ", end =" ")
print(l)

l = [i for i in l if i != None]

print("The array after deleting the elements:   ", end = " ")
print(l)

print("The elements which are deleted:   ", end  = "  ")
print(del_i)
