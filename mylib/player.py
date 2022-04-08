class Player:
    def __init__(self):
        self.username = ''
    
    def inp(self):
        username = input().strip()
        self.username = username
