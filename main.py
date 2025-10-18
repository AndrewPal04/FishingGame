#Welcome to Python 3!!

#Object-Oriented-Programming (OOP)

#Creating a class:
# class Cat:
#     def __init__(self, name, age, color, baldness):
#         self.name=name
#         self.age=age
#         self.color=color
#         self.baldness=baldness
#     def yawn(self):
#         print(self.name, "yawned!")
#     def eat(self, food):
#         print(self.name,"ate some",food)
#     def hunt(self):
#         return "rat"

# #Creating objects using the class
# cat1=Cat("Garfield",47,"Orange","Not Bald")
# dog2=Cat("pug",1,"brownish-yellow","baldish")

#Using attributes

# print("Andrew's cat is named",cat1.name)
# print("Benson's dog is named",dog2.name)
# #Print out, "___ is the color ___" for your 'cat'

# print(dog2.name, "is",dog2.color)
# print(cat1.name,"is",cat1.color)

# print("Next year,",cat1.name,"will be",cat1.age + 1,"years old!")
# print("But he is still",cat1.age)
# cat1.age+=1
# print("It's been a year, Garfield is now",cat1.age)

#Using methods

# cat1.yawn()
# dog2.yawn()

# cat1.eat("lasagna")
# dog2.eat("chocolate")

# item=cat1.hunt()
# print(cat1.name,"brought me a",item)

#Create a class for a lemonade stand
#The lemonade stand should have attributes like cups_of_lemonade, money, name, and price

# import random

# class lemonade_stand:
#     def __init__(self, cups, lemons, money, name, price, level):
#         self.cups = cups
#         self.lemons = lemons
#         self.money = money
#         self.name = name
#         self.price = price
#         self.level = level

#     def restock(self):
#         if self.money >= 3:
#             print(self.name, "purchased lemons.")
#             self.lemons += 5
#             self.money -= 3
#         else:
#             print(self.name, "is broke.")

#     def make_lemonade(self):
#         if self.lemons > 0:
#             print(self.name, "made some lemonade!")
#             self.lemons -= 1
#             self.cups += 1
#         else:
#             print(self.name, "is out of lemons!")

#     def sell(self):
#         if self.cups > 0:
#             print(self.name, "sold a cup of lemonade!")
#             print("You made", self.price, "Euros!")
#             self.cups -= 1
#             self.money += self.price
#         else:
#             print(self.name, "is out of cups of lemonade!")

#     def stats(self):
#         print("\n--- Stand Stats ---")
#         print("Name:", self.name)
#         print("Euros:", self.money)
#         print("Cups:", self.cups)
#         print("Lemons:", self.lemons)
#         print("Stand Level:", self.level)
#         print("-------------------\n")

#     def adv(self):
#         if self.level == 0:
#             if self.money >= 100:
#                 print(self.name, "got a commercial plane to advertise!")
#                 print("You are now level 1!\n")
#                 self.level += 1
#                 self.money -= 100
#                 self.price += 10
#             else:
#                 print(self.name, "doesn't have enough for an ad...\nYou flew an ad over your stand and it made customers run away!")
#         elif self.level == 1:
#             if self.money >= 10000:
#                 print(self.name, "got a contrail to draw and show off your stand by bombing a wedding, that was by Elon Musk!")
#                 print("You are now level 2!\n")
#                 self.level += 1
#                 self.money -= 10000
#                 self.price += 713
#             else:
#                 print(self.name, "'s customers went on a yacht to drink 2 dollar lemonade by X Æ A-Xii.")
#         else:
#             print("You are already max level... more levels tomorrow!")

#     def bankruptcy(self):
#         print("\n Oh no you really just got robbed!")

#         # Safe money loss
#         if self.money > 0:
#             stolen_money = random.randint(1, self.money)
#         else:
#             stolen_money = 0
#         self.money -= stolen_money

#         # Random lemons and cups taken, but not more than available
#         stolen_lemons = random.randint(1, 3)
#         stolen_cups = random.randint(1, 3)

#         actual_stolen_lemons = min(self.lemons, stolen_lemons)
#         actual_stolen_cups = min(self.cups, stolen_cups)

#         self.lemons -= actual_stolen_lemons
#         self.cups -= actual_stolen_cups

#         print(f"The robber stole {stolen_money} Euros, {actual_stolen_lemons} lemons, and {actual_stolen_cups} cups!\n")

