setClasses = tuple(str(i) for i in range(1, 12))
dictHeight = dict.fromkeys(setClasses, 0)
dictCount = dict.fromkeys(setClasses, 0)

file = open('answers.txt', 'a+')

with open('dataset_3380_5.txt', encoding='UTF-8') as inf:
    for line in inf:
        lst = line.strip().split('\t')
        dictHeight[lst[0]] += float(lst[2])
        dictCount[lst[0]] += 1

for i in setClasses:
    if dictHeight[i] == 0:
        d = '-'
    else:
        d = str(dictHeight[i] / dictCount[i])
    print(i + ' ' + d, file=file)

#     Вариант № 2
# d = dict()
# with open('dataset.txt') as inf:
#     for line in inf:
#         a, b, c = line.strip().split( )
#         d.setdefault(a, []).append(int(c))
#
# k = 1
#
# while k <= 11:
#     if str(k) in d.keys():
#         print(k, sum(d.get(str(k)))/len(d.get(str(k))))
#     else:
#         print(k, '-')
#     k += 1