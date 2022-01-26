from collections import defaultdict
list_int =map(int,input().split(","))

dict1 = defaultdict(lambda : 0)
a=range(1,10)
for i in list_int:
    for j in a:
        if i%j==0:
            dict1[str(j)] = dict1[str(j)]+1
print(dict(dict1))
