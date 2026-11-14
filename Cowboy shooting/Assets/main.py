import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 800
PLAYER_SPEED = 5
BULLET_SPEED = 7
MAX_BULLETS = 3

screen = pygame.display.set_mode((1200,800))

divider = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path,controls,side):
        #Initialsing parent class constructor
        super().__init__()
        #self.image is a parent class property
        self.image = pygame.image.load(image_path)

        #Adding hitbox around the image
        self.rect = self.image.get_rect(topleft = (x,y))
        #child class property
        self.controls = controls
        self.side = side
        self.health = 100
        self.bullets = pygame.sprite.Group()

    #Movement 
    def move(self,keys):
        if keys[self.controls["left"]]:
            self.rect.x-=PLAYER_SPEED
        if keys[self.controls["right"]]:
            self.rect.x+=PLAYER_SPEED
        if keys[self.controls["up"]]:
            self.rect.y-=PLAYER_SPEED
        if keys[self.controls["down"]]:
            self.rect.y+=PLAYER_SPEED
    

player_1 = Player(25,400,"Assets/Cowboy_Left.png",{"left":pygame.K_a,"right":pygame.K_d,"up":pygame.K_w,"down":pygame.K_s},"left")
player_2 = Player(1075,400,"Assets/Cowboy_Right.png",{"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"up":pygame.K_UP,"down":pygame.K_DOWN},"right")

#Creating players group
players = pygame.sprite.Group()
players.add(player_1,player_2)

def draw():
    screen.fill("orange")
    #Displaying both the players
    players.draw(screen)

    #Displaying the divider rectangle
    pygame.draw.rect(screen,"red",divider)
    


    pygame.display.update()

def main_function():
    while True:
        draw()

        #Getting all the keys pressed
        keys_pressed = pygame.key.get_pressed()
        player_1.move(keys_pressed)
        player_2.move(keys_pressed)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

    pygame.quit()

main_function()
