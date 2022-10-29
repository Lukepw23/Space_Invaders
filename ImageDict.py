import pygame

### CALLING ###
### imageDict['NAME'[0 = IMG or 1 = RECT]]

### Dropdown Menu Open ###
Dropdown_Menu_Open_Center_x = 25
Dropdown_Menu_Open_Center_y = 25
Dropdown_Menu_Open_Width = 50
Dropdown_Menu_Open_Height = 50

### Dropdown Menu Closed ###
Dropdown_Menu_Closed_Center_x = 30
Dropdown_Menu_Closed_Center_y = 25
Dropdown_Menu_Closed_Width = 50
Dropdown_Menu_Closed_Height = 50

### Open Edit Mode ###
Open_Edit_Mode_Center_x = 25
Open_Edit_Mode_Center_y = 75
Open_Edit_Mode_Width = 60
Open_Edit_Mode_Height = 50

### Exit Game ###
Exit_Game_Center_x = 25
Exit_Game_Center_y = 125
Exit_Game_Width = 50
Exit_Game_Height = 50

### Boss Enemy Selection ###
Boss_Enemy_Selection_Center_x = 245
Boss_Enemy_Selection_Center_y = 675
Boss_Enemy_Selection_Width = 50
Boss_Enemy_Selection_Height = 40

### Shooter Enemy Selection ###
Shooter_Enemy_Selection_Center_x = 110
Shooter_Enemy_Selection_Center_y = 675
Shooter_Enemy_Selection_Width = 60
Shooter_Enemy_Selection_Height = 50

### Kamikaze Enemy Selection ###
Kamikaze_Enemy_Selection_Center_x = 175
Kamikaze_Enemy_Selection_Center_y = 675
Kamikaze_Enemy_Selection_Width = 60
Kamikaze_Enemy_Selection_Height = 50

### Basic Enemy Selection ###
Basic_Enemy_Selection_Center_x = 40
Basic_Enemy_Selection_Center_y = 675
Basic_Enemy_Selection_Width = 40
Basic_Enemy_Selection_Height = 20

### Spawn Enemy ###
Spawn_Enemy_Center_x = 320
Spawn_Enemy_Center_y = 675
Spawn_Enemy_Width = 50
Spawn_Enemy_Height = 50

### Move Enemy ###
Move_Enemy_Center_x = 380
Move_Enemy_Center_y = 675
Move_Enemy_Width = 50
Move_Enemy_Height = 50

### Delete Enemy ###
Delete_Enemy_Center_x = 445
Delete_Enemy_Center_y = 675
Delete_Enemy_Width = 60
Delete_Enemy_Height = 50

### Ruler ###
Ruler_Center_x = 510
Ruler_Center_y = 675
Ruler_Width = 50
Ruler_Height = 50

### Enemy Selection Cursor ###
Enemy_Selection_Cursor_Center_x = 590
Enemy_Selection_Cursor_Center_y = 675
Enemy_Selection_Cursor_Width = 50
Enemy_Selection_Cursor_Height = 50

### Add Patrol Point ###
Add_Patrol_Point_Center_x = 650
Add_Patrol_Point_Center_y = 675
Add_Patrol_Point_Width = 50
Add_Patrol_Point_Height = 50

### Delete Patrol Point ###
Delete_Patrol_Point_Center_x = 715
Delete_Patrol_Point_Center_y = 675
Delete_Patrol_Point_Width = 60
Delete_Patrol_Point_Height = 50

### Change Movement Type ###
Change_Movement_Type_Center_x = 780
Change_Movement_Type_Center_y = 675
Change_Movement_Type_Width = 50
Change_Movement_Type_Height = 50

### Enemy Route ###
Enemy_Route_Center_x = 845
Enemy_Route_Center_y = 675
Enemy_Route_Width = 80
Enemy_Route_Height = 50

### Add Level/Wave ###
Add_Wave_Center_x = 975
Add_Wave_Center_y = 605
Add_Wave_Width = 50
Add_Wave_Height = 70

