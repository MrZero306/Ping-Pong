from pygame import *
from random import randint
font.init()
font1 = font.Font(None, 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 36)

 
img_fon = "fon.jpg" 
img_ball = "ball.png" 
img_rocket = "rocket2.png"


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
            
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
      

win_width = 700
win_height = 500
display.set_caption("PinPong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_fon), (win_width, win_height))
rocket = Player(img_rocket, 5, win_height - 100, 80, 100, 10)
rocket2 = Player2(img_rocket, 610, win_height - 100, 80, 100, 10)
ball = GameSprite(img_ball, 320 ,250 , 50 ,50 , 10)
bullets = sprite.Group()

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE' , True , (180 ,0 ,0))
lose2 = font.render('PLAYER 2 LOSE' , True , (180 ,0 ,0))

speed_x = 3
speed_y = 3

finish = False
run = True 

rel_time = False 
num_fire = 0  

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False    

    if finish != True:
        window.blit(background,(0,0))   
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket , ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1 , (200 , 200))
            game_over = True

        if ball.rect.x > win_width-50:
            finish = True
            window.blit(lose2 , (200 , 200))
            game_over = True

        rocket.update()
        rocket2.update()
        
        rocket.reset()
        ball.reset() 
        rocket2.reset()

        display.update()   

    time.delay(60)