# # Create lemonade stand
# water = lemonade_stand(1, 1, 0, "good lemons", 3, 0)

# # Game Loop
# while True:
#     # Random chance of robbery (1 in 10)
#     if random.randint(1, 10) == 1:
#         water.bankruptcy()

#     print("1. Buy lemons\n2. Make cups\n3. Sell cups\n4. View stats\n5. Advertise\n6. Quit")

#     try:
#         choice = int(input("> "))
#     except ValueError:
#         print("nuh uh. please enter a number.\n")
#         continue

#     if choice == 1:
#         water.restock()
#     elif choice == 2:
#         water.make_lemonade()
#     elif choice == 3:
#         water.sell()
#     elif choice == 4:
#         water.stats()
#     elif choice == 5:
#         water.adv()
#     elif choice == 6:
#         print("retired from all that richness you made")
#         break
#     else:
#         print("nuh uh. try again.\n")

# idea - add staff members, allow bulk sell/buy option

# Homework
# Robbery - create a method where you get robbed, and you lose a random amount of money, and 1-3 cups of lemonade, and 1-3 lemons
# tell the user (print) that they got robbed
# Pick a random number 1-max
# Remove the money from the user
# Pick two numbers 1-3, and remove that many lemons/cups
# Tell the user what they lost
# Make sure the amount of money you have after getting robbed isn't negative

#PYGAME

# import pygame  #If you do this on vs code, you might have to type "pip install pygame" in the terminal

# pygame.init()

# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# #Game Loop

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace

#     #var  =pygame.draw.rect(surface, (RGB),(X,Y,Width,Height))
#     square1 = pygame.draw.rect(screen, (0, 255, 0), (500, 250, 100, 200))

#     cube2 = pygame.draw.rect(screen, (121, 121, 121), (100, 210, 122, 212))

#     #var = pygame.draw.circle(surface, (R,G,B),(X,Y),Radius)
#     circle1 = pygame.draw.circle(screen, (100, 0, 120), (500, 300), 50)
#     circle3 = pygame.draw.circle(screen, (252, 3, 3), (950, 450), 40)

#     #var=pygame.draw.line(surface, (R.G.B), (start x,y), (end x,y), width)
#     line1 = pygame.draw.line(screen, (255, 255, 255), (0, 0), (1000, 500), 10)
#     line2 = pygame.draw.line(screen, (3, 215, 252), (10,10), (200,210), 10)

#     #var=pygame.draw.polygon(surface, (R.G.B),[(coordinate1),(coordinate2),etc.])
#     yellow_triangle = pygame.draw.polygon(screen, (248, 252, 3), [(10, 300), (40, 200), (70, 300) ])
#     pink_pentagon = pygame.draw.polygon(screen, (255, 0, 230), [(146, 300), (272, 370), (236, 495), (56, 495), (20, 370)])

#     pygame.display.update()
#     clock.tick(60)

#Create your own pygame loop, and draw an emoji face using circles and lines
# import pygame
# pygame.init()

# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     face = pygame.draw.circle(screen, (240, 252, 3),(500, 250),200)
#     eye1 = pygame.draw.circle(screen, (41, 41, 38), (400, 150), 25)
#     eye2 = pygame.draw.circle(screen, (41, 41, 38), (600, 150), 25)
#     mouth = pygame.draw.line(screen, (255, 0, 230), (425, 275), (575, 275), 25)

#     pygame.display.update()
#     clock.tick(60)

#Keystate

# import pygame

# pygame.init()
# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500

# screen = pygame.display.set_mode((screen_width, screen_height))
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((0,0,0))
#     keystate = pygame.key.get_pressed()  #Tracks what keys the user presses

#     if keystate[pygame.K_a]:
#         square = pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 50))
#     if keystate[pygame.K_UP]:
#         print("Bye")

#     pygame.display.update()
#     clock.tick(60)

#Homework
#Create a game loop so that when the user clicks certain buttons, different things pop up on the screen
#When they click UP, draw a blue circle
#When they clock DOWN, draw a red square
#When they click RIGHT, draw a green line
#When they click LEFT, draw an emoji
#When they click tab, draw a checkerboard pattern (lines)
#OPTIONAL: when they click the space bar, draw a blue sky, with green grass(rectangle) and a snowman (3 white circles)

#Good Luck!

#Link for keystate codes: https://www.pygame.org/docs/ref/key.html

