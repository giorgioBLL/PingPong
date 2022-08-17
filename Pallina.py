import pygame
from random import randrange
pygame.init()

screen_x = 700
screen_y = 400

tempo = pygame.time.Clock()
pos_player_x = screen_x-40
pos_player_y = screen_y/2-40
pos_notplayer_x = 20
pos_notplayer_y = screen_y/2-40
vel_player_y = 0
vel_notplayer_y = 0
punteggio = 0
carattere = pygame.font.Font(None,50)
caratterepiccolo = pygame.font.Font(None,20)
caratteregrande = pygame.font.Font(None,100)
round = 1
FPS = 80
difficulty_level = 2
pos_numero_round_transizione_x = screen_x
pos_scritta_sotto_x = screen_x
vel_numero_round_transizione_x = -2
vel_scritta_sotto_x = 0
movimento_transizione_round = False
frasi_level_1 = ["You are still noob","now the games are getting complicated","still it's easy"]
frasi_level_2 = ["It will be more difficult","round 2 is coming","it's time to get better!"]
frasi_level_3 = ["now it gets very complicated","You are improving visibily","you have improved considerably"]
frasi_level_4 = ["now the game gets complicated","When the going gets tough, the tough play","You are god"]
frasi_level_5 = "the last level"
vita = 3
new_match = False

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def conta_round():
    global round
    global numero_round
    global punteggio
    global difficulty_level
    global numero_round_transizione
    global pos_numero_round_transizione_x
    global vel_ball_y
    global vel_ball_x
    global movimento_transizione_round
    global scritta_sotto
    global pos_scritta_sotto_x
    global vel_scritta_sotto_x
    global new_match
    global vita

    numero_round = caratterepiccolo.render(f"round: {round}",True,(0,0,0))
    screen.blit(numero_round,(20,60))     
    if punteggio == 5:
        punteggio = 0
        round += 1
        difficulty_level += 0.5
        index_frasi = randrange(0,3,1)
        vita = 3
        while pos_numero_round_transizione_x+150 > 0:
            movimento_transizione_round = True
            disegno()
            confini()
            movimento_player()
            pos_numero_round_transizione_x += vel_numero_round_transizione_x
            pos_scritta_sotto_x += vel_scritta_sotto_x
            if round == 2:
                scritta_sotto = caratterepiccolo.render(frasi_level_2[index_frasi],True,(0,0,0))
            if round == 3:
                scritta_sotto = caratterepiccolo.render(frasi_level_3[index_frasi],True,(0,0,0))
            if round == 4:
                scritta_sotto = caratterepiccolo.render(frasi_level_4[index_frasi],True,(0,0,0))
            if round == 5:
                scritta_sotto = caratterepiccolo.render(frasi_level_5,True,(0,0,0))
            if round == 6:
                hai_vinto()
            if pos_numero_round_transizione_x < screen_x/2 + 110:
                vel_scritta_sotto_x = -4.5
                if pos_scritta_sotto_x < screen_x/2 +10:
                    vel_scritta_sotto_x = -1
                    if pos_scritta_sotto_x < screen_x/2 -110:
                        vel_scritta_sotto_x = -4.5
            numero_round_transizione = carattere.render(f"{round} ROUND",True,(0,0,0))
            screen.blit(numero_round_transizione,(pos_numero_round_transizione_x,80))
            
            screen.blit(scritta_sotto,(pos_scritta_sotto_x,110))
            aggiorna()
        movimento_transizione_round = False
        pos_numero_round_transizione_x = screen_x
        vel_scritta_sotto_x = 0
        pos_scritta_sotto_x = screen_x
        new_match = True
        restart()
        

#funzione restart: quando si inizia un nuovo match
def restart():
    global pos_ball_x
    global pos_ball_y
    global vel_ball_x
    global vel_ball_y
    global punteggio 
    global vita
    global new_match

    if new_match:
        vita = 3
        new_match = False
    pos_ball_x = screen_x/2
    pos_ball_y = randrange(20,screen_y-20)
    vel_ball_x = randrange(-35,35,69)/10
    if round >= 4:
        vel_ball_y =randrange(-40,40,79)/10
    else:
        vel_ball_y = randrange(-30,30,59)/10

def sei_morto():
    global numero_round_transizione
    global movimento_transizione_round
    global pos_numero_round_transizione_x
    global new_match
    global round
    global difficulty_level
    global punteggio
    global pos_player_y

    movimento_transizione_round = True
    while pos_numero_round_transizione_x + 500 > 0:
        screen.fill(pygame.Color('light grey'))
        pos_numero_round_transizione_x += vel_numero_round_transizione_x
        numero_round_transizione = caratteregrande.render("YOU LOSE",True,(0,0,0))
        screen.blit(numero_round_transizione,(pos_numero_round_transizione_x+50,screen_y/2-50))
        aggiorna()
    movimento_transizione_round = False
    new_match = True
    round = 1
    difficulty_level = 2
    punteggio = 0
    restart()

