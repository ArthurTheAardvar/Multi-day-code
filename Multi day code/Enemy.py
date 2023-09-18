import pygame
import Multi_day_code
import random

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
militree = pygame.image.load("GoombaHeadaa.png")



class rope:
    def __init__(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = RIGHT
        self.isOnGround = False
        self.movingx = False
        self.movingy = False
        self.x_offset = 0
        self.y_offset = 0  
    def draw(self, screen, xoff, yoff):
        screen.blit(militree, (self.xpos-15 + xoff, self.ypos-10 + yoff))

    def move(self, map, ticker,  px, py, xoff, yoff):
        #check if player is direct line of sight
        #print("y positions in grid:", int(py/50),int(self.ypos/50))
        if int(py/50) == int(self.ypos/50): #check that player and rope are in same row
            if px < self.xpos: #check that player is to the right of rope
                print("I SEE YOU", end = " ")
                if map[int((self.ypos ) / 50)][int( (self.xpos +30 )  / 50)] !=2:
                    self.xpos+=5
            elif px > self.xpos: #left
                if map[int((self.ypos ) / 50)][int( (self.xpos - 30 )  / 50)] !=2:
                    self.xpos-=5
       

       
        #you need to expand this for the other directions

        #otherwise randomly wander
        elif ticker%40==0:
            num = random.randrange(0, 4)
            if num == 0:
                self.direction == RIGHT
            elif num == 1:
                self.direction == LEFT
            elif num == 2:
                self.direction == UP
            elif num == 3:
                self.direction == DOWN
     


        
        
        
        #check for collision and change direction if you've bumped
        if self.direction == RIGHT and map[int((self.ypos ) / 50)][int( (self.xpos +10 )  / 50)] ==2:
            #print("bumped right!")
            self.direction = LEFT
        if self.direction == LEFT and map[int((self.ypos) / 50)][int( (self.xpos - 20 )  / 50)] ==2:
            #print("bumped left!")
            self.direction = DOWN
        if self.direction == DOWN and map[int((self.ypos + 30) / 50)][int( (self.xpos + 15 ) / 50)] == 2:
            self.direction = RIGHT

        
       
#or actually move!
        elif self.direction == RIGHT:
                self.xpos += 5
        elif self.direction == LEFT:
                self.xpos -= 5
        elif self.direction == DOWN:
                self.ypos += 5
        elif self.direction == UP:
                self.ypos -= 5


    