# import pygame
# import sys

# pygame.init()
# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     #workspace
#     screen.fill((204, 6, 5))
#     keystate = pygame.key.get_pressed()

#     if keystate[pygame.K_UP]:
#         pygame.draw.circle(screen, (16, 44, 84), (500, 250), 100)

#     if keystate[pygame.K_DOWN]:
#         pygame.draw.rect(screen, (175, 43, 30), (450, 200, 100, 100))

#     if keystate[pygame.K_RIGHT]:
#         pygame.draw.line(screen, (30, 89, 69), (100, 250), (900, 250), 5)

#     if keystate[pygame.K_LEFT]:
#         pygame.draw.circle(screen, (255, 204, 0), (500, 250), 100)
#         pygame.draw.circle(screen, (0, 0, 0), (450, 215), 10)
#         pygame.draw.circle(screen, (0, 0, 0), (550, 215), 10)
#         pygame.draw.line(screen, (0, 0, 0), (460, 300), (540, 300), 5)

#     if keystate[pygame.K_TAB]:
#         cell_size = 50
#         for x in range(0, screen_width, cell_size):
#             pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, screen_height), 1)
#         for y in range(0, screen_height, cell_size):
#             pygame.draw.line(screen, (255, 255, 255), (0, y), (screen_width, y), 1)

#     if keystate[pygame.K_SPACE]:
#         screen.fill((135, 206, 235))
#         pygame.draw.rect(screen, (34, 139, 34), (0, 400, screen_width, 100))
#         pygame.draw.circle(screen, (255, 255, 255), (500, 350), 40)
#         pygame.draw.circle(screen, (255, 255, 255), (500, 290), 30)
#         pygame.draw.circle(screen, (255, 255, 255), (500, 240), 20)

#     pygame.display.update()
#     clock.tick(60)

#Class: Text

# import pygame
# pygame.init()
# #Tells you what fonts you can use:
# # print(pygame.font.get_fonts())

# class Text():
#     def __init__(self, surface, text, size, color, x, y):
#         font_name = pygame.font.match_font("microsofthimalaya")
#         self.surface = surface
#         self.text = text
#         self.size = size
#         self.font = pygame.font.Font(font_name, self.size)
#         self.color = color
#         self.x = x
#         self.y = y

#     def draw(self):
#         text_surface = self.font.render(self.text, True, self.color)
#         text_rect = text_surface.get_rect()
#         text_rect.midtop = (self.x, self.y)
#         self.surface.blit(text_surface, text_rect)

# screen_width, screen_height=1000,500
# screen=pygame.display.set_mode((screen_width,screen_height))
# clock=pygame.time.Clock()

# #create a text object
# text1=Text(screen,"CoPilot",200,(150,0,160),500,10)
# text2=Text(screen,"hello there",100,(200,255,255),500,250)
# text3=Text(screen,"stop pressing c",100,(200,255,255),500,250)
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     screen.fill((255,255,255))
#     keystate=pygame.key.get_pressed()
#     if keystate[pygame.K_a]:
#         text1.draw()
#     if keystate[pygame.K_b]:
#         text2.draw()
#     if keystate[pygame.K_c]:
#         text3.draw()
#     pygame.display.update()
#     clock.tick(60)

# Homework
# Bring back the program you created last week for homework
# Notice that there are no instructions for how to draw the different shapes/objects you made
# Use the text class you created in today's meeting, create multiple instructions texts so that
# the user will know how to draw each shape
# Use texts like "press a to draw a circle", "press b to draw square", etc.
# Good Luck!

#Music/Audio Files

# import pygame
# pygame.init()
# screen_width,screen_height=1000,500
# screen=pygame.display.set_mode((screen_width,screen_height))
# clock=pygame.time.Clock()

# pygame.mixer.init()

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     keystate=pygame.key.get_pressed()
#     if keystate[pygame.K_a]:
#         pygame.mixer.music.load("music.mp3")
#         pygame.mixer.music.play()

#     pygame.display.update()
#     clock.tick(60)

#Welcome to Python 3!!

#Object-Oriented-Programming (OOP)

#Creating a class:
# class Cat:
#     def __init__(self, name, age, color, baldness):
#         self.name=name
#         self.age=age
#         self.color=color
#         self.baldness=baldness
#     def yawn(self):
#         print(self.name, "yawned!")
#     def eat(self, food):
#         print(self.name,"ate some",food)
#     def hunt(self):
#         return "rat"

