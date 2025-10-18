
import pygame

class Text():
    def __init__(self, surface, text, size, color, x, y):
        self.surface = surface
        self.text = text
        self.font = pygame.font.Font(pygame.font.match_font("microsofthimalaya"), size)
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, images, scale, x, y, speed):
        super().__init__()
        self.speed=speed
        self.images=[]
        for img in images:
            w,h=img.get_width(), img.get_height()
            self.images.append(pygame.transform.scale(img, (int(w*scale),int(h*scale))))
        self.image=self.images[2]
        self.rect=self.image.get_rect(center=(x,y))
    def update(self,screen_width,screen_height):
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.rect.y -= self.speed
            self.image=self.images[3]
        if keystate[pygame.K_a]:
            self.rect.x -= self.speed
            self.image=self.images[1]
        if keystate[pygame.K_s]:
            self.rect.y += self.speed
            self.image=self.images[2]
        if keystate[pygame.K_d]:
            self.rect.x += self.speed
            self.image=self.images[0]
        #Logic for screen bounds
        if self.rect.left>screen_width:
            self.rect.right=0
        if self.rect.right<0:
            self.rect.left=screen_width
        if self.rect.top>screen_height:
            self.rect.bottom=0
        if self.rect.bottom<0:
            self.rect.top=screen_height



class Background(pygame.sprite.Sprite):
    def __init__(self, surface, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surface=surface
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def draw(self):
        self.surface.blit(self.image,(self.rect.x,self.rect.y))
    

class Button(pygame.sprite.Sprite):
    def __init__(self, surface, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.surface=surface
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        pressed = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return pressed