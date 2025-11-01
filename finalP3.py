#Final Project Python 3
# 2. fishing game
# 	- upgrades, islands, boats, companions
#   - deserted island map
#   - someone comes to buy fish
#   - buy better rods and bait
#   - eventually buy friends to catch fish
#   - you have to pay an hourly wage
#   - option to buy a boat
#   - go to the ocean to find fish
#   - you can get weapons to fight sharks or bosses

import pygame
import time
import random
from classes import Background, Player, Text, Button

pygame.init()

screen_width, screen_height = 1380, 900
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

startScreenIMG = pygame.image.load("startMap.png")
startScreen = Background(screen, startScreenIMG, 0.9, 690, 450)

rightTurnIMG = pygame.image.load("rightTurn.png")
leftTurnIMG = pygame.image.load("leftTurn.png")
downTurnIMG = pygame.image.load("downTurn.png")
upTurnIMG = pygame.image.load("upTurn.png")

nofish = Text(screen, "Can't fish here man!", 50, (255,255,255), 1200, 150)

oBar0IMG = pygame.image.load("oBar0.png")
oBar1IMG = pygame.image.load("oBar1.png")
oBar2IMG = pygame.image.load("oBar2.png")
oBar3IMG = pygame.image.load("oBar3.png")
oBar4IMG = pygame.image.load("oBar4.png")

oxygenBars = [
    Background(screen, oBar0IMG, 2, 150, 850),
    Background(screen, oBar1IMG, 2, 150, 850),
    Background(screen, oBar2IMG, 2, 150, 850),
    Background(screen, oBar3IMG, 2, 150, 850),
    Background(screen, oBar4IMG, 2, 150, 850)
]

oxygenTick=125
oxygenTickup=200
oxygen = 4
spriteImages = [rightTurnIMG, leftTurnIMG, downTurnIMG, upTurnIMG]

bob = Player(spriteImages, 0.1, 750, 450, 2)

waterIMG=pygame.image.load("water.png")
water=Background(screen,waterIMG,0.8452532525898325,690,450)

fish1IMG=pygame.image.load("fish1.png")
fish1=Background(screen, fish1IMG,0.3,random.randint(100,1280), random.randint(100,800))
fish2IMG=pygame.image.load("fish2.png")
fish2=Background(screen, fish2IMG,.1,random.randint(100,1280), random.randint(100,800))
fish3IMG=pygame.image.load("fish3.png")
fish3=Background(screen, fish3IMG,0.5,random.randint(100,1280), random.randint(100,800))

harpoonIMG=pygame.image.load("harpoon.png")
harpoon=Background(screen, harpoonIMG,0.7,100,750)

fishButtonIMG = pygame.image.load("FISHBUTTON.png")

sprite_group = pygame.sprite.Group()
sprite_group.add(bob)

minigame_group=pygame.sprite.Group()
minigame_group.add(fish1)
minigame_group.add(fish2)
minigame_group.add(fish3)
minigame_group.add(harpoon)
last_location = ""

cod_caught = False
angler_caught = False
shark_caught = False

codIMG = pygame.image.load("fish1.png")
anglerIMG = pygame.image.load("fish2.png")
sharkIMG = pygame.image.load("fish3.png")

cod_display_big = Background(screen, codIMG, 0.9, 690, 450)
angler_display_big = Background(screen, anglerIMG, 0.3, 690, 450)
shark_display_big = Background(screen, sharkIMG, 1.5, 690, 450)

caught_cod_text = Text(screen, "You caught a Cod!", 80, (255,255,255), 500, 150)
caught_angler_text = Text(screen, "You caught an Anglerfish!", 80, (255,255,255), 350, 150)
caught_shark_text = Text(screen, "You caught a Shark!", 80, (255,255,255), 500, 150)

caught_message = None
caught_timer = 0

cods=0
anglers=0
sharks=0
money=0

moneyText=Text(screen, "Money: $"+str(money), 50, (0,0,0), 1190, 50)

