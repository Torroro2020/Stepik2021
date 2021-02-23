a = int(input())
b = []
for i in range(a):
    x = input().lower()
    if x not in b:
        b.append(x)

d = int(input())
e = []
for j in range(d):
    x = input().lower().split()
    for i in x:
        if i not in b and i not in e:
            e.append(i)

print('\n'.join(e))