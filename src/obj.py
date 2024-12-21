import sys
from .img import *
import time

class objectbase(Image):
    def __init__(self,pathfmt,pathindex,pos,size=None,pathindexcnt=0):
        super(objectbase,self).__init__(pathfmt,pathindex,pos,size,pathindexcnt)
        self.preindextime=0
        self.prepositiontime=0

    def update(self,movex,movey):
        self.checkimageindex()
        self.checkposition(movex,movey)

    def checkimageindex(self):
        if time.time()-self.preindextime<=0.1:
            return
        self.preindextime=time.time()
        idx=self.pathindex+1
        if idx>=self.pathindexcnt:
            idx=0
        self.updateindex(idx)

    def checkposition(self,movex,movey):
        if time.time()-self.prepositiontime<=0.1:
            return
        self.prepositiontime=time.time()
        self.pos[0]+=movex
        self.pos[1]+=movey
