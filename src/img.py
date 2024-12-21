import pygame

class Image(pygame.sprite.Sprite):
    def __init__(self,pathfmt,pathindex,pos,size,pathindexcnt=0):
        self.pathfmt=pathfmt
        self.pathindex=pathindex
        self.pos=list(pos)
        self.size=size
        self.pathindexcnt=pathindexcnt
        self.updateimage()

    def updateimage(self):
        path=self.pathfmt
        if self.pathindexcnt!=0:
            path=path%self.pathindex
        self.image=pygame.image.load(path)
        if self.size:
            self.image=pygame.transform.scale(self.image,self.size)

    def updatesize(self,size):
        self.size=size
        self.updateimage()

    def updateindex(self,pathindex):
        self.pathindex=pathindex
        self.updateimage()

    def getrect(self):
        rect=self.image.get_rect()
        rect.x,rect.y=self.pos
        return rect

    def doleft(self,force):
        self.pos[0]-=force

    def doright(self,force):
        self.pos[0]+=force

    def doup(self,force):
        self.pos[1]+=force

    def dodown(self,force):
        self.pos[1]-=force

    def draw(self,screen):
        screen.blit(self.image,self.getrect())
