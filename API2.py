import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
answer = r.text
print(answer)

while True:
    r = 'https://stepic.org/media/attachments/course67/3.6.3/' + answer
    link = (requests.get(r).text)
    print(link)
    if len(link) > 10:
        print(link)
        break
    else:
        answer = link

with open(r'C:\Users\Артур Томе\PycharmProjects\Stepik2021\newDataSet.txt', 'w') as n:
    n.write(link)
