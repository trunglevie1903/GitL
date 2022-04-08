class Player:
    def __init__(self):
        self.username = ''
        self.win_count = 0
        self.lost_count = 0
    
    def inp(self):
        username = input().strip()
        self.username = username

    def win_against(self, player):
        print('Player', self.username, 'won against player', player.username)
        self.win_count += 1
        player.lost_count += 1