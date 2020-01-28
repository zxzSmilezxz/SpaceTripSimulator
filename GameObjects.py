import pygame,random
pygame.init()
class Boom():
    def __init__(self,name,display):
        self.page=pygame.image.load(name).convert_alpha()
        self.page.set_colorkey((0,0,0))
        self.place= self.page.get_rect()
        self.place.move_ip(0, -60)
        self.fire=False
        self.display=display
    def Show(self):
        self.display.blit(self.page,(self.place.x,self.place.y))

class Ship():
    def __init__(self,name,display):
        self.page=pygame.image.load(name).convert_alpha()
        self.page.set_colorkey((0,0,0))
        self.place= self.page.get_rect()
        self.place.move_ip(0, 0)
        self.speed=int(5)
        self.bullet=0
        self.fire=False
        self.display = display
    def Show(self):
        self.display.blit(self.page,(self.place.x,self.place.y))

class Arrow():
    def __init__(self,arrowImage,display):
        self.page = pygame.image.load(arrowImage).convert_alpha()
        self.page.set_colorkey((0, 0, 0))
        self.place= self.page.get_rect()
        self.place.y=-51
        self.speed = int( 12)
        self.display = display
    def Show(self):
        self.display.blit(self.page,self.place.topleft)


class Meteor():
    def __init__(self,meteorImage,display,x=900):
        self.x=x
        self.page = pygame.image.load(meteorImage).convert_alpha()
        self.page.set_colorkey((0, 0, 0))
        self.place= self.page.get_rect()
        self.place.move_ip(self.x, random.randrange(0,600,50))
        self.speed = int(-7)
        self.display = display
    def Show(self):
        if self.place.x < - 50:
            self.place.y = 0
            self.place.move_ip(self.x,random.randrange(0,600,50))
        self.display.blit(self.page,self.place)


class Big_blaster():
    def __init__(self,bigBlastImage,bigBlastWarningImage,display):
        self.big_boom_time = 0
        self.page = pygame.image.load(bigBlastImage).convert_alpha()
        self.page_warning = pygame.image.load(bigBlastWarningImage).convert_alpha()
        self.page.set_colorkey((0, 0, 0))
        self.place= self.page.get_rect()
        self.place.move_ip(0, -60)
        self.boom=False
        self.display=display
    def Show(self):
        if self.place.y < - 50:
            self.place.y = random.randrange(0,600,50)
        if self.big_boom_time == 0:
            self.big_boom_time=pygame.time.get_ticks()
        if pygame.time.get_ticks()-self.big_boom_time<2500:
            self.display.blit(self.page_warning,(self.place.x+885,self.place.y))
        elif pygame.time.get_ticks() - self.big_boom_time < 4000:

            self.display.blit(self.page,self.place)
        else:
            self.boom = False
            self.place.y=-60
            self.big_boom_time = 0

class Prize():
    def __init__(self,name,display,x=900):
        self.page = pygame.image.load(name)
        self.page.set_colorkey((0, 0, 0))
        self.page = pygame.transform.scale(self.page,(50,50)).convert_alpha()
        self.place= self.page.get_rect()
        self.x = int(x)
        self.place.move_ip(self.x, random.randrange(0,600,50))
        self.speed = int(-7)
        self.run=False
        self.display = display

    def Show(self,Meteor_list):
        if self.place.x<-50:
            self.place.y = 0
            self.place.move_ip(self.x, random.randrange(0,600,50))
            c=True
            while c==True:
                self.place.y = 0
                self.place.move_ip(self.x, random.randrange(0,600,50))
                for m in Meteor_list:
                    if self.place.colliderect(m.place):
                        c=True
                        break
                    c=False
                continue
            self.run = False
        self.display.blit(self.page,self.place)