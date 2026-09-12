import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((1200,800))

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,image_path,controls,side):
        #Initialsing parent class constructor
        super().__init__()
        #self.image is a parent class property
        self.image = pygame.image.load(image_path)

        #Adding hitbox around the image
        self.rect = self.image.get_rect(topleft = (x,y))
        #child class property
        self.control = controls
        self.side = side
        self.health = 100
        self.bullets = pygame.sprite.Group()

    #Movement 
    def move(self,keys):
        pass




while True:
    screen.fill("orange")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    pygame.display.update()

pygame.quit()