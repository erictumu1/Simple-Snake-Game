import pygame
from pygame.locals import *
import time

SIZE = 40

class Apple:
    
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3
        
    def run(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    

class Snake:
    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.display = 'down'
        
    def run(self):
        self.parent_screen.fill((14, 31, 9))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    
    def move_up(self):
        self.display = 'up'
         
    def move_down(self):
        self.display = 'down'
        
    def move_left(self):
        self.display = 'left'
        
    def move_right(self):
        self.display = 'right'
        
    def move(self):
        
        for i in range(self.length - 1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        if self.display == 'down':
            self.y[0] += SIZE
        if self.display == 'up':
            self.y[0] -= SIZE
        if self.display == 'left':
            self.x[0] -= SIZE
        if self.display == 'right':
            self.x[0] += SIZE
            
        self.run()
            
                  
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,800))
        self.screen.fill((14, 31, 9))
        self.snake = Snake(self.screen,6)
        self.snake.run()
        self.apple = Apple(self.screen)
        self.apple.run()
        
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
                    
                if event.type == QUIT:
                    running = False
                    
            self.snake.move()
            self.apple.run()
            time.sleep(0.3)

if __name__ == "__main__":
    game = Game()
    game.run()