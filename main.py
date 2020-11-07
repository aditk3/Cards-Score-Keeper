from collections import namedtuple

Player = namedtuple('Player', ['name', 'score'])


def reset_scores():
    names = [name for name in open('players.txt')]
    for i, name in enumerate(names):
        names[i] = name[:-1]

    players = [Player(n, 0)for n in names]
    file = open('scores.txt', 'w')

    for a in players:
        file.write(f'{a.name} {a.score}\n')
    file.close()


def read_score_to_dict():
    file = open('scores.txt')
    dict_ver = {}
    list_ver = []

    rl = file.readlines()
    for line in rl:
        list_ver.append(line[:-1])

    for line in list_ver:
        dict_ver[line.split(' ')[0]] = int(line.split()[1])

    file.close()
    return dict_ver


def update_score():
    names = open('round.txt').read().split()

    score_dict = read_score_to_dict()
    score_dict[names[0]] = score_dict[names[0]] + (50 * (len(names) - 1))
    for i, name in enumerate(names):
        if i != 0:
            score_dict[name] = score_dict[name] - 50

    write_scores(score_dict)


def write_scores(sdict):
    names = [name for name in sdict.keys()]

    file = open('scores.txt', 'w')

    for name in names:
        file.write(f'{name} {sdict[name]}\n')

    file.close()

def to_pay():
    dictt = read_score_to_dict()
    for k in dictt.keys():
        print(f'{k} : {dictt[k]}')


if __name__ == '__main__':
    reset_scores()
    # update_score()
    to_pay()
