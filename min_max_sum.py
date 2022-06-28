l = [1,2,3,4,5,6]

max_ = l[0]
min_ = l[0]

for i in range(len(l)):
    if max_ < l[i] :
        max_ = l[i]
    elif min_ > l[i]:
        min_ = l[i]
print("The sum of min and max of array:  ",min_ + max_)