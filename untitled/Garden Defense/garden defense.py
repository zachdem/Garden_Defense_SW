#Authors: Zach Demaris, Ryan Cerveny, Jacob Sandvig
#@COPYRIGHT 2017


#Test Commit

import pygame, sys
import ctypes
import time
from pygame.locals import *
import random
import tkinter

root = tkinter.Tk()
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
#windowHeight = 850
#windowWidth = 1550
windowHeight = root.winfo_screenheight()
windowWidth = root.winfo_screenwidth()
window = pygame.display.set_mode((windowWidth, windowHeight))
high_score = 0


def main():
    while True:
        mainScreen()
        instructions()
        game_loop(gnome)
        # gameEnd()


class Bunnies:
    def __init__(self, color, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.x = x

        self.y = y

        choice = random.randrange(0,2)
        if choice == 0:
            self.bunny = pygame.image.load("bunny.png")
        else:
            self.bunny =pygame.image.load("flybunny.png")

    def render(self):
        window.blit(self.bunny, (self.x, self.y))


class Bullets:
    def __init__(self, color, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.x = x

        self.y = y

        self.bullet = pygame.image.load("bullet.png")

    def render(self):
        window.blit(self.bullet, (self.x, self.y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def main_display(text, x, y, size):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    window.blit(TextSurf, TextRect)


def gameEnd(SCORE, ACCURACY):
    scareRabbit = pygame.image.load("creepRabb.png")
    scare = pygame.image.load("blood.png")
    window.blit(scare, (0,0))
    window.blit(scareRabbit, (windowWidth/2, windowHeight/2))
    main_display('GAME OVER', windowWidth/2, windowHeight/2, 80)
    main_display("SCORE: " + str((int)(SCORE * (ACCURACY))), windowWidth/2, windowHeight/2 - 100, 50)
    pygame.display.update()
    #death = pygame.mixer.Sound("death.wav")  ---optional scream when fail
   #pygame.mixer.Sound.play(death)
    time.sleep(5)


def instructions():
    window.fill(black)
    main_display("Defend your Carrots from the Invading Rabbits...", windowWidth / 2, 50, 30)
    main_display("Push Up/Down to move", windowWidth / 2, 90, 30)
    main_display("Push Space to shoot", windowWidth / 2, 130, 30)
    main_display("Hint: Your Score is Determined by Kills * Accuracy", windowWidth / 2, 180, 30)
    main_display("GOOD LUCK AND THANKS FOR PLAYING!!!", windowWidth / 2, windowHeight - 100, 30)

    pygame.display.update()
    time.sleep(8)

def mainScreen():
    global gnome
    global high_score
    gnum = 0
    t = pygame.time.get_ticks()
    musicTime = 0

    mainScreenBackground = pygame.image.load("mainScreen.jpg")
    window.blit(mainScreenBackground, (0, 0))
    main_display("Garden Defense", windowWidth/2, 200, 80)
    elevatormusic = pygame.mixer.Sound("elevatormusic.wav")
    pygame.mixer.Sound.play(elevatormusic)
    musicTime = t

    gnome1 = pygame.image.load("knome1.png")
    gnome2 = pygame.image.load("knome2.png")
    gnome3 = pygame.image.load("knome3.png")

    window.blit(gnome1, ((windowWidth / 3), (windowHeight / 2)))
    window.blit(gnome2, ((windowWidth / 2), (windowHeight / 2)))
    window.blit(gnome3, (2 * windowWidth / 3, windowHeight / 2))

    main_display("1", (windowWidth / 3) + 30, (windowHeight / 2) + 150, 50)
    main_display("2", (windowWidth / 2) + 30, (windowHeight / 2) + 150, 50)
    main_display("3", (2 * windowWidth / 3) + 30, (windowHeight / 2) + 150, 50)
    main_display("Choose Your Gnomeber. (Type 1, 2, or 3)", (windowWidth / 2) + 30, (windowHeight / 2) + 300, 50)
    main_display("High Score: " + str((int) (high_score)), windowWidth/2, 290, 55)


    pygame.display.update()





    while gnum == 0:
        global event

        t = pygame.time.get_ticks()
        if t > musicTime + 195000:
            pygame.mixer.Sound.play(elevatormusic)
            musicTime = t


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] or keys[pygame.K_KP1]:
            gnum = 1
            gnome = gnome1
            pygame.mixer.Sound.stop(elevatormusic)
        elif keys[pygame.K_2] or keys[pygame.K_KP2]:
            gnum = 1
            gnome = gnome2
            pygame.mixer.Sound.stop(elevatormusic)
        elif keys[pygame.K_3] or keys[pygame.K_KP3]:
            gnum = 1
            gnome = gnome3
            pygame.mixer.Sound.stop(elevatormusic)




def game_loop(GNOME):

    #definitions
    gnome = GNOME
    FPS = 60
    gardenBackground = pygame.image.load("garden2.jpg")
    explosion = pygame.image.load("explosion.png")
    carrot = pygame.image.load("carrots.png")
    clock = pygame.time.Clock()
    newtime = 0
    numberOfLives = 4
    difficultyfactor = 1
    global high_score
    recPress = False
    bulletCount = 1
    bulletHit = 1
    score = 0

    bunnyGroup = pygame.sprite.Group()
    bulletGroup = pygame.sprite.Group()

    gnomepositionx = 200
    gnomepositiony = 600
    gnomepositionychange = 0

    pressed_up = False
    pressed_down = False
    pressed_space = False

    elevatormusic = pygame.mixer.Sound("elevatormusic.wav")
    pygame.mixer.Sound.play(elevatormusic)


    while numberOfLives > 0:

        window.blit(gardenBackground, (0, 0))
        window.blit(gnome, (gnomepositionx, gnomepositiony))
        main_display("Kills: " + str(score), 70, 30, 30)
        main_display("Carrots: " + str(numberOfLives), 83, 65, 30)
        main_display("Accuracy: " + str((int) ((bulletHit/bulletCount)*100)) + "%", 120, 100, 30)


        t = pygame.time.get_ticks()
        global event

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:  # up arrow goes up
                    pressed_up = True

                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    pressed_down = True

                elif event.key == pygame.K_SPACE:
                    pressed_space = True


            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:  # up arrow goes up
                    pressed_up = False

                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    pressed_down = False

                elif event.key == pygame.K_SPACE:  # down arrow goes down
                    pressed_space = False
                    recPress = False

        if pressed_up:
            gnomepositionychange = -7
        elif pressed_down:
            gnomepositionychange = 7
        elif not pressed_down and not pressed_up:
            gnomepositionychange = 0






        if pressed_space and not recPress:
            bullet = Bullets(black, gnomepositionx + 50, gnomepositiony + 50)
            bulletGroup.add(bullet)
            recPress = True
            bulletCount += 1

        if 325 < (gnomepositiony + gnomepositionychange) < 722:
           gnomepositiony += gnomepositionychange

        if t > newtime + (2000/difficultyfactor):
            bunny = Bunnies(black,windowWidth + 100,random.randrange(325, 722))
            bunnyGroup.add(bunny)
            newtime = t

        if numberOfLives == 4:
            window.blit(carrot, (75, windowHeight - 100))
            window.blit(carrot, (75, windowHeight - 200))
            window.blit(carrot, (75, windowHeight - 300))
            window.blit(carrot, (75, windowHeight - 400))

        if numberOfLives == 3:
            window.blit(carrot, (75, windowHeight - 100))
            window.blit(carrot, (75, windowHeight - 200))
            window.blit(carrot, (75, windowHeight - 300))

        if numberOfLives == 2:
            window.blit(carrot, (75, windowHeight - 100))
            window.blit(carrot, (75, windowHeight - 200))

        if numberOfLives == 1:
            window.blit(carrot, (75, windowHeight - 100))

        for bunny in bunnyGroup:
            bunny.x -= 4 * difficultyfactor
            Bunnies.render(bunny)
            if bunny.x <= 100:
                bunnyGroup.remove(bunny)
                numberOfLives -= 1



        for bullet in bulletGroup:

            bullet.x += 10
            Bullets.render(bullet)
            if bullet.x >= windowWidth:
                bulletGroup.remove(bullet)


        for bullet in bulletGroup:
            for bunny in bunnyGroup:
                if bullet.x > bunny.x and bunny.y + 100 > bullet.y > bunny.y:
                    bulletGroup.remove(bullet)
                    bunnyGroup.remove(bunny)
                    window.blit(explosion, (bunny.x, bunny.y))
                    score += 1
                    bulletHit += 1

        difficultyfactor += .0009
        pygame.display.update()
        clock.tick(FPS)
    pygame.mixer.Sound.stop(elevatormusic)
    if score * (bulletHit / bulletCount) > high_score:
        high_score = (score * (bulletHit / bulletCount))
    gameEnd(score, (bulletHit/bulletCount))




















