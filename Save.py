import pygame,sys
pygame.init()
class Score():
    @staticmethod
    def showScore(font1,display,window):
        try:
            f = open('score.txt', 'r')
            guy = f.readlines()
            f.close()
        except:
            f.close()
        level = 0
        u = 1
        while u:
            window.fill((0, 0, 0))
            GO = font1.render(' SCORE ', 1, (47, 156, 77))
            window.blit(GO, (350, level + 50))
            level2 = 150
            i = 0
            while i < (len(guy)):
                GO = font1.render("Guy: " + guy[i + 1][0:-1] + "          Score : " + guy[i][0:-1], 1, (200, 155, 77))
                window.blit(GO, (150, level + level2))
                level2 += 100
                if i == len(guy) - 2:
                    max_l = level2
                i += 2
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP and level < 0:
                        level += 100
                    if e.key == pygame.K_DOWN and max_l + level > 700:
                        level -= 100
                    if e.key == pygame.K_ESCAPE:
                        return

            display.blit(window, (0, 0))
            pygame.display.update()

    @staticmethod
    def putName(font1,display,window):
        u=1
        name=""
        while u:
            window.fill((0, 0, 0))
            GO = font1.render(' Put your name ', 1, (200, 155, 77))
            window.blit(GO, (350, 50))
            GO = font1.render(name, 1, (200, 155, 77))
            window.blit(GO, (150, 150))
            for e in pygame.event.get():
                    if e.type==pygame.QUIT :
                        sys.exit()
                    if e.type==pygame.KEYDOWN:
                        if e.key==pygame.K_q:
                            a="q"
                            name+=a
                        if e.key==pygame.K_w:
                            a="w"
                            name+=a
                        if e.key==pygame.K_e:
                            a="e"
                            name+=a
                        if e.key==pygame.K_r:
                            a="r"
                            name+=a
                        if e.key==pygame.K_t:
                            a="t"
                            name+=a
                        if e.key==pygame.K_y:
                            a="y"
                            name+=a
                        if e.key==pygame.K_u:
                            a="u"
                            name+=a
                        if e.key==pygame.K_i:
                            a="i"
                            name+=a
                        if e.key==pygame.K_o:
                            a="o"
                            name+=a
                        if e.key==pygame.K_p:
                            a="p"
                            name+=a
                        if e.key==pygame.K_a:
                            a="a"
                            name+=a
                        if e.key==pygame.K_s:
                            a="s"
                            name+=a
                        if e.key==pygame.K_d:
                            a="d"
                            name+=a
                        if e.key==pygame.K_f:
                            a="f"
                            name+=a
                        if e.key==pygame.K_g:
                            a="g"
                            name+=a
                        if e.key==pygame.K_h:
                            a="h"
                            name+=a
                        if e.key==pygame.K_j:
                            a="j"
                            name+=a
                        if e.key==pygame.K_k:
                            a="k"
                            name+=a
                        if e.key==pygame.K_l:
                            a="l"
                            name+=a
                        if e.key==pygame.K_z:
                            a="z"
                            name+=a
                        if e.key==pygame.K_x:
                            a="x"
                            name+=a
                        if e.key==pygame.K_c:
                            a="c"
                            name+=a
                        if e.key==pygame.K_v:
                            a="v"
                            name+=a
                        if e.key==pygame.K_b:
                            a="b"
                            name+=a
                        if e.key==pygame.K_n:
                            a="n"
                            name+=a
                        if e.key==pygame.K_m:
                            a="m"
                            name+=a
                        if e.key==pygame.K_BACKSPACE:
                            name=name[0:-1]
                        if e.key==pygame.K_RETURN:
                            if name=="":
                                name="NoName"
                            return name

            display.blit(window, (0, 0))
            pygame.display.update()

                    

                   
        
