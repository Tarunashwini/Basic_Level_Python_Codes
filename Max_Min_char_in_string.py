s = "Java is an oop language"

def max_min_char(s):
    dic = {}
    max_ = 0
    min_ = 99
    min_char = ''
    max_char = ''
    min_arr = []
    max_arr = []

    for i in range(len(s)):
        if (s[i] == " " or s[i] == "."):
            pass
        elif (s[i] not in dic):
            dic[s[i]] = 0
        else:
            dic[s[i]] += 1
    #print(dic)

    for key in dic:
        if dic[key] > max_:
            max_char = key
            max_arr.append(key)
        elif dic[key] < min_:
            min_arr.append(key)
            min_char = key
    print("The min array :  ",min_arr)
    print("The max array :   ",max_arr)

    return (min_char, max_char)



print(max_min_char(s))