def hai_vinto():
    global numero_round_transizione
    global movimento_transizione_round
    global pos_numero_round_transizione_x
    global new_match
    global round
    global difficulty_level
    global punteggio
    global scritta_sotto

    while True:
        screen.fill(pygame.Color('light grey'))
        pos_numero_round_transizione_x += vel_numero_round_transizione_x
        numero_round_transizione = caratteregrande.render("YOU WIN",True,(0,0,0))
        if pos_numero_round_transizione_x <= screen_x/2-200:
            screen.blit(numero_round_transizione,(screen_x/2-150,screen_y/2-50))
        else: 
            screen.blit(numero_round_transizione,(pos_numero_round_transizione_x+50,screen_y/2-50))
        scritta_sotto = caratterepiccolo.render("press SPACE to close the game",True,(0,0,0))
        screen.blit(scritta_sotto,(screen_x/2-100,350))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quit()
            if event.type == pygame.QUIT:
                quit()
        aggiorna() 

def disegno():
    global player
    global ball
    global line
    global notplayer
    global screen
    global pos_ball_x
    global pos_ball_y
    global pos_player_y
    global pos_notplayer_y

    
    screen = pygame.display.set_mode((screen_x,screen_y))
    screen.fill(pygame.Color('grey'))
    
    
    pos_ball_x += vel_ball_x
    pos_ball_y += vel_ball_y
    if movimento_transizione_round == False:
        pos_player_y += vel_player_y
    else:
        pos_player_y = screen_y/2-40

    if movimento_transizione_round == False:
        pos_notplayer_y += vel_notplayer_y
    else:
        pos_notplayer_y = screen_y/2-40

    line = pygame.draw.line(screen,(100,90,100),(screen_x/2,0),(screen_x/2,screen_y),10)
    
    if movimento_transizione_round == False:
        ball = pygame.draw.circle(screen,(100,70,100),(pos_ball_x,pos_ball_y),10)
    
    notplayer = pygame.Rect(pos_notplayer_x,pos_notplayer_y,10,70)
    pygame.draw.rect(screen,(100,70,100),notplayer)
    
    if vita == 3:
        cuore1_pieno = pygame.draw.circle(screen,(0,0,0),(screen_x-40,20),6)
        cuore2_pieno = pygame.draw.circle(screen,(0,0,0),(screen_x-60,20),6)
        cuore3_pieno = pygame.draw.circle(screen,(0,0,0),(screen_x-80,20),6)
    elif vita == 2:
        cuore1_pieno = pygame.draw.circle(screen,(0,0,0),(screen_x-40,20),6)
        cuore2_pieno = pygame.draw.circle(screen,(0,0,0),(screen_x-60,20),6)
    elif vita == 1:
        cuore1_pieno = pygame.draw.circle(screen,(0,0,0),(screen_x-40,20),6)

    player = pygame.Rect(pos_player_x,pos_player_y,10,70)
    pygame.draw.rect(screen,(100,70,100),player)

    conta_round()

    punteggio_ottenuto = carattere.render(str(punteggio),True,(0,0,0))
    screen.blit(punteggio_ottenuto,(20,20))

    if vita == 0:
        sei_morto()

def confini():
    global pos_player_y
    global pos_notplayer_y
    global vel_ball_y
    global vel_ball_x
    global vel_notplayer_y
    global round
    global difficulty_level

    #collisione palla avversario
    if ball.colliderect(notplayer) and pos_ball_x >= pos_notplayer_x+6:
        vel_ball_x *= -1
        vel_ball_x += 0.4 + ((round-1)*0.05)  #((round-1)*0.05): aumento velocità incremento palla

    #confine player
    if player.top <= 0:
        pos_player_y = 1
    if player.bottom >= screen_y:
        pos_player_y = screen_y-69

    #confine ball
    if ball.bottom >= screen_y:
        vel_ball_y *= -1
    if ball.top <= 0:
        vel_ball_y *=- 1

    #collisine palla player (migliorato)
    if ball.colliderect(player) and pos_ball_x <= pos_player_x+4:
        if pos_ball_y < pos_player_y+10:
            vel_ball_y =randrange(45,55)/-10
        elif pos_ball_y < pos_player_y+25:
            if round >= 4:
                vel_ball_y =randrange(40,45)/-10
            else:
                vel_ball_y =randrange(30,45)/-10
        elif pos_ball_y > pos_player_y+45:
            if round >= 4:
                vel_ball_y =randrange(40,45)/10
            else:
                vel_ball_y =randrange(30,45)/10
        elif pos_ball_y > pos_player_y+60:
            vel_ball_y = randrange(45,55)/10
        vel_ball_x *= -1
        vel_ball_x -= 0.4 - ((round-1)*0.05)  #((round-1)*0.05): aumento velocità incremento palla
    
    #movimento avversario
    if ball.top+10 > notplayer.top+35:
       vel_notplayer_y = difficulty_level
    elif ball.top+10 < notplayer.top+35:
        vel_notplayer_y = -difficulty_level
        
    #confine notplayer
    if notplayer.top <= 0:
        pos_notplayer_y = 0
    if notplayer.bottom >= screen_y:
        pos_notplayer_y = screen_y-70

def movimento_player():
    global vel_player_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                vel_player_y -= 2.5
            if event.key == pygame.K_s:
                vel_player_y += 2.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                vel_player_y += 2.5
            if event.key == pygame.K_s:
                vel_player_y -= 2.5

restart()
while True:
    disegno()
    movimento_player()
    confini()
    if pos_ball_x > screen_x:
        vita -= 1
        restart()
    if pos_ball_x < 0:
        punteggio +=1
        restart()
    
    aggiorna()