# #Creating objects using the class
# cat1=Cat("Garfield",47,"Orange","Not Bald")
# dog2=Cat("pug",1,"brownish-yellow","baldish")

#Using attributes

# print("Andrew's cat is named",cat1.name)
# print("Benson's dog is named",dog2.name)
# #Print out, "___ is the color ___" for your 'cat'

# print(dog2.name, "is",dog2.color)
# print(cat1.name,"is",cat1.color)

# print("Next year,",cat1.name,"will be",cat1.age + 1,"years old!")
# print("But he is still",cat1.age)
# cat1.age+=1
# print("It's been a year, Garfield is now",cat1.age)

#Using methods

# cat1.yawn()
# dog2.yawn()

# cat1.eat("lasagna")
# dog2.eat("chocolate")

# item=cat1.hunt()
# print(cat1.name,"brought me a",item)

#Create a class for a lemonade stand
#The lemonade stand should have attributes like cups_of_lemonade, money, name, and price

# import random

# class lemonade_stand:
#     def __init__(self, cups, lemons, money, name, price, level):
#         self.cups = cups
#         self.lemons = lemons
#         self.money = money
#         self.name = name
#         self.price = price
#         self.level = level

#     def restock(self):
#         if self.money >= 3:
#             print(self.name, "purchased lemons.")
#             self.lemons += 5
#             self.money -= 3
#         else:
#             print(self.name, "is broke.")

#     def make_lemonade(self):
#         if self.lemons > 0:
#             print(self.name, "made some lemonade!")
#             self.lemons -= 1
#             self.cups += 1
#         else:
#             print(self.name, "is out of lemons!")

#     def sell(self):
#         if self.cups > 0:
#             print(self.name, "sold a cup of lemonade!")
#             print("You made", self.price, "Euros!")
#             self.cups -= 1
#             self.money += self.price
#         else:
#             print(self.name, "is out of cups of lemonade!")

#     def stats(self):
#         print("\n--- Stand Stats ---")
#         print("Name:", self.name)
#         print("Euros:", self.money)
#         print("Cups:", self.cups)
#         print("Lemons:", self.lemons)
#         print("Stand Level:", self.level)
#         print("-------------------\n")

#     def adv(self):
#         if self.level == 0:
#             if self.money >= 100:
#                 print(self.name, "got a commercial plane to advertise!")
#                 print("You are now level 1!\n")
#                 self.level += 1
#                 self.money -= 100
#                 self.price += 10
#             else:
#                 print(self.name, "doesn't have enough for an ad...\nYou flew an ad over your stand and it made customers run away!")
#         elif self.level == 1:
#             if self.money >= 10000:
#                 print(self.name, "got a contrail to draw and show off your stand by bombing a wedding, that was by Elon Musk!")
#                 print("You are now level 2!\n")
#                 self.level += 1
#                 self.money -= 10000
#                 self.price += 713
#             else:
#                 print(self.name, "'s customers went on a yacht to drink 2 dollar lemonade by X Æ A-Xii.")
#         else:
#             print("You are already max level... more levels tomorrow!")

#     def bankruptcy(self):
#         print("\n Oh no you really just got robbed!")

#         # Safe money loss
#         if self.money > 0:
#             stolen_money = random.randint(1, self.money)
#         else:
#             stolen_money = 0
#         self.money -= stolen_money

#         # Random lemons and cups taken, but not more than available
#         stolen_lemons = random.randint(1, 3)
#         stolen_cups = random.randint(1, 3)

#         actual_stolen_lemons = min(self.lemons, stolen_lemons)
#         actual_stolen_cups = min(self.cups, stolen_cups)

#         self.lemons -= actual_stolen_lemons
#         self.cups -= actual_stolen_cups

#         print(f"The robber stole {stolen_money} Euros, {actual_stolen_lemons} lemons, and {actual_stolen_cups} cups!\n")

# # Create lemonade stand
# water = lemonade_stand(1, 1, 0, "good lemons", 3, 0)

# # Game Loop
# while True:
#     # Random chance of robbery (1 in 10)
#     if random.randint(1, 10) == 1:
#         water.bankruptcy()

#     print("1. Buy lemons\n2. Make cups\n3. Sell cups\n4. View stats\n5. Advertise\n6. Quit")

