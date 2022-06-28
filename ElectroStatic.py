def Electrostic(arr, con):
    con = list(con)
    print(con)
    sum = 0
    for i in range(len(con)):
        if con[i] == 'P' or con[i] == 'p':
            sum += arr[i]
        elif con[i] == 'N' or con[i] == 'n':
            sum -= arr[i]
    return sum*100

print(Electrostic([4,3,5], 'PNP'))