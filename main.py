import pygame
from pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120
        
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
        
    def move(self):
        self.x = random.randint(0, (1000 // SIZE) - 1) * SIZE
        self.y = random.randint(0, (810 // SIZE) - 1) * SIZE


class Snake:
    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.length = length
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.drection = 'down'
        
    def draw(self):
        self.parent_screen.fill((14, 31, 9)) # This is for the main screen since every time you draw a new image the old one remains. You can comment it out to see the different.
        
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i])) # This blit function is used to display items to the display
        pygame.display.flip() # Keeps updating the changes in screen.
     
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.drection = 'left'
        
    def move_right(self):
        self.drection = 'right'
    
    def move_up(self):
        self.drection = 'up'
        
    def move_down(self):
        self.drection = 'down'
        
        
    def walk(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        
        if self.drection == 'up':
            self.y[0] -=SIZE
            
        if self.drection == 'down':
            self.y[0] +=SIZE
            
        if self.drection == 'left':
            self.x[0] -=SIZE
            
        if self.drection == 'right':
            self.x[0] +=SIZE
            
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 810))# This is to set the display size.
        self.surface.fill((14, 31, 9)) # This is to modify the color.
        
        self.snake = Snake(self.surface,1)
        self.snake.draw()
        
        self.apple = Apple(self.surface)
        self.apple.draw()
        
        self.display_score()
        pygame.display.flip() # This is very useful when making a change to the display
    
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
    
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip() # This is very useful when making a change to the display
        
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()
    
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(800,10))
    
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        running = False
                        
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        
                        
                elif event.type == QUIT:
                    running = False
                    
            self.play()
            
            time.sleep(0.2)
            
if __name__ == "__main__":
    
    game = Game()
    game.run()
    