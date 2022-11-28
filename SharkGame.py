import pygame
from pygame.locals import *
import random
import time

#I should see this on my windows computer

macRoute = "/Users/darrenosborne/Programming/SharkGame/"
route = macRoute
size = width, height =(800, 800)
roadmark_w = int(width/80)
rightSide = width + 100
leftSide = -100
topSide = -100
bottomSide = height + 100
level = 1 
score = 0
pygame.init()

running = True
screen = pygame.display. set_mode(size)
screen.fill((21, 137, 238))

def drawThings():
  pygame.draw.rect(screen, (255,255,255), (10, 10, width/10, height/30))
  pygame.draw.rect(screen, (255,255,255), (width-(width/10)-10, 10, width/10, height/30))
def drawLevelScreen(l):
  pygame.draw.rect(screen, (255,255,255), (0, 0, width, height))
  levelScreen = scoreScreenFont.render("Level: "+str(l), 1, "black")
  screen.blit(levelScreen, (width/2, height/2))
  time.sleep(5)




pygame.display.set_caption("AnotherGame")
pygame.display.update()

#score and level font
scoreScreenFont = pygame.font.SysFont("Times New Roman", 40)
myFont = pygame.font.SysFont("Times New Roman", 18)
scoreText = myFont.render("Score: "+str(score), 1, "black")
levelText = myFont.render("Level: "+str(level), 1, "black")

#loading sharks
rightShark = pygame.image.load(route+"RightShark.png")
rightShark_loc = rightShark.get_rect()
rightShark_loc.center = leftSide, height*0.5
leftShark = pygame.image.load(route+"LeftShark.png")
leftShark_loc = leftShark.get_rect()
leftShark_loc.center = rightSide, height*0.5
upShark = pygame.image.load(route+"UpShark.png")
upShark_loc = upShark.get_rect()
upShark_loc.center = width*0.5, bottomSide
downShark = pygame.image.load(route+"DownShark.png")
downShark_loc = downShark.get_rect()
downShark_loc.center = width*0.5, topSide

#loading player
player = pygame.image.load(route+"Player.png")
player_loc = player.get_rect()
player_loc.center = width*0.5, height*0.5

#crafted coordinate containers
rightShark_locContainer = 0
leftShark_locContainer = 0
tick = 0

#game loop
time.sleep(1)
while(running):
  tick+=1
  #animating sharks
  scoreScreenIndicator = 0
  if score<20:
    level = 1
    if scoreScreenIndicator==0:
      drawLevelScreen(level)
      scoreScreenIndicator+=1
    if tick%2==0:
      if score%4==0:
        leftShark_loc[0]+=-1
      if score%4==1:
        rightShark_loc[0]+=1
      if score%4==2:
        upShark_loc[1]+=-1
      if score%4==3:
        downShark_loc[1]+=1
  elif score<40:
    level = 2
    if scoreScreenIndicator==1:
      drawLevelScreen(level)
      scoreScreenIndicator+=1
    if tick%2==0:
      if score%4==0:
        leftShark_loc[0]+=-1
        downShark_loc[1]+=1
      if score%4==2:
        rightShark_loc[0]+=1
        upShark_loc[1]+=-1
  elif score<80:
    level = 3
    if scoreScreenIndicator==2:
      drawLevelScreen(level)
      scoreScreenIndicator+=1
    if tick%2==0:
      leftShark_loc[0]+=-1
      downShark_loc[1]+=1
      rightShark_loc[0]+=1
      upShark_loc[1]+=-1
  else:
    level = 4
    if scoreScreenIndicator==3:
      drawLevelScreen(level)
      scoreScreenIndicator+=1
    if tick%3>0:
      leftShark_loc[0]+=-1
      downShark_loc[1]+=1
      rightShark_loc[0]+=1
      upShark_loc[1]+=-1
        

  #resetting sharks and increasing score
  if leftShark_loc[0]< -200:
    leftShark_loc.center = rightSide, random.randint(0,800)
    score+=1
  if rightShark_loc[0]> width:
    rightShark_loc.center = leftSide, random.randint(0,800)
    score+=1
  if upShark_loc[1] < -200:
    upShark_loc.center = random.randint(0,800), bottomSide
    score+=1
  if downShark_loc[1] > height:
    downShark_loc.center = random.randint(0,800), topSide
    score+=1
  
  
  #end game condition
  if ((player_loc[0]+100>leftShark_loc[0] and player_loc[0]<leftShark_loc[0]+200) \
    and (player_loc[1]+100>leftShark_loc[1] and player_loc[1]<leftShark_loc[1]+100))\
      or\
        ((player_loc[0]+100>rightShark_loc[0] and player_loc[0]<rightShark_loc[0]+200) \
    and (player_loc[1]+100>rightShark_loc[1] and player_loc[1]<rightShark_loc[1]+100))\
      or\
        ((player_loc[0]+100>upShark_loc[0] and player_loc[0]<upShark_loc[0]+100) \
    and (player_loc[1]+100>upShark_loc[1] and player_loc[1]<upShark_loc[1]+200))\
      or\
        ((player_loc[0]+100>downShark_loc[0] and player_loc[0]<downShark_loc[0]+100) \
    and (player_loc[1]+100>downShark_loc[1] and player_loc[1]<downShark_loc[1]+200)):
    
    print("GAME OVER")
    print("Your score was "+str(score))
    print("At level "+str(level))
    break

  #player movement
  if tick%2==0:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_loc[0]>0:
          player_loc[0]+=-1
    if keys[pygame.K_RIGHT] and player_loc[0] <width - 100:
          player_loc[0]+=1
    if keys[pygame.K_DOWN] and player_loc[1] < height-100:
          player_loc[1]+=1
    if keys[pygame.K_UP] and player_loc[1]>0:
          player_loc[1]+=-1
    
  #event listeners(quit)
  for event in pygame.event.get():
    if event.type == QUIT:
      running = False

  drawThings()

  #updating score and level
  scoreText = myFont.render("Score: "+str(score), 1, "black")
  screen.blit(scoreText, (10,10))
  levelText = myFont.render("Level: "+str(level), 1, "black")
  screen.blit(levelText, (width-(width/10), 10))
  
  #updating cars
  screen.blit(rightShark, rightShark_loc)
  screen.blit(leftShark, leftShark_loc)
  screen.blit(upShark, upShark_loc)
  screen.blit(downShark, downShark_loc)
  screen.blit(player, player_loc)
  pygame.display.update()

pygame.quit()