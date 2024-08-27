import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.drection = 'down'
        
    def draw(self):
        self.parent_screen.fill((14, 31, 9)) # This is for the main screen since every time you draw a new image the old one remains. You can comment it out to see the different.
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip() # Keeps updating the changes in screen.
        
    def move_left(self):
        self.drection = 'left'
        
    def move_right(self):
        self.drection = 'right'
    
    def move_up(self):
        self.drection = 'up'
        
    def move_down(self):
        self.drection = 'down'
        
        
    def walk(self):
        
        if self.drection == 'up':
            self.y -=10
            
        if self.drection == 'down':
            self.y +=10
            
        if self.drection == 'left':
            self.x -=10
            
        if self.drection == 'right':
            self.x +=10
        
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 500))# This is to set the display size.
        self.surface.fill((14, 31, 9)) # This is to modify the color.
        self.snake = Snake(self.surface)
        self.snake.draw()
    
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
                    
            self.snake.walk()
            time.sleep(0.2)
            
if __name__ == "__main__":
    
    game = Game()
    game.run()
    