import pygame

class Enemies(pygame.sprite.Sprite):

    def __init__(self, enemyType):
        super().__init__()

        self.type = enemyType
        self.x = 0
        self.y = -50
        self.vel = 0
        self.canShoot = False
        self.canMove = False
        self.health = 0


    def shoot(self):
        pass
    def move(self):
        pass

