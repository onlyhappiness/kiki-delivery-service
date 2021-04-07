import pygame
import random
import time

#clock = pygame.time.Clock()

# pygame 초기화
pygame.init()

# 게임 화면 구현
# 15인치 화면에 호환되도록 하였기 때문에
# 다른 desktop에서 보면 작게 보일 수 있습니다...)
screen = pygame.display.set_mode((900, 650))

# color
green = (0,255,0)
white = (255, 255, 255)
light_green = (0,200,0)

# Image
background = pygame.image.load('background.jpg')
intro_background = pygame.image.load('intro.jpg')

# Title and Icon
pygame.display.set_caption("Kiki's Delivery Service")
icon = pygame.image.load('witch.png')
pygame.display.set_icon(icon)

# Player 구현
playerImg = pygame.image.load('kiki.png')
playerX = 0
playerY = 200

playerX_change = 0
playerY_change = 0


# Enemy 구현
enemyImg = pygame.image.load('Raven.png')
x_random = 900
y_random = random.randrange(0,600)

"""
# Enemy 구현(까마귀)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('raven.png'))
    enemyX.append(random.randint(200, 900))
    enemyY.append(random.randint(0, 650))
    enemyX_change.append(-2)
    enemyY_change.append(-2)
"""



# 폰트
font = pygame.font.Font('Goyang.ttf',40)

# Score 
score_value = 0
textX = 10
textY = 10


# 함수
def Message(size,mess,x_pos,y_pos):
    font = pygame.font.Font('Goyang.ttf',40)
    render = font.render(mess, True, white)
    screen.blit(render, (x_pos,y_pos))
    
#Message(100,"START",150,100)
#clock.tick(1)


def show_score(x,y):
    score = font.render("Score:" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x_random, y_random):
    screen.blit(enemyImg, (x_random, y_random))

"""
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
"""

"""
def button(x_button, y_button, mess_b):
    pygame.draw.rect(screen, green,[x_button, y_button, 100, 30])
    Message(50, mess_b, x_button, y_button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_button < mouse[0] < x_button+100 and y_button < mouse[1] < y_button+30:
        pygame.draw.rect(screen, light_green, [x_button, y_button, 100, 30])
        Message(50, mess_b, x_button, y_button)
        if click == (1,0,0) and mess_b == "PLAY":
            Game_loop()
        elif click == (1,0,0) and mess_b == "QUIT":
            pygame.quit()
      
def game_intro():
    intro = False
    while intro == False:
        screen.blit(intro_background,(0,0))
        button(100, 300, "배달 시작!")
        button(600, 300, "나가기")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        pygame.display.update()   
"""

# 게임 루프
running = True
while running:
    # screen.fill((0,51,255))

    # Background Image
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키를 눌렀을 때 움직이는 이벤트
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 1
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -1
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 1

            # ESC를 누르면 게임이 종료하도록..
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0

    # player가 화면 밖으로 나갈 경우
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0

    elif playerX >= 850:
        playerX = 850

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0

    elif playerY >= 550:
        playerY = 550

    """  
    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = -2
            # enemyY[i] += enemyY_change[i]
            # enemyY[i] += enemyY_change[i]

        # 살짝 억지 부려보았다.
        
        while enemyX[i] < -1:
            enemyX[i] = random.randint(300,800)
            #enemyY[i] = random.randint(0.600)
        
                # enemyY[i] += enemyY_change[i]   

        enemy(enemyX[i], enemyY[i], i)

    #enemyY += enemyY_change
    #if enemyY <= 0:
        #enemyY_change = 0.4

    #elif enemyY >= 550:
        #enemyY_change = -0.4
    """
    enemy(x_random,y_random)
    x_random -= 3
    if x_random == 0:
        x_random = 900
        y_random = random.randrange(0,600)
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

#game_intro()
pygame.display.update()
pygame.quit()

