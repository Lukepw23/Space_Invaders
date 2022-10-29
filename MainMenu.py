import sys
import pygame
from MapBuilder import MapMaker
from ImageDict import imageDict

class menu(pygame.sprite.Sprite):

    def __init__(self, win, MapBuilder):
        super().__init__()

        # Attributes

        self.win = win
        self.MM = MapBuilder

        self.MenuOpen = False
        self.EditMode = False
        self.MousePOS = (-10,-10)
        self.EnemyType = None
        self.SelectingEnemy = False
        self.RectList = []
        self.MoveCounter = 1
        self.RulerCounter = 0
        self.MoveSelectedEnemy = None

        self.RulerSelectedEnemy1 = None
        self.RulerSelectedEnemy2 = None
        self.MovableEnemy = None

        self.MovementSelectedEnemy = None


        # Menu Ship Attributes

        self.BasicWidth = 40
        self.BasicHeight = 20
        self.BasicDim = self.BasicWidth, self.BasicHeight
        self.BasicSelected = False

        self.ShooterWidth = 60
        self.ShooterHeight = 50
        self.ShooterDim = self.ShooterWidth, self.ShooterHeight
        self.ShooterSelected = False

        self.KamikazeWidth = 60
        self.KamikazeHeight = 50
        self.KamikazeDim = self.KamikazeWidth, self.KamikazeHeight
        self.KamikazeSelected = False

        self.BossWidth = 50
        self.BossHeight = 40
        self.BossDim = self.BossWidth, self.BossHeight
        self.BossSelected = False

        self.SpawnSelected = False
        self.MoveSelected = False
        self.DeleteSelected = False
        self.RulerSelected = False

        self.CursorSelected = False
        self.AddPointSelected = False
        self.DeletePointSelected = False
        self.RouteIconSelected = False


        # Images

        # Font Styles

        pygame.font.init()
        self.TitleFont = pygame.font.SysFont('Proxima Nova', 50)
        self.LevelFont = pygame.font.SysFont('Proxima Nova', 23)
        self.MovementFont = pygame.font.SysFont('Proxima Nova', 25)

        # Menu Closed
        self.MenuClosedImg = pygame.transform.scale(pygame.image.load('Images/Menu4.jpeg'), (50, 50))
        self.ClosedSurf = pygame.Surface((50,50))
        self.ClosedRect = self.ClosedSurf.get_rect(center = (30,25))

        self.RectList.append(self.ClosedRect)

        # Menu Open
        self.MenuOpenImg = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/Menu4.jpeg'), (50, 50)), 90)
        self.OpenSurf = pygame.Surface((50, 50))
        self.OpenRect = self.OpenSurf.get_rect(center=(25, 25))

        self.RectList.append(self.OpenRect)

        # Map Editing
        self.EditImg = pygame.transform.scale(pygame.image.load('Images/MapEdit.png'), (60, 50))
        self.EditSurf = pygame.Surface((50, 50))
        self.EditRect = self.EditSurf.get_rect(center=(25, 75))

        self.RectList.append(self.EditRect)

        # Exit
        self.ExitImg = pygame.transform.scale(pygame.image.load('Images/Exit.png'), (50, 50))
        self.ExitSurf = pygame.Surface((50, 50))
        self.ExitRect = self.ExitSurf.get_rect(center=(25, 125))

        self.RectList.append(self.ExitRect)

        # Boss Enemy
        self.BossImg = pygame.transform.scale(pygame.image.load('Images/Enemy_Boss.png'), (self.BossDim))
        self.BossSurf = pygame.Surface((self.BossDim))
        self.BossRect = self.BossSurf.get_rect(center=(245, 675))

        # Shooter Enemy
        self.ShooterImg = pygame.transform.scale(pygame.image.load('Images/Enemy_Shooter.png'), (self.ShooterDim))
        self.ShooterSurf = pygame.Surface((self.ShooterDim))
        self.ShooterRect = self.ShooterSurf.get_rect(center=(110, 675))

        # Kamikaze Enemy
        self.KamikazeImg = pygame.transform.scale(pygame.image.load('Images/Enemy_Kamikaze.png'), (self.KamikazeDim))
        self.KamikazeSurf = pygame.Surface((self.KamikazeDim))
        self.KamikazeRect = self.KamikazeSurf.get_rect(center=(175, 675))

        # Basic Enemy
        self.BasicImg = pygame.transform.scale(pygame.image.load('Images/Enemy_Normal.png'), (self.BasicDim))
        self.BasicSurf = pygame.Surface((self.BasicDim))
        self.BasicRect = self.BasicSurf.get_rect(center=(40, 675))

        # Spawn Enemy
        self.SpawnEnemyImg = pygame.transform.scale(pygame.image.load('Images/SpawnEnemy.png'), (50,50))
        self.SpawnEnemySurf = pygame.Surface((50,50))
        self.SpawnEnemyRect = self.SpawnEnemySurf.get_rect(center=(320, 675))

        self.RectList.append(self.SpawnEnemyRect)

        # Move Enemy
        self.MoveEnemyImg = pygame.transform.scale(pygame.image.load('Images/MoveEnemy.png'), (50,50))
        self.MoveEnemySurf = pygame.Surface((50,50))
        self.MoveEnemyRect = self.MoveEnemySurf.get_rect(center=(380, 675))

        self.RectList.append(self.MoveEnemyRect)

        # Delete Enemy
        self.DeleteEnemyImg = pygame.transform.scale(pygame.image.load('Images/DeleteEnemy.png'), (60,50))
        self.DeleteEnemySurf = pygame.Surface((60,50))
        self.DeleteEnemyRect = self.DeleteEnemySurf.get_rect(center=(445, 675))

        self.RectList.append(self.DeleteEnemyRect)

        # Ruler Icon
        self.RulerImg = pygame.transform.scale(pygame.image.load('Images/Ruler_Icon.png'), (50,50))
        self.RulerSurf = pygame.Surface((50,50))
        self.RulerRect = self.RulerSurf.get_rect(center=(510, 675))

        self.RectList.append(self.RulerRect)

        # Cursor Icon
        self.CursorImg = pygame.transform.scale(pygame.image.load('Images/CursorIcon.png'), (50,50))
        self.CursorSurf = pygame.Surface((50,50))
        self.CursorRect = self.CursorSurf.get_rect(center=(590, 675))

        self.RectList.append(self.CursorRect)

        # AddPoint Icon
        self.AddPointImg = pygame.transform.scale(pygame.image.load('Images/AddPointIcon.png'), (50,50))
        self.AddPointSurf = pygame.Surface((50,50))
        self.AddPointRect = self.AddPointSurf.get_rect(center=(650, 675))

        self.RectList.append(self.AddPointRect)

        # Delete Point Icon
        self.DeletePointImg = pygame.transform.scale(pygame.image.load('Images/DeleteEnemy.png'), (60,50))
        self.DeletePointSurf = pygame.Surface((60,50))
        self.DeletePointRect = self.DeletePointSurf.get_rect(center=(715, 675))

        self.RectList.append(self.DeletePointRect)

        # Change Movement Icon
        self.ChangeMovementImg = pygame.transform.scale(pygame.image.load('Images/ChangeIcon.png'), (50,50))
        self.ChangeMovementSurf = pygame.Surface((50,50))
        self.ChangeMovementRect = self.ChangeMovementSurf.get_rect(center=(780, 675))

        self.RectList.append(self.ChangeMovementRect)

        # Route Icon
        self.RouteIconImg = pygame.transform.scale(pygame.image.load('Images/RouteIcon.png'), (80,50))
        self.RouteIconSurf = pygame.Surface((80,50))
        self.RouteIconRect = self.RouteIconSurf.get_rect(center=(845, 675))

        self.RectList.append(self.RouteIconRect)

        # Titles
        self.EditText = self.TitleFont.render('Edit Mode', True, (255,255,255))
        self.LevelText = self.LevelFont.render(f'[Level, Wave] : [1,1]', True, (255,255,255))

        self.ar = self.MM.AddRect
        self.RectList.append(self.ar)
        self.rer = self.MM.RemoveRect
        self.RectList.append(self.rer)
        self.lr = self.MM.LeftRect
        self.RectList.append(self.lr)
        self.rir = self.MM.RightRect
        self.RectList.append(self.rir)        
    
    def enemy_selection_dot(self, rect):

        #circle(surface, color, center, radius)

        self.Dotx = rect.centerx
        self.Doty = 700
        self.DotRadius = 5
        self.DotColor = (255,255,255)

        pygame.draw.circle(self.win, self.DotColor, (self.Dotx, self.Doty), self.DotRadius)
    
    def tool_selection_dot(self, rect):

        #circle(surface, color, center, radius)

        self.Dotx = rect.centerx
        self.Doty = 700
        self.DotRadius = 5
        self.DotColor = (255,255,255)

        pygame.draw.circle(self.win, self.DotColor, (self.Dotx, self.Doty), self.DotRadius)
 
    def menu_tabs(self):

        if pygame.mouse.get_pressed(3) == (1,0,0):
            self.MousePOS = pygame.mouse.get_pos()
            pygame.time.wait(200)

            if self.ClosedRect.collidepoint(self.MousePOS) and self.MenuOpen is False:
                self.MenuOpen = True
                self.MousePOS = (-10,-10)
            if self.OpenRect.collidepoint(self.MousePOS) and self.MenuOpen is True:
                self.MenuOpen = False
                self.MousePOS = (-10, -10)

            if self.EditRect.collidepoint(self.MousePOS) and self.MenuOpen is True:
                if self.EditMode == False:
                    self.EditMode = True
                elif self.EditMode == True:
                    self.EditMode = False

            if self.ExitRect.collidepoint(self.MousePOS) and self.MenuOpen is True:
                self.exit()
            
            if self.BasicRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.BasicSelected = True
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False

                self.EnemyType = 'basic'

                self.SelectingEnemy = True

            elif self.ShooterRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):
                
                self.BasicSelected = False
                self.ShooterSelected = True
                self.KamikazeSelected = False
                self.BossSelected = False

                self.EnemyType = 'shooter'

                self.SelectingEnemy = True

            elif self.KamikazeRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):
                
                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = True
                self.BossSelected = False

                self.EnemyType = 'kamikaze'

                self.SelectingEnemy = True

            elif self.BossRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):
                
                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = True

                self.EnemyType = 'boss'

                self.SelectingEnemy = True
            
            else:

                self.SelectingEnemy = False
            
            if self.SpawnEnemyRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.SpawnSelected = True
                self.MoveSelected = False
                self.DeleteSelected = False
                self.RulerSelected = False

                self.CursorSelected = False
                self.AddPointSelected = False
                self.DeletePointSelected = False
                self.RouteIconSelected = False


                self.MovementSelectedEnemy = None

            
            if self.MoveEnemyRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.SpawnSelected = False
                self.MoveSelected = True
                self.DeleteSelected = False
                self.RulerSelected = False

                self.EnemyType = None
                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False

                self.CursorSelected = False
                self.AddPointSelected = False
                self.DeletePointSelected = False
                self.RouteIconSelected = False


                self.MovementSelectedEnemy = None

            if self.DeleteEnemyRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.SpawnSelected = False
                self.MoveSelected = False
                self.DeleteSelected = True
                self.RulerSelected = False

                self.EnemyType = None
                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False

                self.CursorSelected = False
                self.AddPointSelected = False
                self.DeletePointSelected = False
                self.RouteIconSelected = False


                self.MovementSelectedEnemy = None
            
            if self.RulerRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.SpawnSelected = False
                self.MoveSelected = False
                self.DeleteSelected = False
                self.RulerSelected = True

                self.EnemyType = None
                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False

                self.CursorSelected = False
                self.AddPointSelected = False
                self.DeletePointSelected = False
                self.RouteIconSelected = False


                self.MovementSelectedEnemy = None
            
            if self.CursorRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.CursorSelected = True
                self.AddPointSelected = False
                self.DeletePointSelected = False
                self.RouteIconSelected = False


                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False
                self.SpawnSelected = False
                self.MoveSelected = False
                self.DeleteSelected = False
                self.RulerSelected = False
                

                

            elif self.AddPointRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen and self.CursorSelected is True) is True):

                
                self.AddPointSelected = True
                self.DeletePointSelected = False
                self.RouteIconSelected = False


                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False
                self.SpawnSelected = False
                self.MoveSelected = False
                self.DeleteSelected = False
                self.RulerSelected = False

            
            elif self.DeletePointRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen and self.CursorSelected is True) is True):

                
                self.AddPointSelected = False
                self.DeletePointSelected = True
                self.RouteIconSelected = False


                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False
                self.SpawnSelected = False
                self.MoveSelected = False
                self.DeleteSelected = False
                self.RulerSelected = False

            if self.RouteIconRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.CursorSelected = False
                self.AddPointSelected = False
                self.DeletePointSelected = False
                self.RouteIconSelected = True

                self.BasicSelected = False
                self.ShooterSelected = False
                self.KamikazeSelected = False
                self.BossSelected = False
                self.SpawnSelected = False
                self.MoveSelected = False
                self.DeleteSelected = False
                self.RulerSelected = False


            if self.MM.LeftRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.MM.change_selected_level('-')
                Level = self.MM.get_current_wave()
                self.LevelText = self.LevelFont.render(f'[Level, Wave] : {Level}', True, (255,255,255))
            
            if self.MM.RightRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.MM.change_selected_level('+')
                Level = self.MM.get_current_wave()
                self.LevelText = self.LevelFont.render(f'[Level, Wave] : {Level}', True, (255,255,255))
            
            if self.MM.AddRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.MM.add_or_remove_level('+')
                Level = self.MM.get_current_wave()
                self.LevelText = self.LevelFont.render(f'[Level, Wave] : {Level}', True, (255,255,255))
            
            if self.MM.RemoveRect.collidepoint(self.MousePOS) and ((self.EditMode and self.MenuOpen) is True):

                self.MM.add_or_remove_level('-')
                Level = self.MM.get_current_wave()
                self.LevelText = self.LevelFont.render(f'[Level, Wave] : {Level}', True, (255,255,255))
                         
    def redraw(self):

        if self.MenuOpen == False:
            self.win.blit(self.MenuClosedImg, self.ClosedRect)
            self.BasicSelected = False
            self.ShooterSelected = False
            self.KamikazeSelected = False
            self.BossSelected = False
            self.EditMode = False
            self.SpawnSelected = False
            self.MoveSelected = False
            self.DeleteSelected = False
            self.CursorSelected = False
            self.AddPointSelected = False
            self.DeletePointSelected = False
            self.RouteIconSelected = False
            


        else:
            self.win.blit(self.MenuOpenImg, self.OpenRect)
            self.win.blit(self.EditImg, self.EditRect)
            self.win.blit(self.ExitImg, self.ExitRect)

        if self.EditMode is True:

            self.blit_edit_mode()

        else:
            self.BasicSelected = False
            self.ShooterSelected = False
            self.KamikazeSelected = False
            self.BossSelected = False
            self.SpawnSelected = False
            self.MoveSelected = False
            self.DeleteSelected = False
            self.CursorSelected = False
            self.AddPointSelected = False
            self.DeletePointSelected = False
            self.RouteIconSelected = False


        
        if self.BasicSelected and self.SpawnSelected is True:
            self.enemy_selection_dot(self.BasicRect)
        if self.ShooterSelected and self.SpawnSelected is True:
            self.enemy_selection_dot(self.ShooterRect)
        if self.KamikazeSelected and self.SpawnSelected is True:
            self.enemy_selection_dot(self.KamikazeRect)
        if self.BossSelected and self.SpawnSelected is True:
            self.enemy_selection_dot(self.BossRect)
        
        if self.SpawnSelected is True:
            self.tool_selection_dot(self.SpawnEnemyRect)
        if self.MoveSelected is True:
            self.tool_selection_dot(self.MoveEnemyRect)
        if self.DeleteSelected is True:
            self.tool_selection_dot(self.DeleteEnemyRect)
        if self.RulerSelected is True:
            self.tool_selection_dot(self.RulerRect)
        
        if self.CursorSelected is True:
            self.tool_selection_dot(self.CursorRect)
        if self.AddPointSelected is True:
            self.tool_selection_dot(self.AddPointRect)
        if self.DeletePointSelected is True:
            self.tool_selection_dot(self.DeletePointRect)
        if self.RouteIconSelected is True:
            self.tool_selection_dot(self.RouteIconRect)

    
    def clicking_buttons(self):
        for rect in self.RectList:
            if rect.collidepoint(self.MousePOS):
                return True

    def blit_edit_mode(self):
        
        if self.EditMode == True:

            self.win.blit(self.EditText, (460,40))
            self.win.blit(self.LevelText, (930, 560))

            s = pygame.Surface((535,70))  
            s.set_alpha(128)                
            s.fill((173,173,173))           
            self.win.blit(s, (10,640))

            s1 = pygame.Surface((365,70))  
            s1.set_alpha(128)                
            s1.fill((173,173,173))           #end at 910 start at 565
            self.win.blit(s1, (555,640))

            self.win.blit(self.BasicImg, self.BasicRect)
            self.win.blit(self.ShooterImg, self.ShooterRect)
            self.win.blit(self.KamikazeImg, self.KamikazeRect)
            self.win.blit(self.BossImg, self.BossRect)

            self.win.blit(self.SpawnEnemyImg, self.SpawnEnemyRect)
            self.win.blit(self.MoveEnemyImg, self.MoveEnemyRect)
            self.win.blit(self.DeleteEnemyImg, self.DeleteEnemyRect)
            self.win.blit(self.RulerImg, self.RulerRect)

            self.win.blit(self.CursorImg, self.CursorRect)
            self.win.blit(self.AddPointImg, self.AddPointRect)
            self.win.blit(self.DeletePointImg, self.DeletePointRect)
            self.win.blit(self.ChangeMovementImg, self.ChangeMovementRect)
            self.win.blit(self.RouteIconImg, self.RouteIconRect)

            self.MM.draw_level_editor()

            self.blit_movement_selected_enemy()

    def check_for_spawn(self):
        spawncount = 0

        if (self.EditMode is True) and (self.SpawnSelected is True) and (self.EnemyType != None) and (self.SelectingEnemy is False):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                for rect in self.RectList:
                    if rect.collidepoint(self.MousePOS):
                        spawncount += 1
                    else:
                        spawncount += 0

                if spawncount == 0:
                    self.MM.spawn_enemy(self.MousePOS, self.EnemyType)
                    spawncount = 0
                else:
                    spawncount = 0
    
    def check_for_delete(self):

        if (self.EditMode is True) and (self.DeleteSelected is True):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.MM.delete_enemy()

    def check_for_move(self):

        keys = pygame.key.get_pressed()

        if (self.EditMode is True) and (self.MoveSelected is True):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.clicking_buttons() is not True:
                    if (self.MoveCounter == 1):
                        self.MoveSelectedEnemy = self.MM.get_selected_enemy()
                        self.MoveCounter = 2
                    elif (self.MoveCounter == 2) and (self.MM.is_colliding() is not True):
                        self.MoveCounter = 3
                    else:
                        self.MoveSelectedEnemy = self.MM.get_selected_enemy()
                        self.MoveCounter = 2
                else:
                    self.MoveCounter = 1
            
            if (self.MoveCounter == 2):
                if keys[pygame.K_UP]:
                    self.MM.micro_move_enemy(self.MoveSelectedEnemy, 'up')
                    pygame.time.wait(200)
                elif keys[pygame.K_DOWN]:
                    self.MM.micro_move_enemy(self.MoveSelectedEnemy, 'down')
                    pygame.time.wait(200)
                elif keys[pygame.K_LEFT]:
                    self.MM.micro_move_enemy(self.MoveSelectedEnemy, 'left')
                    pygame.time.wait(200)
                elif keys[pygame.K_RIGHT]:
                    self.MM.micro_move_enemy(self.MoveSelectedEnemy, 'right')
                    pygame.time.wait(200)
                    
                
            if self.MoveCounter == 2:
                self.MM.rect_selected_enemy(self.MoveSelectedEnemy)
            elif self.MoveCounter == 3:
                self.MM.move_enemy(self.MoveSelectedEnemy)
                self.MoveCounter = 1
        
        else:
            self.MoveSelectedEnemy = None

    def check_for_ruler(self):
        keys = pygame.key.get_pressed()

        if (self.EditMode is True) and (self.RulerSelected is True):
            if (pygame.mouse.get_pressed() == (1, 0, 0)):
                if (self.clicking_buttons() is not True) and (self.MM.clicking_enemy() is True):
                    if self.RulerCounter == 0:
                        self.RulerSelectedEnemy1 = self.MM.get_selected_enemy()
                        self.RulerCounter = 1
                        self.MovableEnemy = self.RulerSelectedEnemy1
                        print('enemy1 selected')

                    elif self.RulerCounter == 1:
                        self.RulerSelectedEnemy2 = self.MM.get_selected_enemy()
                        self.RulerCounter = 2
                        print('enemy2 selected')
                
            if (keys[pygame.K_r]) or (self.MM.level_changed() is True):
                self.RulerCounter = 0
                self.RulerSelectedEnemy1 = None
                self.RulerSelectedEnemy2 = None
                print('reset')
                pygame.time.wait(200)
                self.MovableEnemy = None
            
            if self.RulerCounter == 1:
                self.MM.rect_selected_enemy(self.RulerSelectedEnemy1)

            elif self.RulerCounter == 2:
                self.MM.rect_selected_enemy(self.RulerSelectedEnemy1)
                self.MM.rect_selected_enemy(self.RulerSelectedEnemy2)

                self.MM.line_up_ruler(self.RulerSelectedEnemy1, self.RulerSelectedEnemy2)

                if keys[pygame.K_1]:
                    self.MovableEnemy = self.RulerSelectedEnemy1
                elif keys[pygame.K_2]:
                    self.MovableEnemy = self.RulerSelectedEnemy2

                if keys[pygame.K_UP]:
                    self.MM.micro_move_enemy(self.MovableEnemy, 'up')
                    pygame.time.wait(150)
                elif keys[pygame.K_DOWN]:
                    self.MM.micro_move_enemy(self.MovableEnemy, 'down')
                    pygame.time.wait(150)
                elif keys[pygame.K_LEFT]:
                    self.MM.micro_move_enemy(self.MovableEnemy, 'left')
                    pygame.time.wait(150)
                elif keys[pygame.K_RIGHT]:
                    self.MM.micro_move_enemy(self.MovableEnemy, 'right')
                    pygame.time.wait(150)
        
        else:
            self.RulerCounter = 0

    def check_movement_select_enemy(self):
        if (self.EditMode is True) and (self.CursorSelected is True) and (self.AddPointSelected is False):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.clicking_buttons() is not True:
                    self.MovementSelectedEnemy = self.MM.get_selected_enemy()
    
    def check_cycle_movement_pattern(self):
        if (self.EditMode is True) and (self.MovementSelectedEnemy != None):
            if self.ChangeMovementRect.collidepoint(self.MousePOS):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    self.MM.change_movement_pattern(self.MovementSelectedEnemy)
                    pygame.time.wait(150)
    
    def check_add_point(self):
        if (self.EditMode is True) and (self.MovementSelectedEnemy != None) and (self.AddPointSelected is True):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if self.clicking_buttons() is not True:
                    if self.MM.clicking_enemy() is not True:
                        self.MM.add_point(self.MovementSelectedEnemy, self.MousePOS)
                        pygame.time.wait(150)


    def blit_movement_selected_enemy(self):
        
        if self.MovementSelectedEnemy != None:
            self.MM.rect_selected_enemy(self.MovementSelectedEnemy)

            self.MovementPatternText = self.MovementFont.render(f'Movement Type : {self.MovementSelectedEnemy.SelectedMovement}', True, (255,255,255))
            self.win.blit(self.MovementPatternText, (635, 615))

    def check_draw_points(self):
        if  (self.EditMode is True) and (self.MovementSelectedEnemy != None) and (self.AddPointSelected is True):
            self.MM.draw_selected_points(self.MovementSelectedEnemy)
    def is_editing(self):
        return self.EditMode

    def exit(self):

        pygame.quit()
        sys.exit()
    
    