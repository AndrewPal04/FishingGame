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
from classes import Background, Player, Text

pygame.init()

# Screen setup
screen_width, screen_height = 1380, 900
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Starting screen
startScreenIMG = pygame.image.load("startMap.png")
startScreen = Background(screen, startScreenIMG, 0.9, 690, 450)

#User
rightTurnIMG = pygame.image.load("rightTurn.png")
leftTurnIMG = pygame.image.load("leftTurn.png")
downTurnIMG = pygame.image.load("downTurn.png")
upTurnIMG = pygame.image.load("upTurn.png")

#Fishing Text
nofish = Text(screen, "Can't fish here man!", 50, (255,255,255), 1200, 150)

#oxygen bar
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

#Mini game
#water background
waterIMG=pygame.image.load("water.png")
water=Background(screen,waterIMG,0.8452532525898325,690,450)

#fish that move around
fish1IMG=pygame.image.load("fish1.png")
fish1=Background(screen, fish1IMG,0.3,random.randint(100,1280), random.randint(100,800))

fish2IMG=pygame.image.load("fish2.png")
fish2=Background(screen, fish2IMG,.1,random.randint(100,1280), random.randint(100,800))

fish3IMG=pygame.image.load("fish3.png")
fish3=Background(screen, fish3IMG,0.5,random.randint(100,1280), random.randint(100,800))

harpoonIMG=pygame.image.load("harpoon.png")
harpoon=Background(screen, harpoonIMG,0.7,100,750)

sprite_group = pygame.sprite.Group()
sprite_group.add(bob)

minigame_group=pygame.sprite.Group()
minigame_group.add(fish1)
minigame_group.add(fish2)
minigame_group.add(fish3)
minigame_group.add(harpoon)
last_location = ""

def fishingMiniGame():
    start=time.time()
    #Choosing spots for fish movement
    spot1=(random.randint(100,1280),random.randint(100,800))
    spot2=(random.randint(100,1280),random.randint(100,800))
    spot3=(random.randint(100,1280),random.randint(100,800))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Workspace
        pos=pygame.mouse.get_pos()
        harpoon.rect.topright=pos
        end=time.time()
        water.draw()
        #Movement for fish 1
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
        
        #Movement for fish 2
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
            
        #Movement for fish 3
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


        if end-start>15:
            break

        pygame.display.update()
        clock.tick(60)

def mainLoop():
    global oxygen, oxygenTick, oxygenTickup, last_location
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #workspace
        startScreen.draw()
        sprite_group.draw(screen)
        bob.update(screen_width, screen_height)
        oxygenBars[oxygen].draw()

        fishing=pygame.mouse.get_pressed()[0] == 1

        #Create Bounds
        x = bob.rect.x
        y = bob.rect.y
        print("X:",x," Y:",y)

        #Water rectangles
        water1rect=pygame.Rect(0,0,250,900)#Left side
        water2rect=pygame.Rect(0,0,1380,80)#Top side
        water3rect=pygame.Rect(1110,0,270,900)#right sides
        water4rect=pygame.rect=(0,812,1380,88)#Bottom
        if bob.rect.colliderect(water1rect) or bob.rect.colliderect(water2rect) or bob.rect.colliderect(water3rect) or bob.rect.colliderect(water4rect):
            current_location = "water"
        landRect=pygame.Rect(250,80,860,732)
        if bob.rect.colliderect(landRect):
            current_location = "land"
        bridgeRect=pygame.Rect(632,725,90,73)
        if bob.rect.colliderect(bridgeRect):
            current_location = "bridge"


        #if they are in the water, lower their oxygen
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
                fishingMiniGame()
            elif current_location == "land":
                nofish.draw()



        pygame.display.update()
        clock.tick(60)

mainLoop()

#Homework
#


