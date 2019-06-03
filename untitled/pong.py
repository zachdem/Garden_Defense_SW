import pygame, sys
import time
from pygame.locals import *

pygame.init()

# # definitions
WINHEIGHT = 500
WINWIDTH = 800
# white = (255, 255, 255)
black = (0, 0, 0)
# FPS = 60
#
# paddleLeft = pygame.image.load("paddle.png")
# paddleRight = pygame.image.load("paddle.png")
# paddleRightx = 750
# paddleRighty = (WINHEIGHT / 2) - 32
# paddleLeftx = 42
# paddleLefty = (WINHEIGHT / 2) - 32
# paddleRightyChange = 0
# paddleLeftyChange = 0
#
# ballImage = pygame.image.load("ball.png")
# ballx = (WINWIDTH / 2) - 15
# bally = (WINHEIGHT / 2) - 15
# ballxDIR = 1
# ballyDIR = 1
# ballxchange = 3
# ballychange = 5
#
#
# # init surface & clock
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
# pygame.display.set_caption('pong')
# clock = pygame.time.Clock()
#
while True:
#
      DISPLAYSURF.fill(black)
#
#     ballx += ballxDIR * ballxchange
#     bally += ballyDIR * ballychange
#     DISPLAYSURF.blit(ballImage, (ballx, bally))
#     DISPLAYSURF.blit(paddleLeft, (paddleLeftx, paddleLefty))
#     DISPLAYSURF.blit(paddleRight, (paddleRightx, paddleRighty))
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     if bally == WINHEIGHT:
#         ballyDIR *= -1
#
#     if bally == 0:
#         ballyDIR *= -1
#
#
#     #RIGHT PADDLE MOVEMENT
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_UP:
#             paddleRightyChange = -5
#         elif event.key == pygame.K_DOWN:
#             paddleRightyChange = 5
#     if event.type == pygame.KEYUP:
#         if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#             paddleRightyChange = 0
#
#     if 0 < (paddleRighty + paddleRightyChange) < WINHEIGHT - 64:
#         paddleRighty += paddleRightyChange
#
#
#     #LEFT PADDLE MOVEMENT
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_w:
#             paddleLeftyChange = -5
#         elif event.key == pygame.K_s:
#             paddleLeftyChange = 5
#     if event.type == pygame.KEYUP:
#         if event.key == pygame.K_w or event.key == pygame.K_s:
#             paddleLeftyChange = 0
#
#     if 0 < (paddleLefty + paddleLeftyChange) < WINHEIGHT - 64:
#         paddleLefty += paddleLeftyChange
#
#
#     pygame.display.update()
#     clock.tick(FPS)
#
#
# def faggot():
#     print("faggot")