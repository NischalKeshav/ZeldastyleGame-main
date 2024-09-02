from charactarlev import charactar

class enemy(charactar):
    def __init__(self,space,screen,handler,tuple):
        charactar.__init__(self,screen,space,handler,tuple)
        print("b")
        self.xpos=tuple[0]
        self.ypos=tuple[1]
        self.poly.collision_type=2
        print(self.xpos)
