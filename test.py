from mylib.player import Player
import random

def main():
    p1, p2 = Player('p1'), Player('p2')
    if random.random() < 0.5:
        p1.win_against(p2)
    else:
        p1.win_against(p2)

if __name__ == '__main__':
    main()