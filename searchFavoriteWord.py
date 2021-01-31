from collections import Counter
import re
with open(r'C:\Users\Артур Томе\PycharmProjects\Stepik2021\dataset.txt', 'r') as rr:
    lista = [re.sub('\W+',' ', i).lower() for i in rr]
    lippa = ' '.join(lista)
    zidda = lippa.split()
    cnt = Counter(zidda)
    keyMax = max(cnt, key = cnt.get)
    valueMax = cnt.setdefault(keyMax)
    out = open(r'C:\Users\Артур Томе\PycharmProjects\Stepik2021\newDataSet.txt', 'w')
    out.write(keyMax + ' ' + str(valueMax))
    out.close()
