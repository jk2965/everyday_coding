#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pygame
import random
import time

screen_width = 480
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
size_bg_width = screen.get_size()[0]
size_bg_height = screen.get_size()[1]

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("사탕먹기")

#배경음악 로드 및 적용
background_sound = pygame.mixer.Sound("bgm0.wav")
background_sound.set_volume(0.8)
background_sound.play()

#그 외 사운드
candy_sound = pygame.mixer.Sound("normal_candy1.wav") #캔디
gold_candy_sound = pygame.mixer.Sound("gold_candy0.wav") #골드 캔디
pumpkin1_sound = pygame.mixer.Sound("pumpkin2.wav") #호박
gameover_sound = pygame.mixer.Sound("gameover0.wav") #게임오버
gameclear_sound = pygame.mixer.Sound("gameclear0.wav") #게임클리어

clock = pygame.time.Clock()
total_time = 10000 # 제한시간
# gold_time = 10000 # 골드캔디 먹으면 타이머

counter = 5 #골드캔디 먹으면 카운트다운
chance = 5
score = 0

#폰트 설정
game_font = pygame.font.Font("Galmuri9.ttf", 60)
game_font2 = pygame.font.Font("Galmuri9.ttf", 20)
start_font = pygame.font.Font("미원Miwon.otf", 50)
start_font2 = pygame.font.Font("미원Miwon.otf", 35)
number_font = pygame.font.Font("HBIOS-SYS.ttf", 30)
start_ticks = pygame.time.get_ticks()

#게임 오버, 게임 클리어 내용 설정
text_gameover = game_font.render('GAME OVER',True, (255,0,0))
text_gameclear= game_font.render('GAME CLEAR',True, (255,0,0))
text2_gameclear= game_font2.render('계속 하려면 스페이스를 누르세요',True, (255,0,0))

#게임오버, 클리어 글자 가운데 배치
size_text_width = text_gameover.get_rect().size[0]
size_text_height = text_gameover.get_rect().size[1]

#게임오버, 클리어 좌표
x_pos_text = size_bg_width / 2 - size_text_width / 2
y_pos_text = size_bg_height / 2 - size_text_height / 2

# 배경만들기
background = pygame.image.load("background.png")