def newScreen(currentMoney):
    global cods, anglers, sharks
    option1=Text(screen, "a. Sell All Fish", 50, (255,255,255), screen_width/2, 200)
    option2=Text(screen, "b. close", 50, (255,255,255), screen_width/2, 300)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((0,0,0))
        keystate=pygame.key.get_pressed()
        option1.draw()
        option2.draw()
        if keystate[pygame.K_a]:
            while cods>0:
                currentMoney+=5
                cods-=1
            while anglers>0:
                currentMoney+=20
                anglers-=1
            while sharks>0:
                currentMoney+=100
                sharks-=1
                
        if keystate[pygame.K_b]:
            break
        pygame.display.update()
        clock.tick(60)
    return currentMoney

def fishingMiniGame():
    global cod_caught, angler_caught, shark_caught
    pygame.mixer.music.load("reel.mp3") 
    cod_caught=False
    angler_caught=False
    shark_caught=False
    fish1clicks=0
    fish2clicks=0
    fish3clicks=0
    if fish1 not in minigame_group:
        minigame_group.add(fish1)
    if fish2 not in minigame_group:
        minigame_group.add(fish2)
    if fish3 not in minigame_group:
        minigame_group.add(fish3)

    start=time.time()
    spot1=(random.randint(100,1280),random.randint(100,800))
    spot2=(random.randint(100,1280),random.randint(100,800))
    spot3=(random.randint(100,1280),random.randint(100,800))

    fish1_button = Button(screen, fishButtonIMG, 0.1, fish1.rect.x, fish1.rect.y - 50)
    fish2_button = Button(screen, fishButtonIMG, 0.15, fish2.rect.x, fish2.rect.y - 50)
    fish3_button = Button(screen, fishButtonIMG, 0.25, fish3.rect.x, fish3.rect.y - 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pos=pygame.mouse.get_pos()
        harpoon.rect.topright=pos
        end=time.time()
        water.draw()
        if fish1.rect.x<spot1[0]:
            fish1.rect.x+=3
        if fish1.rect.x>spot1[0]:
            fish1.rect.x-=3
        if fish1.rect.y<spot1[1]:
            fish1.rect.y+=3
        if fish1.rect.y>spot1[1]:
            fish1.rect.y-=3
        if abs(fish1.rect.x-spot1[0])<5 and abs(fish1.rect.y-spot1[1])<5:
            spot1=(random.randint(100,1280),random.randint(100,800))

        if fish2.rect.x<spot2[0]:
            fish2.rect.x+=3
        if fish2.rect.x>spot2[0]:
            fish2.rect.x-=3
        if fish2.rect.y<spot2[1]:
            fish2.rect.y+=3
        if fish2.rect.y>spot2[1]:
            fish2.rect.y-=3
        if abs(fish2.rect.x-spot2[0])<5 and abs(fish2.rect.y-spot2[1])<5:
            spot2=(random.randint(100,1280),random.randint(100,800))

        if fish3.rect.x<spot3[0]:
            fish3.rect.x+=5
        if fish3.rect.x>spot3[0]:
            fish3.rect.x-=5
        if fish3.rect.y<spot3[1]:
            fish3.rect.y+=5
        if fish3.rect.y>spot3[1]:
            fish3.rect.y-=5
        if abs(fish3.rect.x-spot3[0])<6 and abs(fish3.rect.y-spot3[1])<6:
            spot3=(random.randint(100,1280),random.randint(100,800))

        minigame_group.draw(screen)

        fish1_button.rect.centerx, fish1_button.rect.y = fish1.rect.centerx, fish1.rect.y - 30
        fish2_button.rect.centerx, fish2_button.rect.y = fish2.rect.centerx, fish2.rect.y - 40
        fish3_button.rect.centerx, fish3_button.rect.y = fish3.rect.centerx, fish3.rect.y - 45

        if fish1 in minigame_group:
            if fish1_button.draw():
                pygame.mixer.music.play()
                fish1clicks+=1
            if fish1clicks==2:
                minigame_group.remove(fish1)
                cod_caught=True
        if fish2 in minigame_group:
            if fish2_button.draw():
                pygame.mixer.music.play()
                fish2clicks+=1
            if fish2clicks==3:
                minigame_group.remove(fish2)
                angler_caught=True
        if fish3 in minigame_group:
            if fish3_button.draw():
                pygame.mixer.music.play()
                fish3clicks+=1
            if fish3clicks==5:
                minigame_group.remove(fish3)
                shark_caught=True

        if end-start>4:
            break

        pygame.display.update()
        clock.tick(60)

    return cod_caught, angler_caught, shark_caught

def mainLoop():
    global oxygen, oxygenTick, oxygenTickup, last_location, caught_message, caught_timer, money, moneyText, cods, anglers, sharks
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        startScreen.draw()
        sprite_group.draw(screen)
        bob.update(screen_width, screen_height)
        oxygenBars[oxygen].draw()
        moneyText=Text(screen, "Money: $"+str(money), 50, (0,0,0), 1190, 50)
        moneyText.draw()

        fishing=pygame.mouse.get_pressed()[0] == 1

        x = bob.rect.x
        y = bob.rect.y
        print("X:",x," Y:",y)
        doorRect=pygame.Rect(925,500,36,57)
        water1rect=pygame.Rect(0,0,250,900)
        water2rect=pygame.Rect(0,0,1380,80)
        water3rect=pygame.Rect(1110,0,270,900)
        water4rect=pygame.rect=(0,812,1380,88)
        if bob.rect.colliderect(water1rect) or bob.rect.colliderect(water2rect) or bob.rect.colliderect(water3rect) or bob.rect.colliderect(water4rect):
            current_location = "water"
        landRect=pygame.Rect(250,80,860,732)
        if bob.rect.colliderect(landRect):
            current_location = "land"
        bridgeRect=pygame.Rect(632,725,90,73)
        if bob.rect.colliderect(bridgeRect):
            current_location = "bridge"

        if current_location == "water":
            oxygenTick-=1
            if oxygenTick<1:
                oxygen-=1
                oxygenTick=125

        if current_location == "land" or current_location == "bridge":
            if oxygen<4:
                oxygenTickup-=1
                if oxygenTickup<1:
                    oxygen+=1
                    oxygenTickup=200

        if fishing:
            if current_location == "bridge" or current_location == "water":
                c_caught, a_caught, s_caught = fishingMiniGame()
                global cod_caught, angler_caught, shark_caught
                if c_caught:
                    cods+=1
                    cod_caught = True
                    caught_message = "cod"
                    caught_timer = time.time()
                if a_caught:
                    anglers+=1
                    angler_caught = True
                    caught_message = "angler"
                    caught_timer = time.time()
                if s_caught:
                    sharks+=1
                    shark_caught = True
                    caught_message = "shark"
                    caught_timer = time.time()
            elif current_location == "land":
                nofish.draw()

        if caught_message:
            elapsed = time.time() - caught_timer
            if elapsed < 3:
                if caught_message == "cod":
                    cod_display_big.draw()
                    caught_cod_text.draw()
                elif caught_message == "angler":
                    angler_display_big.draw()
                    caught_angler_text.draw()
                elif caught_message == "shark":
                    shark_display_big.draw()
                    caught_shark_text.draw()
            else:
                caught_message = None
        if bob.rect.colliderect(doorRect):
            money=newScreen(money)
            bob.rect.x=800
            bob.rect.y=500
        pygame.display.update()
        clock.tick(60)

mainLoop()

#GITHUB REPO
#    https://github.com/AndrewPal04/FishingGame

#Open the link above and click code
#After, click download ZIP
#Then, right click the ZIP and extract all
#Then you can open that folder in your VS Code and you will have
#everything exactly like how I do


#Homework
#Using the link below, start creating your final presentation
#Follow the instructions on the slides to fill out each one
#and feel free to look at your past presentations if you 
#forgot what to put on each slide
#Good Luck!
# https://docs.google.com/presentation/d/1SvjGVSDHrpJ3E__emNbEpPLVFicQvc0u9rTCRFXXVmg/edit#slide=id.p