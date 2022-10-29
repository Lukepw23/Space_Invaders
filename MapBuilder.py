import pygame
from pygame.constants import K_EQUALS, K_MINUS
from pygame.cursors import broken_x
from LevelEnemies import NewEnemy

class MapMaker(NewEnemy):

    def __init__(self, win):
        self.win = win

        # Sprite Groups

        self.AllSprites = pygame.sprite.Group()
        self.LevelRectList = []
        
        # Add level/wave
        self.AddImg = pygame.transform.scale(pygame.image.load('Images/AddSign.png'), (50,70))
        self.AddSurf = pygame.Surface((70,50))
        self.AddRect = self.AddSurf.get_rect(center=(975, 605))

        self.LevelRectList.append(self.AddRect)

        # Remove level/wave
        self.RemoveImg = pygame.transform.scale(pygame.image.load('Images/TrashSign.png'), (50,50))
        self.RemoveSurf = pygame.Surface((50,50))
        self.RemoveRect = self.RemoveSurf.get_rect(center=(1035, 615))

        self.LevelRectList.append(self.RemoveRect)

        # Left Arrow
        self.LeftImg = pygame.transform.scale(pygame.image.load('Images/LeftArrow.png'), (50,50))
        self.LeftSurf = pygame.Surface((50,50))
        self.LeftRect = self.LeftSurf.get_rect(center=(965, 675))

        self.LevelRectList.append(self.LeftRect)

        # Right Arrow
        self.RightImg = pygame.transform.scale(pygame.image.load('Images/RightArrow.png'), (50,50))
        self.RightSurf = pygame.Surface((50,50))
        self.RightRect = self.RightSurf.get_rect(center=(1035, 675))

        self.LevelRectList.append(self.RightRect)

        

        
        # Counters and Levels
        self.LevelCounter = 1

        self.Level1_WaveCounter = 1
        self.Level2_WaveCounter = 1
        self.Level3_WaveCounter = 1
        self.Level4_WaveCounter = 1
        self.Level5_WaveCounter = 1
        self.Level6_WaveCounter = 1
        self.Level7_WaveCounter = 1
        self.Level8_WaveCounter = 1
        self.Level9_WaveCounter = 1
        self.Level10_WaveCounter = 1

        self.SelectedLevel = [1, 1]
        self.AddLevelCounter = 1
        self.LenOfLevelList = 1
        self.LevelListPlace = 0

        self.ConstantLevelList = [
            [1,1],[1,2],[1,3],[1,4],[1,5],
            [2,1],[2,2],[2,3],[2,4],[2,5],
            [3,1],[3,2],[3,3],[3,4],[3,5],
            [4,1],[4,2],[4,3],[4,4],[4,5],
            [5,1],[5,2],[5,3],[5,4],[5,5],
            [6,1],[6,2],[6,3],[6,4],[6,5],
            [7,1],[7,2],[7,3],[7,4],[7,5],
            [8,1],[8,2],[8,3],[8,4],[8,5],
            [9,1],[9,2],[9,3],[9,4],[9,5],
            [10,1],[10,2],[10,3],[10,4],[10,5],
            [11,1]
        ]

        self.RealLevelList = [
            [1,1]
        ]

        self.LevelDict = {
            
            'level1': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level2': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level3': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level4': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level5': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level6': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level7': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level8': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level9': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            },
            'level10': {
                'wave1': 0,
                'wave2': 0,
                'wave3': 0,
                'wave4': 0,
                'wave5': 0
            }

        }

        self.SpriteDict = {
            '[1, 1]': pygame.sprite.Group(),
            '[1, 2]': pygame.sprite.Group(),
            '[1, 3]': pygame.sprite.Group(),
            '[1, 4]': pygame.sprite.Group(),
            '[1, 5]': pygame.sprite.Group(),

            '[2, 1]': pygame.sprite.Group(),
            '[2, 2]': pygame.sprite.Group(),
            '[2, 3]': pygame.sprite.Group(),
            '[2, 4]': pygame.sprite.Group(),
            '[2, 5]': pygame.sprite.Group(),

            '[3, 1]': pygame.sprite.Group(),
            '[3, 2]': pygame.sprite.Group(),
            '[3, 3]': pygame.sprite.Group(),
            '[3, 4]': pygame.sprite.Group(),
            '[3, 5]': pygame.sprite.Group(),

            '[4, 1]': pygame.sprite.Group(),
            '[4, 2]': pygame.sprite.Group(),
            '[4, 3]': pygame.sprite.Group(),
            '[4, 4]': pygame.sprite.Group(),
            '[4, 5]': pygame.sprite.Group(),

            '[5, 1]': pygame.sprite.Group(),
            '[5, 2]': pygame.sprite.Group(),
            '[5, 3]': pygame.sprite.Group(),
            '[5, 4]': pygame.sprite.Group(),
            '[5, 5]': pygame.sprite.Group(),

            '[6, 1]': pygame.sprite.Group(),
            '[6, 2]': pygame.sprite.Group(),
            '[6, 3]': pygame.sprite.Group(),
            '[6, 4]': pygame.sprite.Group(),
            '[6, 5]': pygame.sprite.Group(),

            '[7, 1]': pygame.sprite.Group(),
            '[7, 2]': pygame.sprite.Group(),
            '[7, 3]': pygame.sprite.Group(),
            '[7, 4]': pygame.sprite.Group(),
            '[7, 5]': pygame.sprite.Group(),

            '[8, 1]': pygame.sprite.Group(),
            '[8, 2]': pygame.sprite.Group(),
            '[8, 3]': pygame.sprite.Group(),
            '[8, 4]': pygame.sprite.Group(),
            '[8, 5]': pygame.sprite.Group(),

            '[9, 1]': pygame.sprite.Group(),
            '[9, 2]': pygame.sprite.Group(),
            '[9, 3]': pygame.sprite.Group(),
            '[9, 4]': pygame.sprite.Group(),
            '[9, 5]': pygame.sprite.Group(),

            '[10, 1]': pygame.sprite.Group(),
            '[10, 2]': pygame.sprite.Group(),
            '[10, 3]': pygame.sprite.Group(),
            '[10, 4]': pygame.sprite.Group(),
            '[10, 5]': pygame.sprite.Group(),
        }

    def draw_level_editor(self):

        s = pygame.Surface((140,130))  
        s.set_alpha(80)                
        s.fill((173,173,173))           
        self.win.blit(s, (930,585))
        
        self.win.blit(self.LeftImg, self.LeftRect)
        self.win.blit(self.RightImg, self.RightRect)
        self.win.blit(self.AddImg, self.AddRect)
        self.win.blit(self.RemoveImg, self.RemoveRect)

    def add_rects(self, rectlist):

        rectlist.append(self.LeftRect)
        rectlist.append(self.RightRect)
        rectlist.append(self.AddRect)
        rectlist.append(self.RemoveRect)

        return rectlist

    def change_selected_level(self, change):

        self.LenOfLevelList = len(self.RealLevelList)
        
        if change == '+':
            if self.LevelListPlace < self.LenOfLevelList - 1: 

                self.LevelListPlace += 1

                self.SelectedLevel = self.RealLevelList[self.LevelListPlace]

        if change == '-':  
            if self.LevelListPlace > 0:

                
                self.LevelListPlace -= 1

                self.SelectedLevel = self.RealLevelList[self.LevelListPlace]
    
    def get_current_wave(self):
        return self.RealLevelList[self.LevelListPlace]
    
    def add_or_remove_level(self, change):

        self.LenOfLevelList = len(self.RealLevelList)

        if change == '+':
            if self.LenOfLevelList != 51:
                self.RealLevelList.append(self.ConstantLevelList[self.AddLevelCounter])
                self.AddLevelCounter += 1
                self.LevelListPlace = self.LenOfLevelList

                self.SelectedLevel = self.RealLevelList[self.LevelListPlace]

                
        if change == '-':
            if self.LenOfLevelList != 1:
                if self.LevelListPlace == self.LenOfLevelList - 1:
                    self.RealLevelList.pop(self.LevelListPlace)

                    for e in self.SpriteDict[f'{self.SelectedLevel}']:
                        self.AllSprites.remove(e)
                    
                    self.SpriteDict[f'{self.SelectedLevel}'].empty()

                    self.LevelListPlace -= 1
                    self.AddLevelCounter -= 1

                    self.SelectedLevel = self.RealLevelList[self.LevelListPlace]

                    
                else:
                    print('Must Remove Last Level')

    def redraw_editing_enemies(self):
    
        for entity in self.SpriteDict[f'{self.SelectedLevel}']:
            entity.enemy_draw()

    def spawn_enemy(self, POS, enemytype):

        if POS[1] <= 500:
            E = NewEnemy(enemytype, self.win, POS)
            self.SpriteDict[f'{self.SelectedLevel}'].add(E)
            self.AllSprites.add(E)

    def get_selected_enemy(self):
        MousePOS = pygame.mouse.get_pos()

        for sprite in self.SpriteDict[f'{self.SelectedLevel}']:
            if sprite.rect.collidepoint(MousePOS):
                return sprite
    
    def is_colliding(self):
        MousePOS = pygame.mouse.get_pos()

        for sprite in self.SpriteDict[f'{self.SelectedLevel}']:
            if sprite.rect.collidepoint(MousePOS):
                return True

    def level_changed(self):
        MousePOS = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            for rect in self.LevelRectList:
                if rect.collidepoint(MousePOS):
                    return True
                
    def clicking_enemy(self):
        MousePOS = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            for enemy in self.SpriteDict[f'{self.SelectedLevel}']:
                if enemy.rect.collidepoint(MousePOS):
                    return True

    def rect_selected_enemy(self, SelectedEnemy):

        if SelectedEnemy != None:
            centerx = SelectedEnemy.rect.centerx
            centery = SelectedEnemy.rect.centery
            width = SelectedEnemy.surf.get_width()
            height = SelectedEnemy.surf.get_height()

            TLx = (centerx - (width / 2))
            TLy = (centery - (height / 2))
            TL = (TLx, TLy)

            TRx = TLx + width
            TRy = TLy
            TR = (TRx, TRy)

            BRx = TLx + width
            BRy = TLy + height
            BR = (BRx, BRy)

            BLx = TLx
            BLy = TLy + height
            BL = (BLx, BLy)

            width = 5

            pygame.draw.line(self.win, (0,255,0), TL, TR, width)
            pygame.draw.line(self.win, (0,255,0), TR, BR, width)
            pygame.draw.line(self.win, (0,255,0), BR, BL, width)
            pygame.draw.line(self.win, (0,255,0), BL, TL, width)
        
    def delete_enemy(self):
        
        SelectedEnemy = self.get_selected_enemy()

        self.SpriteDict[f'{self.SelectedLevel}'].remove(SelectedEnemy)
        self.AllSprites.remove(SelectedEnemy)
        
    def move_enemy(self, SelectedEnemy):

        if SelectedEnemy != None:
            MousePOS = pygame.mouse.get_pos()

            centerx = SelectedEnemy.rect.centerx
            centery = SelectedEnemy.rect.centery
            
            xchange = round(MousePOS[0] - centerx)
            ychange = round(MousePOS[1] - centery)
            
            
            SelectedEnemy.rect.move_ip(xchange, ychange)
    
    def micro_move_enemy(self, SelectedEnemy, direction):
        vel = 1

        centerx = SelectedEnemy.rect.centerx
        centery = SelectedEnemy.rect.centery

        xchange = 0
        ychange = 0

        if direction == 'up':
            ychange = -vel
        elif direction == 'down':
            ychange = vel
        elif direction == 'left':
            xchange = -vel
        elif direction == 'right':
            xchange = vel
        
        SelectedEnemy.rect.move_ip(xchange, ychange)
        
    def line_up_ruler(self, SelectedEnemy1, SelectedEnemy2):

        if (SelectedEnemy1 != None) and (SelectedEnemy2 != None):
            width = 3

            centerx_1 = SelectedEnemy1.rect.centerx
            centery_1 = SelectedEnemy1.rect.centery

            centerx_2 = SelectedEnemy2.rect.centerx
            centery_2 = SelectedEnemy2.rect.centery

            if centerx_1 == centerx_2:
                color = (0,255,0)
            elif centery_1 == centery_2:
                color = (0,255,0)
            elif ((centery_2 - centery_1) == (centerx_2 - centerx_1)) or ((centery_2 - centery_1) == -(centerx_2 - centerx_1)):
                color = (0,255,0)
            else:
                color = (255,0,0)

            pygame.draw.line(self.win, color, (centerx_1, centery_1), (centerx_2, centery_2), width)
    
    def change_movement_pattern(self, SelectedEnemy):
        
        if SelectedEnemy != None:
            SelectedEnemy.cycle_pattern()

    def add_point(self, SelectedEnemy, POS):
        if (SelectedEnemy.type != 'kamikaze') or (SelectedEnemy.Pattern != 'static'):
            SelectedEnemy.add_patrol_point(POS)

    def draw_selected_points(self, SelectedEnemy):
        SelectedEnemy.draw_points(self.win)


        
    def preset_levels(self):
        pass


    def testprint(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            
            for egroup in self.SpriteDict:
                for e in self.SpriteDict[f'{egroup}']:
                    print(egroup, (e.type, e.POS, e.SelectedMovement, (e.PatrolList)))

            pygame.time.wait(200)