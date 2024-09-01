from charactarlev import charactar

class enemy(charactar):
    def __init__(self,space,screen,tuple):
        charactar.__init__(screen,space)
        self.xpos=tuple[0]
        self.ypos=tuple[1]
