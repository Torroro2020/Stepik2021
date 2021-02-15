numberOfMatches = int(input(''))
x_list = [input('').split(';') for x in range(numberOfMatches)]
vs = [(x[0], x[2]) for x in x_list]


import itertools

clubs = set(itertools.chain.from_iterable(vs))

res = {club: [0, 0, 0, 0, 0] for club in clubs}


for team1, score1, team2, score2 in x_list:
    res[team1][0] += 1
    res[team2][0] += 1

    if int(score1) > int(score2):
        res[team1][1] += 1
        res[team1][4] += 3
        res[team2][3] += 1

    elif int(score1) < int(score2):
        res[team2][1] += 1
        res[team2][4] += 3
        res[team1][3] += 1

    elif int(score1) == int(score2):
        res[team1][2] += 1
        res[team1][4] += 1
        res[team2][2] += 1
        res[team2][4] += 1

for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))
