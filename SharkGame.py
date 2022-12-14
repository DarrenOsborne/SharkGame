import pygame
from pygame.locals import *
import random
import time
from datetime import datetime
import json

pygame.init()

macRoute = "/Users/darrenosborne/Programming/SharkGame/"
windowsRoute = "C:\\Users\\Darren Osborne\\Documents\\Programming\\SharkGame\\"
otherRoute = "C:\\Users\\Ethan\\OneDrive\\Documents\\Coding\\GitStuff\\DarrenGame\\SharkGame\\"
route = windowsRoute
size = width, height =(800, 800)
roadmark_w = int(width/80)
rightSide = width + 100
leftSide = -100
topSide = -100
bottomSide = height + 100
level = 1 
score = 0
backgroundColor = (21, 137, 238)
#fonts
scoreScreenFont = pygame.font.SysFont("Times New Roman", 40)
myFont = pygame.font.SysFont("Times New Roman", 18)
highscoreFont = pygame.font.SysFont("Times New Roman", 40)
#top ten scores list
topTenScores = []



running, running2 = True, True

screen = pygame.display. set_mode(size)
screen.fill(backgroundColor)

def uploadHighScore(score, player):
  # OPEN JSON FILE AND GET CURRENT DATE AND TIME
  f = open("highscores.json")
  highscores = json.load(f)
  dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
 
  # CHECK IF THE PLAYER ALREADY HAS PREVOUS HIGHSCORES
  oldPlayer = False
  for highscore in highscores:
    if highscores[highscore][1] == player:
      oldPlayer = True
  
  # IF IT IS A NEW PLAYER, MAKE 10 PLACEHOLDER HIGHSCORES FOR THEM
  if not oldPlayer:
    for i in range(10):
      highscores.update({str("Placeholder " + str(i) + " for " + player):["placeholder",player,i]})

  # CHECKING THE DICTIONARY TO SEE IF THERE ARE ANY OPEN PLACEHOLDERS
  openPlaceholders = False
  for highscore in highscores:
    if highscores[highscore][1] == player and str(highscores[highscore][0]) == "placeholder":
      openPlaceholders = True

  # LOOP THROUGH THE DICTIONARY, LOOKING FOR THE PLACEHOLDER SPOT, 
  # THEN DELETING IT AND UPDATING WITH THE NEW HIGH SCORE
  if openPlaceholders:
    for highscore in highscores:
      if highscores[highscore][1] == player and str(highscores[highscore][0]) == "placeholder":
        highscores.pop("Placeholder " + str(highscores[highscore][2]) + " for " + highscores[highscore][1])
        highscores.update({dt_string:[score, player, dt_string]})
        break
  
  # IF ALL THE PLACEHOLDERS ARE TAKEN, LOOP THROUGH THE DICTIONARY TO FIND THE LOWEST SCORE,
  # DELETE IT, UPDATE THE DICTIONARY WITH THE NEW HIGH SCORE
  if not openPlaceholders:
    actualHighScore = False
    lowScore = score
    lowScoreSpot = ""
    for highscore in highscores:
      if highscores[highscore][1] == player and not str(highscores[highscore][0]) == "placeholder":
        if highscores[highscore][0] < lowScore:
          lowScore = highscores[highscore][0]
          lowScoreSpot = highscore
          actualHighScore = True

    if actualHighScore:
      highscores.pop(lowScoreSpot)
      highscores.update({dt_string:[score, player, dt_string]})
  
  # UPDATE THE JSON FILE WITH THE UPDATED DICTIONARY
  json_object = json.dumps(highscores, indent=3)
  with open("highscores.json", "w") as outfile:
    outfile.write(json_object)

def getYourHighScores(player):
  # LOADS THE JSON FILE INTO A DICTIONARY
  f = open("highscores.json")
  highscores = json.load(f)

  # ADDS ALL THE SCORES FOR THE PLAYER INTO A TOP TEN SCORES LIST
  topTenScores = []
  for highscore in highscores:
    if str(highscores[highscore][1]) == player and not str(highscores[highscore][0]) == "placeholder":
      topTenScores.append(highscores[highscore])
  
  # PRINTS OUT THE TOP TEN SCORES
  print("Your Top Ten Scores of All Time are: ")
  print()
  topTenScores.sort()
  topTenScores.reverse()
  for i, score in enumerate(topTenScores):
    print(str(i+1) + ": " + str(score[0]) + " Points on " + str(score[2]))

def getTopTenScores():
  # LOADS THE JSON FILE INTO A DICTIONARY
  f = open("highscores.json")
  highscores = json.load(f)


  
  for highscore in highscores:
    if not str(highscores[highscore][0]) == "placeholder":
      topTenScores.append(highscores[highscore])

  print("The Top Ten Scores of All Time are: ")
  print()
  topTenScores.sort()
  topTenScores.reverse()
  for i, score in enumerate(topTenScores):
    print(str(i+1) + ": " + str(score[0]) + " Points on " + str(score[2]) + " by " + str(score[1]))
    if i+1 == 10:
      break

def drawThings():
  pygame.draw.rect(screen, (255,255,255), (10, 10, width/10, height/30))
  pygame.draw.rect(screen, (255,255,255), (width-(width/10)-10, 10, width/10, height/30))
