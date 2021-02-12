import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/383.txt')
print(len(r.text))
a = r.text
print(len(a.splitlines()))

