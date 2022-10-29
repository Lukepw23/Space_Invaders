import pygame


class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.x = 540
        self.y = 600
        self.width = 150
        self.height = 120
        self.vel = 1
        self.img = pygame.transform.scale(pygame.image.load('Images/Player.png'), (self.width, self.height))
        self.surf = pygame.Surface((self.width, self.height))
        self.rect = self.surf.get_rect(center = (self.x, self.y))

    def move(self, win, isediting):
        win.blit(self.img, self.rect)
        keys = pygame.key.get_pressed()

        if isediting is False:
            if self.x >= 20:
                if keys[pygame.K_a]:
                    self.rect.move_ip(-self.vel, 0)
                    self.x -= self.vel

            if self.x <= (1060):
                if keys[pygame.K_d]:
                    self.rect.move_ip(self.vel, 0)
                    self.x += self.vel

    def shoot(self):
        pass

