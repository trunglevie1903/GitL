from mylib.player import Player
import random

def main():
    pL = []
    for i in range(10):
        pL.append(Player('p' + str(i)))

    for i in range(len(pL)-1):
        pL[i].win_against(pL[i+1])

if __name__ == '__main__':
    main()