# 캐릭터만들기
character = pygame.image.load("ghost5.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

to_x = 0  # 이동위치 변수 생성
speed = 0.8

#먹으면 바뀌는 캐릭터 만들기
character2 = pygame.image.load("ghost8.png")

#게임클리어 되면 바뀌는 캐릭터 만들기
character3 = pygame.image.load("man2.png")

#게임오버 되면 바뀌는 캐릭터 만들기
character4 = pygame.image.load("ghost6.png")

# 먹어야하는 것(캔디) 만들기
candy1 = pygame.image.load("candy1.png")
candy2 = pygame.image.load("candy2.png")
candy3 = pygame.image.load("candy3.png")
candy4 = pygame.image.load("candy3.png")
candy1_size = candy2_size = candy3_size = candy4_size = candy1.get_rect().size #x, y좌표 크기 정보를 가지고 있음 
candy1_width = candy2_width = candy3_width = candy4_width = candy1_size[0]
candy1_height = candy2_height = candy3_height = candy4_height = candy1_size[1]
candy1_x_pos = random.randint(0, screen_width - candy1_width)
candy2_x_pos = random.randint(0, screen_width - candy2_width)
candy3_x_pos = random.randint(0, screen_width - candy3_width)
candy4_x_pos = random.randint(0, screen_width - candy4_width)
candy1_y_pos = candy2_y_pos = candy3_y_pos = candy4_y_pos = -10
candy1_speed = 15
candy2_speed = 17
candy3_speed = 16
candy4_speed = 18
# candy4_speed = 40 # 황금캔디먹으면 스피드업

# 먹어야하는 것(gold candy) 만들기
gold = pygame.image.load("bonus.png") # 기존 황금캔디
gold_size= gold.get_rect().size
gold_width = gold_size[0]
gold_height = gold_size[1]
gold_x_pos = random.randint(0, screen_width - gold_width)
gold_y_pos = -5000 #x축 대칭해서 떨어지는 떨어지는 높이 다르게 설정
gold_speed = 22

gold2 = gold3 = gold4 = gold5 = pygame.image.load("bonus2.png") # 황금캔디 먹으면 황금캔디2,3이 떨어지게
gold2_size = gold3_size = gold4_size = gold5_size = gold.get_rect().size
gold2_width = gold3_width = gold4_width = gold5_width = gold_size[0]
gold2_height = gold3_height = gold4_height = gold5_height = gold_size[1]
gold2_x_pos = random.randint(0, screen_width-gold2_width)
gold3_x_pos = random.randint(0, screen_width-gold3_width)
gold4_x_pos = random.randint(0, screen_width-gold4_width)
gold5_x_pos = random.randint(0, screen_width-gold5_width)
gold2_y_pos = -700000
gold3_y_pos = -700000 #x축 대칭해서 떨어지는 떨어지는 높이 다르게 설정
gold4_y_pos = -700000
gold5_y_pos = -700000
gold2_speed = 20
gold3_speed = 22
gold4_speed = 25
gold5_speed = 18

# 피해야할 호박 만들기
pumpkin1 = pumpkin2 = pumpkin3 = pumpkin4 = pumpkin5 = pumpkin6 = pygame.image.load("pumpkin.png")
pumpkin1_size = pumpkin2_size = pumpkin3_size = pumpkin4_size = pumpkin5_size = pumpkin6_size = pumpkin1.get_rect().size
pumpkin1_width = pumpkin2_width = pumpkin3_width = pumpkin4_width = pumpkin5_width = pumpkin6_width = pumpkin1_size[0]
pumpkin1_height = pumpkin2_height = pumpkin3_height = pumpkin4_height = pumpkin5_height = pumpkin6_height = pumpkin1_size[1]
pumpkin1_x_pos = random.randint(0, screen_width - pumpkin1_width)
pumpkin2_x_pos = random.randint(0, screen_width - pumpkin2_width)
pumpkin3_x_pos = random.randint(0, screen_width - pumpkin3_width)
pumpkin4_x_pos = random.randint(0, screen_width - pumpkin4_width)
pumpkin5_x_pos = random.randint(0, screen_width - pumpkin5_width)
pumpkin6_x_pos = random.randint(0, screen_width - pumpkin6_width)
pumpkin1_y_pos = pumpkin2_y_pos = pumpkin3_y_pos = 0
pumpkin4_y_pos = pumpkin5_y_pos = pumpkin6_y_pos = -100
pumpkin1_speed = 18
pumpkin2_speed = 20
pumpkin3_speed = 22
pumpkin4_speed = 20
pumpkin5_speed = 22
pumpkin6_speed = 24

#게임 처음 시작화면
running = False
while running == False:
    clock.tick(35)
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                running = True
        if(event.type == pygame.QUIT):
            pygame.quit()
    image = pygame.image.load("게임 - 메인 화면.jpg")
    image = pygame.transform.scale(image, (400, 470)) #배경이미지 크기조절
    text = start_font.render("사탕먹기 게임", True,(255, 0, 0))
    text2 = start_font2.render("스페이스키를 누르세요", True,(255, 255, 0))
    screen.blit(text, (100,550))
    screen.blit(text2, (78,620))
    screen.blit(image, (45,50))
    pygame.display.update()

while running:
    dt = clock.tick(35)
    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT] == 1:
            character_x_pos -= 400 * clock.get_time() / 600
    if key[pygame.K_RIGHT] == 1:
            character_x_pos += 400 * clock.get_time() / 600
    
    # 떨어지기 설정
    candy1_y_pos += candy1_speed 
    candy2_y_pos += candy2_speed
    candy3_y_pos += candy3_speed
    candy4_y_pos += candy4_speed
    gold_y_pos += gold_speed
    gold2_y_pos += gold2_speed
    gold3_y_pos += gold3_speed
    gold4_y_pos += gold4_speed
    gold5_y_pos += gold5_speed
    pumpkin1_y_pos += pumpkin1_speed
    pumpkin2_y_pos += pumpkin2_speed
    pumpkin3_y_pos += pumpkin3_speed
    
    if score >=20:
        pumpkin4_y_pos += pumpkin4_speed
    if score >=30:
        pumpkin5_y_pos += pumpkin5_speed
    if score >=40:
        pumpkin6_y_pos += pumpkin6_speed
    
    if candy1_y_pos > screen_height:
        candy1_y_pos = 0
        candy1_x_pos = random.randint(0, screen_width - candy1_width)
        
    if candy2_y_pos > screen_height:
        candy2_y_pos = 0
        candy2_x_pos = random.randint(0, screen_width - candy2_width)
        
    if candy3_y_pos > screen_height:
        candy3_y_pos = 0
        candy3_x_pos = random.randint(0, screen_width - candy3_width)
        
    if candy4_y_pos > screen_height:
        candy4_y_pos = 0
        candy4_x_pos = random.randint(0, screen_width - candy4_width)
        
    if gold_y_pos > screen_height:
        gold_y_pos = -random.randint(gold_height, 7000) #떨어지는 위치 다르게설정
        gold_x_pos = random.randint(0, screen_width - gold_width)
        
    if gold2_y_pos > screen_height:
        gold2_y_pos = -random.randint(gold2_height, 70000) #떨어지는 위치 다르게설정
        gold2_x_pos = random.randint(0, screen_width - gold_width)
        
    if gold3_y_pos > screen_height:
        gold3_y_pos = -random.randint(gold3_height, 70000) #떨어지는 위치 다르게설정
        gold3_x_pos = random.randint(0, screen_width - gold3_width)
        
    if gold4_y_pos > screen_height:
        gold4_y_pos = -random.randint(gold4_height, 70000) #떨어지는 위치 다르게설정
        gold4_x_pos = random.randint(0, screen_width - gold3_width)
        
    if gold5_y_pos > screen_height:
        gold5_y_pos = -random.randint(gold5_height, 70000) #떨어지는 위치 다르게설정
        gold5_x_pos = random.randint(0, screen_width - gold5_width)
        
    if pumpkin1_y_pos > screen_height:
        pumpkin1_y_pos = 0
        pumpkin1_x_pos = random.randint(0, screen_width - pumpkin1_width)
        
    if pumpkin2_y_pos > screen_height:
        pumpkin2_y_pos = 0
        pumpkin2_x_pos = random.randint(0, screen_width - pumpkin2_width)
        
    if pumpkin3_y_pos > screen_height:
        pumpkin3_y_pos = 0
        pumpkin3_x_pos = random.randint(0, screen_width - pumpkin3_width)
        
    if pumpkin4_y_pos > screen_height:
        pumpkin4_y_pos = 0
        pumpkin4_x_pos = random.randint(0, screen_width - pumpkin4_width)
        
    if pumpkin5_y_pos > screen_height:
        pumpkin5_y_pos = 0
        pumpkin5_x_pos = random.randint(0, screen_width - pumpkin5_width)
        
    if pumpkin6_y_pos > screen_height:
        pumpkin6_y_pos = 0
        pumpkin6_x_pos = random.randint(0, screen_width - pumpkin6_width)

    if character_x_pos < 0:
        character_x_pos = 0
        
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    candy1_rect = candy1.get_rect()
    candy1_rect.left = candy1_x_pos
    candy1_rect.top = candy1_y_pos
    
    candy2_rect = candy2.get_rect()
    candy2_rect.left = candy2_x_pos
    candy2_rect.top = candy2_y_pos
    
    candy3_rect = candy3.get_rect()
    candy3_rect.left = candy3_x_pos
    candy3_rect.top = candy3_y_pos
    
    candy4_rect = candy4.get_rect()
    candy4_rect.left = candy4_x_pos
    candy4_rect.top = candy4_y_pos
    
    gold_rect = gold.get_rect()
    gold_rect.left = gold_x_pos
    gold_rect.top = gold_y_pos
    
    gold2_rect = gold2.get_rect()
    gold2_rect.left = gold2_x_pos
    gold2_rect.top = gold2_y_pos
    
    gold3_rect = gold3.get_rect()
    gold3_rect.left = gold3_x_pos
    gold3_rect.top = gold3_y_pos
        
    gold4_rect = gold4.get_rect()
    gold4_rect.left = gold4_x_pos
    gold4_rect.top = gold4_y_pos
        
    gold5_rect = gold5.get_rect()
    gold5_rect.left = gold5_x_pos
    gold5_rect.top = gold5_y_pos
    
    pumpkin1_rect = pumpkin1.get_rect()
    pumpkin1_rect.left = pumpkin1_x_pos
    pumpkin1_rect.top = pumpkin1_y_pos
    
    pumpkin2_rect = pumpkin2.get_rect()
    pumpkin2_rect.left = pumpkin2_x_pos
    pumpkin2_rect.top = pumpkin2_y_pos

    pumpkin3_rect = pumpkin3.get_rect()
    pumpkin3_rect.left = pumpkin3_x_pos
    pumpkin3_rect.top = pumpkin3_y_pos
    
    pumpkin4_rect = pumpkin4.get_rect()
    pumpkin4_rect.left = pumpkin4_x_pos
    pumpkin4_rect.top = pumpkin4_y_pos
    
    pumpkin5_rect = pumpkin5.get_rect()
    pumpkin5_rect.left = pumpkin5_x_pos
    pumpkin5_rect.top = pumpkin5_y_pos
    
    pumpkin6_rect = pumpkin6.get_rect()
    pumpkin6_rect.left = pumpkin6_x_pos
    pumpkin6_rect.top = pumpkin6_y_pos

    if character_rect.colliderect(candy1_rect): #candy
        candy1_y_pos = 0
        candy1_x_pos = random.randint(0, screen_width - candy1_width)
        score += 1
        running = True
        
        candy_sound.play()
        candy_sound.set_volume(1)
   
    if character_rect.colliderect(candy2_rect): #candy2
        candy2_y_pos = 0
        candy2_x_pos = random.randint(0, screen_width - candy2_width)
        score += 1
        running = True

        candy_sound.play()
        candy_sound.set_volume(1)
        
    if character_rect.colliderect(candy3_rect): #candy
        candy3_y_pos = 0
        candy3_x_pos = random.randint(0, screen_width - candy3_width)
        score += 1
        running = True
        
        #캔디 먹을 때 사운드 up
        candy_sound.play()
        candy_sound.set_volume(1)
        
    if character_rect.colliderect(candy4_rect): #candy
        candy4_y_pos = 0
        candy4_x_pos = random.randint(0, screen_width - candy4_width)
        score += 1
        running = True
        
        #캔디 먹을 때 사운드 up
        candy_sound.play()
        candy_sound.set_volume(1)

    if character_rect.colliderect(gold2_rect): #candy  
        score += 2
        gold2_y_pos = -70000
        #캔디 먹을 때 사운드 up
        gold_candy_sound.play()
        gold_candy_sound.set_volume(1)
        
    if character_rect.colliderect(gold3_rect): #candy  
        score += 2
        gold3_y_pos = -70000
        #캔디 먹을 때 사운드 up
        gold_candy_sound.play()
        gold_candy_sound.set_volume(1)
        
    if character_rect.colliderect(gold4_rect): #candy  
        score += 2
        gold4_y_pos = -70000
        #캔디 먹을 때 사운드 up
        gold_candy_sound.play()
        gold_candy_sound.set_volume(1)
        
    if character_rect.colliderect(gold5_rect): #candy  
        score += 2
        gold5_y_pos = -70000
        #캔디 먹을 때 사운드 up
        gold_candy_sound.play()
        gold_candy_sound.set_volume(1)
        
    if character_rect.colliderect(gold_rect): #gold candy
        dt = clock.tick(60)
        gold_candy_sound.play()
        gold_candy_sound.set_volume(1)
        
        #랜덤으로 쏟아지게 함
        candy1_x_pos = random.randint(0, screen_width - candy1_width)
        candy2_x_pos = random.randint(0, screen_width - candy2_width)
        candy3_x_pos = random.randint(0, screen_width - candy3_width)
        candy4_x_pos = random.randint(0, screen_width - candy4_width)
        candy1_y_pos = candy2_y_pos = candy3_y_pos = candy4_y_pos = -1000

        gold_x_pos = random.randint(0, screen_width - gold_width)
        gold2_x_pos = random.randint(0, screen_width - gold2_width)
        gold3_x_pos = random.randint(0, screen_width - gold3_width)
        gold4_x_pos = random.randint(0, screen_width - gold4_width)
        gold5_x_pos = random.randint(0, screen_width - gold5_width)
        gold_y_pos = -6000  #오리지날
        gold2_y_pos = -random.randint(0, gold_height) #보너스 캔디
        gold3_y_pos = -random.randint(0, gold_height) #보너스 캔디
        gold4_y_pos = -random.randint(0, gold_height) #보너스 캔디
        gold5_y_pos = -random.randint(0, gold_height)
        
        pumpkin1_x_pos = random.randint(0, screen_width - pumpkin1_width)
        pumpkin2_x_pos = random.randint(0, screen_width - pumpkin2_width)
        pumpkin3_x_pos = random.randint(0, screen_width - pumpkin3_width)
        pumpkin4_x_pos = random.randint(0, screen_width - pumpkin4_width)
        pumpkin5_x_pos = random.randint(0, screen_width - pumpkin5_width)
        pumpkin6_x_pos = random.randint(0, screen_width - pumpkin6_width)
        pumpkin1_y_pos = pumpkin2_y_pos = pumpkin3_y_pos = pumpkin4_y_pos = pumpkin5_y_pos = pumpkin6_y_pos = -2000
        
    if character_rect.colliderect(pumpkin1_rect):
        pumpkin1_y_pos = 0
        pumpkin1_x_pos = random.randint(0, screen_width - pumpkin1_width)
        chance -= 1
        pumpkin1_sound.play()
        pumpkin1_sound.set_volume(1)  
                
    if character_rect.colliderect(pumpkin2_rect):
        pumpkin2_y_pos = 0
        pumpkin2_x_pos = random.randint(0, screen_width - pumpkin2_width)
        chance -= 1    
        pumpkin1_sound.play()
        pumpkin1_sound.set_volume(1) 
                
    if character_rect.colliderect(pumpkin3_rect):
        pumpkin3_y_pos = 0
        pumpkin3_x_pos = random.randint(0, screen_width - pumpkin3_width)
        chance -= 1 
        pumpkin1_sound.play()
        pumpkin1_sound.set_volume(1)
        
    if character_rect.colliderect(pumpkin4_rect):
        pumpkin4_y_pos = 0
        pumpkin4_x_pos = random.randint(0, screen_width - pumpkin4_width)
        chance -= 1 
        pumpkin1_sound.play()
        pumpkin1_sound.set_volume(1) 
        
    if character_rect.colliderect(pumpkin5_rect):
        pumpkin5_y_pos = 0
        pumpkin5_x_pos = random.randint(0, screen_width - pumpkin5_width)
        chance -= 1 
        pumpkin1_sound.play()
        pumpkin1_sound.set_volume(1) 
        
    if character_rect.colliderect(pumpkin6_rect):
        pumpkin6_y_pos = 0
        pumpkin6_x_pos = random.randint(0, screen_width - pumpkin6_width)
        chance -= 1 
        pumpkin1_sound.play()
        pumpkin1_sound.set_volume(1)    

    if(chance == 0):
        running = False
        #모든 음악 끄고 게임 오버 사운드 재생
        background_sound.stop()
        gameover_sound.play()
        gameover_sound.set_volume(1)
        while running == False:
            clock.tick(30)
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_SPACE):
                        running = True
                if(event.type == pygame.QUIT):
                    pygame.quit()
            screen.blit(text_gameover, (x_pos_text, y_pos_text))
            screen.blit(text2_gameclear, (x_pos_text, y_pos_text+80))
            screen.blit(character4, (character_x_pos, character_y_pos))
            pygame.display.update()

        chance = 5 #원래대로 돌아가기
        score = 0
        to_x = 0
        character = pygame.image.load("ghost5.png")
        candy1_y_pos = candy2_y_pos = candy3_y_pos = pumpkin1_y_pos = pumpkin2_y_pos = pumpkin3_y_pos = 0
        pumpkin4_y_pos = pumpkin5_y_pos = pumpkin6_y_pos= -100
        background_sound.play()
           
        
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    screen.blit(gold2, (gold2_x_pos, gold2_y_pos))
    screen.blit(gold3, (gold3_x_pos, gold3_y_pos))
    screen.blit(gold3, (gold4_x_pos, gold4_y_pos))
    screen.blit(gold3, (gold5_x_pos, gold5_y_pos))
    
    screen.blit(candy1, (candy1_x_pos, candy1_y_pos))
    screen.blit(candy2, (candy2_x_pos, candy2_y_pos))
    screen.blit(candy3, (candy3_x_pos, candy3_y_pos))
    screen.blit(candy3, (candy4_x_pos, candy4_y_pos))
    screen.blit(gold, (gold_x_pos, gold_y_pos))

    screen.blit(pumpkin1, (pumpkin1_x_pos, pumpkin1_y_pos))
    screen.blit(pumpkin2, (pumpkin2_x_pos, pumpkin2_y_pos))
    screen.blit(pumpkin3, (pumpkin3_x_pos, pumpkin3_y_pos))
    screen.blit(pumpkin4, (pumpkin4_x_pos, pumpkin4_y_pos))
    screen.blit(pumpkin5, (pumpkin5_x_pos, pumpkin5_y_pos))
    screen.blit(pumpkin6, (pumpkin6_x_pos, pumpkin6_y_pos))
    
    text = number_font.render("남은기회:{} 점수:{}".format(chance,score), True,(255, 255, 0))
    screen.blit(text, (15,20))
            
    if(score >= 50):
        running = False   
        #모든 음악 끄고 게임 오버 사운드 재생
        background_sound.stop()
        gameclear_sound.play()
        gameclear_sound.set_volume(1)
        while running == False:
            clock.tick(30)
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_SPACE):
                        running = True
                if(event.type == pygame.QUIT):         
                    pygame.quit()  
            screen.blit(text_gameclear, (x_pos_text, y_pos_text))
            screen.blit(text2_gameclear, (x_pos_text, y_pos_text+80))
            screen.blit(character3, (character_x_pos-32, character_y_pos-55))
            pygame.display.update()
            
        chance = 5 #원래대로 돌아가기
        score = 0
        to_x = 0
        candy1_y_pos = candy2_y_pos = candy3_y_pos = pumpkin1_y_pos = pumpkin2_y_pos = pumpkin3_y_pos = 0
        pumpkin4_y_pos = pumpkin5_y_pos = pumpkin6_y_pos= -100
        background_sound.play()  
        character = pygame.image.load("ghost5.png")

    pygame.display.update()
    
pygame.quit()


# In[ ]:





# In[ ]:




