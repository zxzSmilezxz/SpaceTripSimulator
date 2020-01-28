import pygame,sys
pygame.init()
Xw=int(900)
Yw=int(650)
X=int(900)
Y=int(600)
display=pygame.display.set_mode((Xw,Yw))
pygame.init()
font1= pygame.font.SysFont("ZOMBIE.TTF", 37)
window=pygame.Surface((Xw,Yw))

    def Score():
        try:
            f = open('score.txt', 'r')
            guy = f.readlines()
            f.close()
        except:
            f.close()
        level = 0
        u=1
        while u:
            window.fill((0, 0, 0))
            GO = font1.render(' SCORE ', 1, (47, 156, 77))
            window.blit(GO, (350,  level+50))
            level2=150
            i=0
            while i<(len(guy)):
                GO = font1.render("Guy: " + guy[i+1][0:-1] + "          Score : " + guy[i][0:-1], 1, (200, 155, 77))
                window.blit(GO, (150, level+level2))
                level2+=100
                if i==len(guy)-2:
                   max_l=level2
                i+=2
            for e in pygame.event.get():
                    if e.type==pygame.QUIT:
                        sys.exit()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_UP and  level <0:
                            level+=100
                        if e.key==pygame.K_DOWN and max_l+level >700 :
                            level-=100
                        if e.key==pygame.K_ESCAPE:
                            return



            display.blit(window, (0, 0))
            pygame.display.update()



                   
        
