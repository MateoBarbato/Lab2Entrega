import pygame
from helpers import drawBackground, exit


class Game ():

    def __init__(self) -> None:
        pass

    def run(self):
        gameRunning = True
        while gameRunning:
            # BLIT ZONE
            drawBackground(screen, background)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # limpiar()
                        gameRunning = False
                    if event.key == pygame.K_SPACE:
                        bug = None
                        pass
                    if event.key == pygame.K_h:
                        hardcoreMode = not hardcoreMode
                    if event.key == pygame.K_m:
                        muteState = not muteState
                    if event.key == pygame.K_SEMICOLON:
                        cheatOn = not cheatOn
                    if event.key == pygame.K_k:
                        pass
                    if event.key == pygame.K_w:
                        pass
                if event.type == pygame.USEREVENT+1:
                    moveBugs = True
                if event.type == pygame.USEREVENT+2:
                    createBug = True
            if cheatOn:
                powerUp1 = True
            else:
                powerUp1 = False

            if player:
                player.blitPlayer()
                player.update()
                if powerUp1:
                    player.movePlayer(8)
                else:
                    player.movePlayer(4)

            if createBug:
                if len(bugs) < 8:
                    bugs.append(Bug(bugImg, randIntPos('x', 60),
                                randIntPos('y', 60), 60, 60, screen))
                createBug = False

            for bug in bugs[:]:
                if moveBugs:
                    bug.moveRandom(25)
                bug.blitBug()
            moveBugs = False

            pygame.display.flip()
