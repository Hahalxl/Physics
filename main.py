import pygame as pg
import math


pg.init()
info = pg.display.Info()
clock = pg.time.Clock()
run = True

class Constants:
    def __init__(self, include_garvity:bool=True, gravity_accleration_earth:float=9.81, include_floor:bool=True, include_walls:bool=True):
        self.include_gravity = include_garvity
        self.gravity_acceleration_earth = gravity_accleration_earth
        self.include_floor = include_floor
        self.include_walls = include_walls
        self.time = 0

width, height = info.current_w, info.current_h
screen = pg.display.set_mode((width, height))


const = Constants(True, 9.81)
print(const.gravity_acceleration_earth)

class Block:
    #Block constructor
    def __init__(self, name:str, size:list[int], mass:int, vector:list[int]):
        if vector is None:
            vector = [0, 0]
        #Variables of the block
        self.name = name
        self.width = size[0]
        self.height = size[1]
        self.init_position = vector
        self.mass = mass

        #X-axis variables
        self.x = vector[0]
        #Velocity for x
        self.vx = 0
        #Acceleration for x
        self.ax = 0

        #Y-axis variables
        self.y = vector[1]
        #Velocity for y
        self.vy = 0
        #Acceleration for y
        self.ay = const.gravity_acceleration_earth

    #Block.methods
    def update(self):
        if const.include_floor and self.y > height and self.ay >= 0:
            self.y = height-self.height
            self.vy = 0
            self.ay = 0
        if self.y < height-self.height and const.include_gravity:
            self.ay = const.gravity_acceleration_earth

        self.y += self.vy

        #Check if the x hits the wall
        if any([self.x < 0 + self.width, self.x > width - self.width]) and const.include_walls:
            self.vx = 0
        elif self.x > width - self.width:
            self.x = 0
        elif self.x < 0 + self.width:
            self.x = width

        self.x += self.vx


        #Display :skull:
        pg.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

        self.vy += self.ay
        self.vx += self.ax

    def push(self, force:int, direction:str):
        #A = F/M
        a = force // self.mass
        if direction.lower() == "right":
            self.ax = a
        elif direction.lower() == "left":
            self.ax = (a-a*2)
        else:
            raise("<object 'block'>\nError: direction can only be 'left' or 'right' ")

    def jump(self, force:int):
        #A = F/M
        self.ay += (force // self.mass)






blocka = Block("Block A", [50, 50], 1, [0, 0])



while(run):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()

    screen.fill((250, 250, 250))

    blocka.update()
    if(keys[pg.K_d]):
        blocka.push(1, 'right')
    if(keys[pg.K_SPACE]):
        blocka.jump(50)





    pg.display.flip()
    clock.tick(60)
