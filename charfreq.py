def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

a = str(input("please enter the string:"))
d=dict(most_frequent(a))
print(d)
sortedByValueDict=sorted(d.items(),key=lambda t:t[1],reverse=True)
print(sortedByValueDict)
