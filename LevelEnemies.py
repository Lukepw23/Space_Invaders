import pygame
import random as r

class NewEnemy(pygame.sprite.Sprite):

    def __init__(self, type, win, POS):
        super().__init__()

        # Dictionary

        self.EnemyDict = {
            "basic": (pygame.transform.scale(pygame.image.load('Images/Enemy_Normal.png'), (40,20))),
            "shooter": (pygame.transform.scale(pygame.image.load('Images/Enemy_Shooter.png'), (60,50))),
            "kamikaze": (pygame.transform.scale(pygame.image.load('Images/Enemy_Kamikaze.png'), (60,50))),
            "boss": (pygame.transform.scale(pygame.image.load('Images/Enemy_Boss.png'), (50,40)))
        }

        # Attributes

        self.MoveCounter = 100

        self.type = type
        self.img = None
        self.win = win
        x, y = POS
        self.x = round(x)
        self.y = round(y)
        self.POS = (self.x, self.y)
        self.Pattern = 'static'
        self.PatrolList = []
        self.MovementDict = {
            'static': [self.POS],
            'patrol': self.PatrolList
        }
        self.PatrolList.append(self.POS)
        
        

        # Enemy Type

        if self.type == 'basic':
            self.img = self.EnemyDict['basic']
            self.surf = pygame.Surface(((self.img.get_width()), (self.img.get_height())))
            self.rect = self.surf.get_rect(center=(self.x, self.y))
            self.SelectedMovement = 'static'
        elif self.type == 'shooter':
            self.img = self.EnemyDict['shooter']
            self.surf = pygame.Surface(((self.img.get_width()), (self.img.get_height())))
            self.rect = self.surf.get_rect(center=(self.x, self.y))
            self.SelectedMovement = 'static'
        elif self.type == 'kamikaze':
            self.img = self.EnemyDict['kamikaze']
            self.surf = pygame.Surface(((self.img.get_width()), (self.img.get_height())))
            self.rect = self.surf.get_rect(center=(self.x, self.y))
            self.SelectedMovement = 'kamikaze'
        elif self.type == 'boss':
            self.img = self.EnemyDict['boss']
            self.surf = pygame.Surface(((self.img.get_width()), (self.img.get_height())))
            self.rect = self.surf.get_rect(center=(self.x, self.y))
            self.SelectedMovement = 'static'

            
    
    def enemy_draw(self):
        self.win.blit(self.img, self.rect)

    def cycle_pattern(self):
        
        if self.type != 'kamikaze':
            if self.SelectedMovement == 'static':
                self.SelectedMovement = 'patrol'
            elif self.SelectedMovement == 'patrol':
                self.SelectedMovement = 'static'
                self.PatrolList.clear()
                self.PatrolList.append(self.POS)
            
            print('changed')

    def add_patrol_point(self, POS):
        if self.type != 'kamikaze':
            self.PatrolList.append((POS))
            print('point added')
    
    def draw_points(self, win):
        for point in self.PatrolList:
            pygame.draw.circle(win, (0,255,0), (point[0], point[1]), 5)
    
    def patrol_move(self):
        pass     

    def move(self):
        pass



        
            


    