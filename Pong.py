# Example file showing a circle moving on screen
import pygame
import gameobjects
import webbrowser

# pygame setup
pygame.init()

pygame.display.set_caption('FloopPong')

screen = pygame.display.set_mode((1280, 720))
Timer = pygame.time.Clock()
running = True

winif = 0
loseif = 0
# Some Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
yellow = (255,255,0)
red = (255, 0, 0)

#Difficulty
DifficultyNum = 0
Difficulty = ['Easy', 'Medium', 'Hard']
DifficultyColor = {0: white, 1: yellow, 2: red}


#important stuff

player1 = pygame.Rect(100, 500, 20, 120)
GameBall = gameobjects.Ball(screen, 15)

GameStart = False

# Menu Text
MenuText = gameobjects.Text(screen, "Floop Pong.py", white, black, 50)
StartButton = gameobjects.Text(screen, "Start", white, black, 50)
Author = gameobjects.Text(screen, "Made In Like 3 Days By Ariel (click here for my GitHub)", yellow, black, 25)



# Game Text
PauseText = gameobjects.Text(screen, "Press Space To Resume", white, black, 30)


Player1 = gameobjects.Player(screen, 100, 300)

Enemy = gameobjects.Player(screen, 1160, 300)

while running:



    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            if StartButton.text_rect.collidepoint(mousePosition):
                GameStart = True
            if DifficultyButton.text_rect.collidepoint(mousePosition):
                if DifficultyNum < 2:
                    DifficultyNum += 1
                else:
                    DifficultyNum = 0
            if Author.text_rect.collidepoint(mousePosition):
                webbrowser.open("https://github.com/Flooperr", 0, True)
            if winif == 1:
                if Winner.text_rect.collidepoint(mousePosition):
                    webbrowser.open("https://github.com/Flooperr", 0, True)
            elif loseif == 1:
                if Winner.text_rect.collidepoint(mousePosition):
                    webbrowser.open("https://github.com/Flooperr", 0, True)


    screen.fill('black')



    if GameStart == True:

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            GameBall.Pause = False

        
        GameBall.Start()


        Player1Score = gameobjects.Text(screen, f'{GameBall.Score} | {GameBall.EnemyScore}', white, black, 50)
        Player1Score.Draw((screen.get_width() / 2 , screen.get_height() /2 - 300))

        Player1.Draw(white)
        Enemy.Draw(DifficultyColor[DifficultyNum])
        Player1.Move(keys)
        if GameBall.Pause == True:
            PauseText.Draw((screen.get_width() / 2 , screen.get_height() /2 - 100))

        else:
            Enemy.MoveAI(GameBall.ball_pos, DifficultyNum + 1)
            
            GameBall.CollisionCheck(Player1.player)
            GameBall.CollisionCheck(Enemy.player)

        if GameBall.Score == 3:
            Winner = gameobjects.Text(screen, "You Win", green, black, 50)
            GameBall.Score = 0
            GameBall.EnemyScore = 0
            GameStart = False
            GameBall.Pause = False
            winif = 1
            loseif = 0
        elif GameBall.EnemyScore == 3:
            Winner = gameobjects.Text(screen, "You Lose", red, black, 50)
            GameBall.Score = 0
            GameBall.EnemyScore = 0
            GameStart = False
            GameBall.Pause = False
            loseif = 1
            winif = 0

    else:
        DifficultyButton = gameobjects.Text(screen, Difficulty[DifficultyNum], DifficultyColor[DifficultyNum], black, 50)
        DifficultyButton.Draw((screen.get_width() / 2 + 200 , screen.get_height() /2))
        MenuText.Draw((screen.get_width() / 2 , screen.get_height() /2 - 200 ))
        StartButton.Draw((screen.get_width() / 2 - 200 , screen.get_height() /2))
        Author.Draw((screen.get_width() / 2 , screen.get_height() /2 - 150))
        if winif == 1 or loseif == 1:
            Winner.Draw((screen.get_width() / 2 , screen.get_height() /2 + 200))
        

        
        




    
    Timer.tick(60)

    # flip() the display to put your work on screen
    pygame.display.flip()

    

pygame.quit()