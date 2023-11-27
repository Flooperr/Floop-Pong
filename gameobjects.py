import pygame

class Ball:

    MoveUp = False
    MoveRight = True

    LowerBorder_Y = 680
    UpperBorder_Y = 40

    RightBorder_X = 1240
    LeftBorder_X = 40

    Score = 0
    EnemyScore = 0

    Pause = False
    

    def __init__(self, screen, Radius):
        self.screen = screen
        self.ball_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
        self.radius = Radius
        

    def Bounce_Y(self):
        if self.ball_pos.y <= self.UpperBorder_Y:
            self.MoveUp = False

        elif self.ball_pos.y >= self.LowerBorder_Y:
            self.MoveUp = True
        if self.MoveUp == False:
            self.ball_pos.y += 10
        elif self.MoveUp == True:
            self.ball_pos.y -= 10



    def Bounce_X(self):
        if self.ball_pos.x >= self.RightBorder_X:
            self.MoveRight = False
            self.Score += 1
            self.ball_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
            self.Pause = True
        elif self.ball_pos.x <= self.LeftBorder_X:
            self.MoveRight = True
            self.EnemyScore += 1
            self.ball_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
            self.Pause = True
        if self.MoveRight == True:
            self.ball_pos.x += 10 
        elif self.MoveRight == False:
            self.ball_pos.x -= 10

    def CollisionCheck(self, player_rect):

        # Makes rectangle Over Circle, subtract Radius to Get Center of Ball (In theory)
        BallRect = pygame.Rect(self.ball_pos.x - self.radius, self.ball_pos.y - self.radius, 50, 50)  

        if BallRect.colliderect(player_rect):
            player_left = player_rect.left
            player_right = player_rect.right
            ball_left = self.ball_pos.x - self.radius  
            ball_right = self.ball_pos.x + self.radius    #Left & Right For Player & Enemy

            # Collision for Left Side
            if ball_right >= player_left and ball_left <= player_left:
                self.MoveRight = False
            # Collision for Right Side
            elif ball_left <= player_right and ball_right >= player_right:
                self.MoveRight = True

            player_top = player_rect.top
            player_bottom = player_rect.bottom
            ball_top = self.ball_pos.y - self.radius  
            ball_bottom = self.ball_pos.y + self.radius  

            # Collision for Top 
            if ball_bottom >= player_top and ball_top <= player_top:
                self.MoveUp = True
                self.MoveDown = False
            # Collision for Bottom
            elif ball_top <= player_bottom and ball_bottom >= player_bottom:
                self.MoveUp = False
                self.MoveDown = True

    def Start(self):
        pygame.draw.circle(self.screen, "white", self.ball_pos, self.radius)
        if self.Pause == False:
            self.Bounce_Y()
            self.Bounce_X()

class Player:
    
    width = 20
    height = 120
    LowerBorder_Y = 680
    UpperBorder_Y = 40
    

    def __init__(self, screen, positionX, positionY) -> None:
        self.screen = screen
        self.player = pygame.Rect(positionX, positionY, self.width, self.height) 
    
    #Movement for Player1
    def Move(self, keys):
        if keys[pygame.K_w]:
            if self.player.y > 0:  # Check if moving up would go past the top boundary
                self.player.y -= 10
        if keys[pygame.K_s]:
            if self.player.y < self.screen.get_height() - self.height:  # Check if moving down would go past the bottom boundary
                self.player.y += 10
        
    #Movement for CPU
    def MoveAI(self, ball, difficulty):
        paddleCenter = self.player.y + self.height / 2  

        # Move player towards ball Y cord, difficulty is speed
        if paddleCenter < ball.y:
            self.player.y += difficulty * 3
        elif paddleCenter > ball.y:
            self.player.y -= difficulty * 3

        # Boundary from Top & Bottom of Screen
        if self.player.top <= 0:
            self.player.top = 0
        elif self.player.bottom >= 720:
            self.player.bottom = 720

    def Draw(self, Color): #Just Draw
        pygame.draw.rect(self.screen, Color, self.player)




class Text:
    
    def __init__(self, screen, text, textColor, RectColor, Size):
        self.font = pygame.font.Font('freesansbold.ttf', Size)
        self.screen = screen
        self.text = self.font.render(str(text), True, textColor, RectColor)

        

    #Display On Screen
    def Draw(self, Cordinate):
        self.text_rect = self.text.get_rect(center=Cordinate)
        self.screen.blit(self.text, self.text_rect)
        


    