#     try:
#         choice = int(input("> "))
#     except ValueError:
#         print("nuh uh. please enter a number.\n")
#         continue

#     if choice == 1:
#         water.restock()
#     elif choice == 2:
#         water.make_lemonade()
#     elif choice == 3:
#         water.sell()
#     elif choice == 4:
#         water.stats()
#     elif choice == 5:
#         water.adv()
#     elif choice == 6:
#         print("retired from all that richness you made")
#         break
#     else:
#         print("nuh uh. try again.\n")

# idea - add staff members, allow bulk sell/buy option

# Homework
# Robbery - create a method where you get robbed, and you lose a random amount of money, and 1-3 cups of lemonade, and 1-3 lemons
# tell the user (print) that they got robbed
# Pick a random number 1-max
# Remove the money from the user
# Pick two numbers 1-3, and remove that many lemons/cups
# Tell the user what they lost
# Make sure the amount of money you have after getting robbed isn't negative

#PYGAME

# import pygame  #If you do this on vs code, you might have to type "pip install pygame" in the terminal

# pygame.init()

# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# #Game Loop

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace

#     #var  =pygame.draw.rect(surface, (RGB),(X,Y,Width,Height))
#     square1 = pygame.draw.rect(screen, (0, 255, 0), (500, 250, 100, 200))

#     cube2 = pygame.draw.rect(screen, (121, 121, 121), (100, 210, 122, 212))

#     #var = pygame.draw.circle(surface, (R,G,B),(X,Y),Radius)
#     circle1 = pygame.draw.circle(screen, (100, 0, 120), (500, 300), 50)
#     circle3 = pygame.draw.circle(screen, (252, 3, 3), (950, 450), 40)

#     #var=pygame.draw.line(surface, (R.G.B), (start x,y), (end x,y), width)
#     line1 = pygame.draw.line(screen, (255, 255, 255), (0, 0), (1000, 500), 10)
#     line2 = pygame.draw.line(screen, (3, 215, 252), (10,10), (200,210), 10)

#     #var=pygame.draw.polygon(surface, (R.G.B),[(coordinate1),(coordinate2),etc.])
#     yellow_triangle = pygame.draw.polygon(screen, (248, 252, 3), [(10, 300), (40, 200), (70, 300) ])
#     pink_pentagon = pygame.draw.polygon(screen, (255, 0, 230), [(146, 300), (272, 370), (236, 495), (56, 495), (20, 370)])

#     pygame.display.update()
#     clock.tick(60)

#Create your own pygame loop, and draw an emoji face using circles and lines
# import pygame
# pygame.init()

# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500
# screen = pygame.display.set_mode((screen_width, screen_height))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     face = pygame.draw.circle(screen, (240, 252, 3),(500, 250),200)
#     eye1 = pygame.draw.circle(screen, (41, 41, 38), (400, 150), 25)
#     eye2 = pygame.draw.circle(screen, (41, 41, 38), (600, 150), 25)
#     mouth = pygame.draw.line(screen, (255, 0, 230), (425, 275), (575, 275), 25)

#     pygame.display.update()
#     clock.tick(60)

#Keystate

# import pygame

# pygame.init()
# clock = pygame.time.Clock()
# screen_width, screen_height = 1000, 500

# screen = pygame.display.set_mode((screen_width, screen_height))
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((0,0,0))
#     keystate = pygame.key.get_pressed()  #Tracks what keys the user presses

#     if keystate[pygame.K_a]:
#         square = pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 50))
#     if keystate[pygame.K_UP]:
#         print("Bye")

#     pygame.display.update()
#     clock.tick(60)

# Homework
# Create a game loop so that when the user clicks certain buttons, different things pop up on the screen
# When they click UP, draw a blue circle
# When they clock DOWN, draw a red square
# When they click RIGHT, draw a green line
# When they click LEFT, draw an emoji
# When they click tab, draw a checkerboard pattern (lines)
# OPTIONAL: when they click the space bar, draw a blue sky, with green grass(rectangle) and a snowman (3 white circles)

# Good Luck!

# Link for keystate codes: https://www.pygame.org/docs/ref/key.html

# import pygame

# class Text():
#     def __init__(self, surface, text, size, color, x, y):
#         self.surface = surface
#         self.text = text
#         self.font = pygame.font.Font(pygame.font.match_font("microsofthimalaya"), size)
#         self.color = color
#         self.x = x
#         self.y = y

