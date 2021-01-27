class piece(object):

    killed = False
    white = False
    
    def __init__(self, white):
        self.setWhite(white)
        

    def setWhite(self, white):
        self.white = white

    def isWhite(self):
        return self.white

    def isKilled(self):
        return self.killed

    def setKilled(self):
        self.killed = killed

   


class chess(piece):

    p = piece(True)
    if p.isWhite() == True:
        print("you gey muddafuka")   
