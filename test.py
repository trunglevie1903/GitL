from mylib.player import Player
import random

def main():
    pL = []
    for i in range(10):
        pL.append(Player('p' + str(i)))

    for i in range(len(pL)-1):
        pL[i].win_against(pL[i+1])

    p1, p2 = Player('p1'), Player('p2')
    if random.random() < 0.5:
        p1.win_against(p2)
    else:
        p2.win_against(p1)

if __name__ == '__main__':
    main()