#     def draw(self):
#         text_surface = self.font.render(self.text, True, self.color)
#         text_rect = text_surface.get_rect()
#         text_rect.midtop = (self.x, self.y)
#         self.surface.blit(text_surface, text_rect)

# pygame.init()
# screen = pygame.display.set_mode((1000, 500))
# clock = pygame.time.Clock()

# instructions = [
#     Text(screen, "^ arrow: Blue Circle", 20, (255, 255, 255), 100, 10),
#     Text(screen, "v arrow: Red Square", 20, (255, 255, 255), 100, 40),
#     Text(screen, "-->: Green Line", 20, (255, 255, 255), 100, 70),
#     Text(screen, "<--: Smiley Face", 20, (255, 255, 255), 100, 100),
#     Text(screen, "Tab: Grid", 20, (255, 255, 255), 100, 130),
#     Text(screen, "Space: Snowman", 20, (255, 255, 255), 130, 160),
# ]

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     #workspace
#     screen.fill((204, 6, 5))
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_UP]:
#         pygame.draw.circle(screen, (16, 44, 84), (500, 250), 100)

#     if keys[pygame.K_DOWN]:
#         pygame.draw.rect(screen, (175, 43, 30), (450, 200, 100, 100))

#     if keys[pygame.K_RIGHT]:
#         pygame.draw.line(screen, (30, 89, 69), (100, 250), (900, 250), 5)

#     if keys[pygame.K_LEFT]:
#         pygame.draw.circle(screen, (255, 204, 0), (500, 250), 100)
#         pygame.draw.circle(screen, (0, 0, 0), (450, 215), 10)
#         pygame.draw.circle(screen, (0, 0, 0), (550, 215), 10)
#         pygame.draw.line(screen, (0, 0, 0), (460, 300), (540, 300), 5)

#     if keys[pygame.K_TAB]:
#         for x in range(0, 1000, 50):
#             pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 500), 1)
#         for y in range(0, 500, 50):
#             pygame.draw.line(screen, (255, 255, 255), (0, y), (1000, y), 1)

#     if keys[pygame.K_SPACE]:
#         screen.fill((135, 206, 235))
#         pygame.draw.rect(screen, (34, 139, 34), (0, 400, 1000, 100))
#         pygame.draw.circle(screen, (255, 255, 255), (500, 350), 40)
#         pygame.draw.circle(screen, (255, 255, 255), (500, 290), 30)
#         pygame.draw.circle(screen, (255, 255, 255), (500, 240), 20)

#     for i in instructions:
#         i.draw()

#     pygame.display.update()
#     clock.tick(60)

#Sprites
# import pygame

# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,50))
#         self.image.fill((161,35,18))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_w]:
#             self.rect.y -= 5
#         if keystate[pygame.K_a]:
#             self.rect.x -= 5
#         if keystate[pygame.K_s]:
#             self.rect.y += 5
#         if keystate[pygame.K_d]:
#             self.rect.x += 5

# class Player2(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,50))
#         self.image.fill((0,160,10))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_UP]:
#             self.rect.y -= 5
#         if keystate[pygame.K_LEFT]:
#             self.rect.x -= 5
#         if keystate[pygame.K_DOWN]:
#             self.rect.y += 5
#         if keystate[pygame.K_RIGHT]:
#             self.rect.x += 5

# #Create our player object
# player = Player(900, 350)
# player2=Player2(100,100)
# #Create our group for players
# player_group = pygame.sprite.Group()
# #Add player object to the group
# player_group.add(player)
# player_group.add(player2)

# pygame.init()
# screen_width,screen_height=1000,500
# screen=pygame.display.set_mode((screen_width,screen_height))
# clock=pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((62,95,138))

#     #Draws player group onto the screen
#     player_group.draw(screen)
#     player_group.update()

#     if pygame.sprite.collide_rect(player,player2):
#         #Draw text on the screen
#         pygame.display.update()
#         pygame.time.delay(1000)
#         player.rect.x=100
#         player.rect.y=100
#         player2.rect.x=900
#         player2.rect.y=250

#     pygame.display.update()
#     clock.tick(60)

#Homework
#Create a new pygame loop, and create 2 classes for different players
#After you have the two classes, draw both players onto the game loop
#IF the players collide, write a TEXT on the screen that says TAG
#After they touch, show the text for a couple seconds, then teleport the players away from eachother
#I also want you to adjust the classes, so that the users cannot leave the screen
#Good Luck!