### Delete Level/Wave ###
Delete_Wave_Center_x = 1035
Delete_Wave_Center_y = 615
Delete_Wave_Width = 50
Delete_Wave_Height = 50

### Left Wave Change Arrow ###
Left_Wave_Change_Arrow_Center_x = 965
Left_Wave_Change_Arrow_Center_y = 675
Left_Wave_Change_Arrow_Width = 50
Left_Wave_Change_Arrow_Height = 50

### Right Wave Change Arrow ###
Right_Wave_Change_Arrow_Center_x = 1036
Right_Wave_Change_Arrow_Center_y = 675
Right_Wave_Change_Arrow_Width = 50
Right_Wave_Change_Arrow_Height = 50

imageDict = {

    'Dropdown Menu Open': 
    (pygame.transform.rotate(pygame.transform.scale(pygame.image.load('Images/Menu4.jpeg'), (Dropdown_Menu_Open_Width, Dropdown_Menu_Open_Height)), 90),
    pygame.Surface((50,50)).get_rect(center = (Dropdown_Menu_Open_Center_x, Dropdown_Menu_Open_Center_y))),
    
    'Dropdown Menu Closed':
    (pygame.transform.scale(pygame.image.load('Images/Menu4.jpeg'), (Dropdown_Menu_Closed_Width, Dropdown_Menu_Closed_Height)),
    pygame.Surface((50,50)).get_rect(center = (Dropdown_Menu_Closed_Center_x, Dropdown_Menu_Closed_Center_y))),

    'Open Edit Mode':
    (pygame.transform.scale(pygame.image.load('Images/MapEdit.png'), (Open_Edit_Mode_Width, Open_Edit_Mode_Height)),
    pygame.Surface((50, 50)).get_rect(center=(Open_Edit_Mode_Center_x, Open_Edit_Mode_Center_y))),

    'Exit Game':
    (pygame.transform.scale(pygame.image.load('Images/Exit.png'), (Exit_Game_Width, Exit_Game_Height)),
    pygame.Surface((50, 50)).get_rect(center=(Exit_Game_Center_x, Exit_Game_Center_y))),

    'Boss Enemy Selection': 
    (pygame.transform.scale(pygame.image.load('Images/Enemy_Boss.png'), (Boss_Enemy_Selection_Width, Boss_Enemy_Selection_Height)),
    pygame.Surface((50, 40)).get_rect(center=(Boss_Enemy_Selection_Center_x, Boss_Enemy_Selection_Center_y))),

    'Shooter Enemy Selection':
    (pygame.transform.scale(pygame.image.load('Images/Enemy_Shooter.png'), (Shooter_Enemy_Selection_Width, Shooter_Enemy_Selection_Height)),
    pygame.Surface((60, 50)).get_rect(center=(Shooter_Enemy_Selection_Center_x, Shooter_Enemy_Selection_Center_y))),

    'Kamikaze Enemy Selection':
    (pygame.transform.scale(pygame.image.load('Images/Enemy_Kamikaze.png'), (Kamikaze_Enemy_Selection_Width, Kamikaze_Enemy_Selection_Height)),
    pygame.Surface((60, 50)).get_rect(center=(Kamikaze_Enemy_Selection_Center_x, Kamikaze_Enemy_Selection_Center_y))),

    'Basic Enemy Selection':
    (pygame.transform.scale(pygame.image.load('Images/Enemy_Normal.png'), (Basic_Enemy_Selection_Width, Basic_Enemy_Selection_Height)),
    pygame.Surface((40, 20)).get_rect(center=(Basic_Enemy_Selection_Center_x, Basic_Enemy_Selection_Center_y))),

    'Spawn Enemy':
    (pygame.transform.scale(pygame.image.load('Images/SpawnEnemy.png'), (Spawn_Enemy_Width, Spawn_Enemy_Height)),
    pygame.Surface((50,50)).get_rect(center=(Spawn_Enemy_Center_x, Spawn_Enemy_Center_y))),

    'Move Enemy':
    (pygame.transform.scale(pygame.image.load('Images/MoveEnemy.png'), (Move_Enemy_Width, Move_Enemy_Height)),
    pygame.Surface((50,50)).get_rect(center=(Move_Enemy_Center_x, Move_Enemy_Center_y))),

    'Delete Enemy':
    (pygame.transform.scale(pygame.image.load('Images/DeleteEnemy.png'), (Delete_Enemy_Width, Delete_Enemy_Height)),
    pygame.Surface((60,50)).get_rect(center=(Delete_Enemy_Center_x, Delete_Enemy_Center_y))),

    'Ruler':
    (pygame.transform.scale(pygame.image.load('Images/Ruler_Icon.png'), (Ruler_Width, Ruler_Height)),
    pygame.Surface((50,50)).get_rect(center=(Ruler_Center_x, Ruler_Center_y))),

    'Enemy Selection Cursor':
    (pygame.transform.scale(pygame.image.load('Images/CursorIcon.png'), (Enemy_Selection_Cursor_Width, Enemy_Selection_Cursor_Height)),
    pygame.Surface((50,50)).get_rect(center=(Enemy_Selection_Cursor_Center_x, Enemy_Selection_Cursor_Center_y))),

    'Add Patrol Point':
    (pygame.transform.scale(pygame.image.load('Images/AddPointIcon.png'), (Add_Patrol_Point_Width, Add_Patrol_Point_Height)),
    pygame.Surface((50,50)).get_rect(center=(Add_Patrol_Point_Center_x, Add_Patrol_Point_Center_y))),

    'Delete Patrol Point':
    (pygame.transform.scale(pygame.image.load('Images/DeleteEnemy.png'), (Delete_Patrol_Point_Width, Delete_Patrol_Point_Height)),
    pygame.Surface((60,50)).get_rect(center=(Delete_Patrol_Point_Center_x, Delete_Patrol_Point_Center_y))),

    'Change Movement Type':
    (pygame.transform.scale(pygame.image.load('Images/ChangeIcon.png'), (Change_Movement_Type_Width, Change_Movement_Type_Height)),
    pygame.Surface((50,50)).get_rect(center=(Change_Movement_Type_Center_x, Change_Movement_Type_Center_y))),

    'Enemy Route':
    (pygame.transform.scale(pygame.image.load('Images/RouteIcon.png'), (Enemy_Route_Width, Enemy_Route_Height)),
    pygame.Surface((80,50)).get_rect(center=(Enemy_Route_Center_x, Enemy_Route_Center_y))),



    'Add Level/Wave':
    (pygame.transform.scale(pygame.image.load('Images/AddSign.png'), (Add_Wave_Width, Add_Wave_Height)),
    pygame.Surface((70,50))
    .get_rect(center=(Add_Wave_Center_x, Add_Wave_Center_y))),

    'Remove Level/Wave':
    (pygame.transform.scale(pygame.image.load('Images/TrashSign.png'), (Delete_Wave_Width, Delete_Wave_Height)),
    pygame.Surface((50,50)).get_rect(center=(Delete_Wave_Center_x, Delete_Wave_Center_y))),

    'Left Wave Change Arrow':
    (pygame.transform.scale(pygame.image.load('Images/LeftArrow.png'), (Left_Wave_Change_Arrow_Width, Left_Wave_Change_Arrow_Height)),
    pygame.Surface((50,50)).get_rect(center=(Left_Wave_Change_Arrow_Center_x, Left_Wave_Change_Arrow_Center_y))),

    'Right Wave Change Arrow':
    (pygame.transform.scale(pygame.image.load('Images/RightArrow.png'), (Right_Wave_Change_Arrow_Width, Right_Wave_Change_Arrow_Height)),
    pygame.Surface((50,50)).get_rect(center=(Right_Wave_Change_Arrow_Center_x, Right_Wave_Change_Arrow_Center_y))),

}