def drawLevelScreen(l):
  #pygame.draw.rect(screen, (255,255,255), (0, 0, width, height))
  levelScreen = scoreScreenFont.render("Level: "+str(l), 1, "black")
  screen.blit(levelScreen, (width/2-50, height/2))
  pygame.display.update()
  time.sleep(2)
  screen.fill(backgroundColor)
  pygame.display.update()
def drawButtons():
  screen.blit(playButton, playButton_loc)
  screen.blit(highscoresButton, highscoresButton_loc)
  screen.blit(titleImage, titleImage_loc)
def drawBackButton():
  screen.blit(backButton, backButton_loc)
def drawHighScores(tp10):
  tp10.sort()
  tp10.reverse()
  titleHighscore = highscoreFont.render("Top Ten Scores of All Time are: ", 1, "black")
  screen.blit(titleHighscore, (5, 0))
  for i, score in enumerate(tp10):
    eachHighscore = highscoreFont.render(str(i+1) + ": " + str(score[0]) + " Points on " + str(score[2]) + " by " + str(score[1]), 1, "black")
    screen.blit(eachHighscore, (5, height*0.08*(1+i)))
    if i+1 == 10:
      break
  
  

pygame.display.set_caption("AnotherGame")
pygame.display.update()


# loading sharks and player
rightShark = pygame.image.load(route+"RightShark.png")
rightShark_loc = rightShark.get_rect()
leftShark = pygame.image.load(route+"LeftShark.png")
leftShark_loc = leftShark.get_rect()
upShark = pygame.image.load(route+"UpShark.png")
upShark_loc = upShark.get_rect()
downShark = pygame.image.load(route+"DownShark.png")
downShark_loc = downShark.get_rect()
player = pygame.image.load(route+"Player.png")
player_loc = player.get_rect()

#re/setting player and shark centers
def setCenters():
  player_loc.center = width*0.5, height*0.5
  rightShark_loc.center = leftSide, height*0.5
  leftShark_loc.center = rightSide, height*0.5
  upShark_loc.center = width*0.5, bottomSide
  downShark_loc.center = width*0.5, topSide
#calling right after to initiallize centers
setCenters()

#loading buttons + title image + blood splatter
playButton = pygame.image.load(route+"PlayButton.png")
playButton_loc = playButton.get_rect()
playButton_loc.center = width*0.25, height*0.75
highscoresButton = pygame.image.load(route+"HighscoresButton.png")
highscoresButton_loc = highscoresButton.get_rect()
highscoresButton_loc.center = width*0.75, height*0.75
backButton = pygame.image.load(route+"BackButton.png")
backButton_loc = backButton.get_rect()
backButton_loc.center = width*0.5, height*0.94
titleImage = pygame.image.load(route+"TitleImage.png")
titleImage_loc = titleImage.get_rect()
titleImage_loc.center = width*0.5, height*0.4
bloodSplatter = pygame.image.load(route+"BloodSplatter.png")
bloodSplatter_loc = titleImage.get_rect()
bloodSplatter_loc.center = width*0.5, height*0.5


tick = 0
getTopTenScores()
playerName = str(input("What is your player name?"))
#entire run loop
while(running):
  #resetting game conditions and booleans
  running, running2 = True, True
  screen.fill(backgroundColor)
  pygame.display.update()
  setCenters()
  tick = 0
  score = 0
  level = 0
  #pregame loop
  homepage = True
  while(running2):
    if homepage:
      drawButtons()
    for ev in pygame.event.get(): 
      if ev.type == pygame.QUIT:
        pygame.quit()
        running, running2 = False, False
        break
      #checks if a mouse is clicked
      if ev.type == pygame.MOUSEBUTTONDOWN:
        if homepage:
          if abs(mouse[0]-playButton_loc.center[0])<150 \
            and abs(mouse[1]-playButton_loc.center[1])<50:
            running2 = False
            screen.fill(backgroundColor)
            break
          if abs(mouse[0]-highscoresButton_loc.center[0])<150 \
            and abs(mouse[1]-highscoresButton_loc[1])<50:
            homepage = False
            screen.fill(backgroundColor)
            drawHighScores(topTenScores)
            drawBackButton()
            pygame.display.update()
        if not(homepage):
          if abs(mouse[0]-backButton_loc.center[0])<100 \
            and abs(mouse[1]-backButton_loc.center[1])<50:
            homepage = True
            screen.fill(backgroundColor)
            pygame.display.update()
    mouse = pygame.mouse.get_pos()
    pygame.display.update()

  #event listener for highscore button
  #if highscore button gets pressed:
  # sort, then display using text module (for loop)

  #game loop
  scoreScreenIndicator = 0
  time.sleep(1)
  while(running):
    tick+=1
    #animating sharks and level screen
    if score<20:
      level = 1
      if scoreScreenIndicator==0:
        scoreScreenIndicator+=1
        drawLevelScreen(level)
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
    elif score < 120:
      level = 4
      if scoreScreenIndicator==3:
        drawLevelScreen(level)
        scoreScreenIndicator+=1
      if tick%3>0:
        leftShark_loc[0]+=-1
        downShark_loc[1]+=1
        rightShark_loc[0]+=1
        upShark_loc[1]+=-1
    else:
      level = 5
      if scoreScreenIndicator==3:
        drawLevelScreen(level)
        scoreScreenIndicator+=1
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
      uploadHighScore(score, str(playerName))
      getYourHighScores(str(playerName))
      print()
      getTopTenScores()
      screen.blit(bloodSplatter, (0,0))
      pygame.display.update()
      time.sleep(2)
      #running, running2 = False, False
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