# import pygame
# from classes import Text

# pygame.init()
# screen_width,screen_height=1500, 500
# screen=pygame.display.set_mode((screen_width,screen_height))
# clock=pygame.time.Clock()

# #Create and use the classes here:

# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,50))
#         self.image.fill((161,35,18))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_w]:
#             self.rect.y -= 10
#         if keystate[pygame.K_a]:
#             self.rect.x -= 10
#         if keystate[pygame.K_s]:
#             self.rect.y += 10
#         if keystate[pygame.K_d]:
#             self.rect.x += 10
#         #Logic for screen bounds
#         if self.rect.left>screen_width:
#             self.rect.right=0
#         if self.rect.right<0:
#             self.rect.left=screen_width
#         if self.rect.top>screen_height:
#             self.rect.bottom=0
#         if self.rect.bottom<0:
#             self.rect.top=screen_height

# class Player2(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((50,50))
#         self.image.fill((0,160,10))
#         self.rect=self.image.get_rect()
#         self.rect.center=(x,y)
#     def update(self):
#         keystate=pygame.key.get_pressed()
#         if keystate[pygame.K_UP]:
#             self.rect.y -= 10
#         if keystate[pygame.K_LEFT]:
#             self.rect.x -= 10
#         if keystate[pygame.K_DOWN]:
#             self.rect.y += 10
#         if keystate[pygame.K_RIGHT]:
#             self.rect.x += 10
#         #Logic for screen bounds
#         if self.rect.left>screen_width:
#             self.rect.right=0
#         if self.rect.right<0:
#             self.rect.left=screen_width
#         if self.rect.top>screen_height:
#             self.rect.bottom=0
#         if self.rect.bottom<0:
#             self.rect.top=screen_height
# #Creating a object using the player class
# andrew=Player(600,400)

# benson=Player2(100,200)

# tag_text=Text(screen, "Tag!",50,(0,0,0),750,100)
# #Creating a group to add the sprites to
# group=pygame.sprite.Group()
# group.add(andrew)
# group.add(benson)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((100,0,120))
#     group.draw(screen)
#     group.update()

#     if pygame.sprite.collide_rect(andrew,benson):
#         #Draw text, and wait 2 seconds
#         tag_text.draw()
#         pygame.display.update()
#         pygame.time.delay(2000)

#         andrew.rect.x=600
#         andrew.rect.y=400
#         benson.rect.x=100
#         benson.rect.y=200

#     pygame.display.update()
#     clock.tick(60)

#Player class with images

# import pygame
# import time
# from classes import Text

# pygame.init()
# screen_width, screen_height = 1500, 800
# screen = pygame.display.set_mode((screen_width, screen_height))
# clock = pygame.time.Clock()


# class Player(pygame.sprite.Sprite):

#     def __init__(self, image, scale, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(
#             image, (int(width * scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)

#     def update(self,target):
#         if self.rect.x>target.rect.x:
#             self.rect.x-=12
#         if self.rect.x<target.rect.x:
#             self.rect.x+=12
#         if self.rect.y>target.rect.y:
#             self.rect.y-=13
#         if self.rect.y<target.rect.y:
#             self.rect.y+=13


#     def update2(self):
#         keystate = pygame.key.get_pressed()
#         if keystate[pygame.K_w]:
#             self.rect.y -= 10
#         if keystate[pygame.K_a]:
#             self.rect.x -= 10
#         if keystate[pygame.K_s]:
#             self.rect.y += 10
#         if keystate[pygame.K_d]:
#             self.rect.x += 10
#         # Logic for screen bounds
#         if self.rect.left > screen_width:
#             self.rect.right = 0
#         if self.rect.right < 0:
#             self.rect.left = screen_width
#         if self.rect.top > screen_height:
#             self.rect.bottom = 0
#         if self.rect.bottom < 0:
#             self.rect.top = screen_height


# # load in the image
# monkeyIMG = pygame.image.load("monkey.png")
# bananaIMG = pygame.image.load("banana.png")
# # Creating object using class
# monkey = Player(monkeyIMG, 0.5, 100, 200)
# banana = Player(bananaIMG, 0.05, 1000, 500)

# group = pygame.sprite.Group()
# group.add(monkey)
# group.add(banana)

# e=Text(screen, "Caught!", 100, (0,0,255),750,100)
# start=time.time()
# # Game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((255, 255, 255))

