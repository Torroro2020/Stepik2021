
with open(r'C:\Users\Артур Томе\PycharmProjects\Stepik2021\dt.txt', 'r') as f:
    strings = [s.rstrip() for s in f.readlines()] # в каждой строке удаляет пробелы
score = [s.split(';')[1:] for s in strings] # разделение строки на части символом c элемента под номером 1

with open(r'C:\Users\Артур Томе\PycharmProjects\Stepik2021\newDataSet.txt', 'w') as n:
    for x in score:
        res = (sum(map(int, x))/len(x))
        n.write(str(res) + '\n')
    sr_mat = sum([int(x[0]) for x in score]) / len(score)
    sr_fiz = sum([int(x[1]) for x in score]) / len(score)
    sr_rus = sum([int(x[2]) for x in score]) / len(score)
    n.writelines(str(sr_mat) + ' ' + str(sr_fiz) + ' ' + str(sr_rus))

