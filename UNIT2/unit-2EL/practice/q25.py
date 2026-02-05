class Player:
    active =0
    def __init__(self):
        Player.active = Player.active+1
    def __del__(self):
        Player.active = Player.active - 1

    @classmethod
    def totalGamePlayer(cls):
        print(Player.active)

p1 =Player()
p2 =Player()
p3 =Player()
Player.totalGamePlayer()
del p2
Player.totalGamePlayer()
p2 =Player()
Player.totalGamePlayer()