#     end=time.time()
#     time_alive=str(round(end-start,2))
#     time_text=Text(screen,time_alive, 50, (100,0,150),750,220)
#     time_text.draw()


#     group.draw(screen)
#     monkey.update(banana)
#     banana.update2()

#     # Check for collision
#     if pygame.sprite.collide_rect(monkey, banana):
#         e.draw()
#         pygame.display.update()
#         pygame.time.delay(3000)
#         pygame.quit()
#         quit()

#     pygame.display.update()
#     clock.tick(60)

#Class: Button
# import pygame
# from classes import Text

# class Button(pygame.sprite.Sprite):
#     def __init__(self, surface, image, scale, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.surface=surface
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width*scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.clicked = False
#     def draw(self):
#         self.surface.blit(self.image, (self.rect.x, self.rect.y))
#         pressed = False
#         pos = pygame.mouse.get_pos()

#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#                 self.clicked = True
#                 pressed = True
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False
#         return pressed

# pygame.init()
# screen_width, screen_height = 1000,500
# screen=pygame.display.set_mode((screen_width,screen_height))
# clock=pygame.time.Clock()


# e=Text(screen, "ok", 100, (0,0,255),750,100)



# buttonIMG=pygame.image.load("button.png")
# button=Button(screen,buttonIMG,0.05,300,100)

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((0,100,100))

#     if button.draw():
#         e.draw()
#         pygame.display.update()
#         pygame.time.delay(1000)


#     pygame.display.update()
#     clock.tick(60)

# Homework
# Find an image of a cookie, and I want you to create a cookie clicker game!
# You will have to use a button class, that we created today in class. 
# When the user clicks the cookie, the cookie will teleport to a new random position on the screen
# Make a variable that tracks how many cookies the user has clicked
# Use a text class to show the number of times a cookie was clicked on the screen
# Optional: Make the sprite a different size every time it's clicked (hint: make scale random)
# Good Luck!

# import pygame
# import random
# from classes import Text, Button

# pygame.init()

# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Cookie Clicker")




# def random_position():
#     x = random.randint(50, screen_width - 50)
#     y = random.randint(50, screen_height - 50)
#     return x, y

# cookie_x, cookie_y = random_position()
# cookie_image = pygame.image.load("cookie.png")
# scale = 0.3

# cookie_button = Button(screen, cookie_image, scale, cookie_x, cookie_y)

# score = 0
# score_text = Text(screen, "Cookies: 0", 50, (0, 0, 0), 100, 100)

# clock = pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     screen.fill((255, 255, 255))
#     if cookie_button.draw():
#         score += 1
#         new_x, new_y = random_position()
#         cookie_button.rect.center = (new_x, new_y)
#         score_text = Text(screen, "Cookies: " + str(score), 50, (0, 0, 0), 100, 100)

#     score_text.draw()

#     pygame.display.update()
#     clock.tick(60)




#Practice Game
# from classes import Player, Background, Text, Button
# import pygame

# pygame.init()
# screen_width,screen_height=1500,900
# screen=pygame.display.set_mode((screen_width,screen_height))
# clock=pygame.time.Clock()

# #Creating objects
# mapIMG=pygame.image.load("map.png")
# map=Background(screen,mapIMG,3,750,450)

# playerIMG=pygame.image.load("playerSprite.png")
# player1=Player(playerIMG,0.3,100,500)

# sprite_group=pygame.sprite.Group()
# sprite_group.add(map)
# sprite_group.add(player1)

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     sprite_group.draw(screen)
#     player1.update(screen_width,screen_height)
    
#     if player1.rect.x>0 and player1.rect.x<50:
#         if player1.rect.y<700:
#             player1.rect.y+=5
            
            
    
    
#     pygame.display.update()
#     clock.tick(60)


# Homework
# I want you to come up with at least 3 ideas for a final project.
# In this final project, try to find as many ways as you can to use the topics we've covered throughout our class.
# We created several classes like Player, Button, Text, and Background. Figure out what classes we will need
# and why we need it for your project.
# Make sure to write notes for things you want to be included in your game. Good Luck!

# 1. casino
# 	- you walk around and use machines to gamble with your starting money then you start upgrading and stuff
# 2. fishing game
# 	- upgrades, islands, boats, companions
# 3. office game
# 	- you work as a office worker climbing up the ranks until you're the CEO



