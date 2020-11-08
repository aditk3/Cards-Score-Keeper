from collections import namedtuple

Player = namedtuple('Player', ['name', 'score'])


def reset_scores():
    names = [name for name in open('players.txt')]
    for i, name in enumerate(names):
        names[i] = name[:-1]

    players = [Player(n, 0) for n in names]
    file = open('payments.txt', 'w')

    for a in players:
        file.write(f'{a.name} {a.score}\n')
    file.close()


def read_score_to_dict():
    file = open('payments.txt')
    dict_ver = {}
    list_ver = []

    rl = file.readlines()
    for line in rl:
        list_ver.append(line[:-1])

    for line in list_ver:
        dict_ver[line.split(' ')[0]] = int(line.split()[1])

    file.close()
    return dict_ver


def update_score(entry_cost=50):
    names = open('round.txt').read().split()

    score_dict = read_score_to_dict()
    score_dict[names[0]] = score_dict[names[0]] + (entry_cost * (len(names) - 1))
    for i, name in enumerate(names):
        if i != 0:
            score_dict[name] = score_dict[name] - entry_cost

    write_scores(score_dict)


def write_scores(scores_dict):
    names = [name for name in scores_dict.keys()]

    file = open('payments.txt', 'w')

    for name in names:
        file.write(f'{name} {scores_dict[name]}\n')

    file.close()


def to_pay():
    temp_dict = read_score_to_dict()
    for k in temp_dict.keys():
        print(f'{k} : {temp_dict[k]}')


if __name__ == '__main__':
    # reset_scores()
    # update_score()
    to_pay() 
    
