import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0,600), 800
        self.image = load_image('dung.png')
        self.speed = random.randint(3,8)

    def update(self):
        self.y -= self.speed
        if self.y <= 60:
            self.y = 800
            self.speed = random.randint(3,8)

    def draw(self):
        self.image.draw(self.x, self.y)


class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0,600), 800
        self.image = load_image('dung2.png')
        self.speed = random.randint(3,8)

    def update(self):
        self.y -= self.speed
        if self.y <= 60:
            self.y = 800
            self.speed = random.randint(3,8)

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(300, 30)



class Boy:

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 300, 90
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_STAND

        self.image = load_image('animation_sheet.png')

    def handle_event(self, event):
       if(event.type, event.key ) == (SDL_KEYDOWN, SDLK_LEFT ):
           if self.state in (self.RIGHT_STAND, self.LEFT_STAND, ):
               self.state = self.LEFT_RUN
               self.last_state = None

           if self.state in (self.RIGHT_RUN, ):
               self.state = self.LEFT_RUN
               self.last_state = self.RIGHT_RUN

       elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_RIGHT ):
           if self.state in (self.RIGHT_STAND, self.LEFT_STAND, ):
               self.state = self.RIGHT_RUN
               self.last_state = None

           if self.state in (self.LEFT_RUN, ):
               self.state = self.RIGHT_RUN
               self.last_state = self.LEFT_RUN

       elif(event.type, event.key ) == (SDL_KEYUP, SDLK_LEFT ):
           if self.state in (self.LEFT_RUN, ):
               self.state = self.LEFT_STAND

               if self.last_state == self.RIGHT_RUN:
                   self.state = self.RIGHT_RUN
                   self.last_state = None

       elif(event.type, event.key ) == (SDL_KEYUP, SDLK_RIGHT ):
           if self.state in (self.RIGHT_RUN, ):
               self.state = self.RIGHT_STAND

               if self.last_state == self.LEFT_RUN:
                   self.state = self.LEFT_RUN
                   self.last_state = None

    def update(self):
        self.frame = (self.frame + 1 ) % 8
        if self.state == self.RIGHT_RUN:
            self.x = min(580,self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(20, self.x - 5)

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def create_position():
    position_data_text = '                                              \
        {                                                           \
            "Boy" : {"StartState" : "RIGHT_STAND", "x" : 300, "y" : 90} \
        }                                                           \
    '
    player_state_table = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN" : Boy.RIGHT_RUN,
        "LEFT_STAND" : Boy.LEFT_STAND,
        "RIGHT_STAND" : Boy.RIGHT_STAND
    }

    position_data = json.loads(position_data_text)

    position = []
    for name in position_data:
        player = Boy()
        player.name = name
        player.x = position_data[name]['x']
        player.y = position_data[name]['y']
        player.state = player_state_table[position_data[name]['StartState']]
        position.append(player)

    return position


def enter():
    global boy, grass, ball, balls, big_ball, big_balls
    boy = Boy()
    grass = Grass()
    ball = Ball()
    big_ball = BigBall()
    big_balls = [BigBall() for i in range(10)]
    balls = [Ball() for i in range(10)]
    balls = big_balls + balls


def exit():
    global boy, grass, ball, big_ball
    del(boy)
    del(grass)
    del(ball)
    del(big_ball)




def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            boy.handle_event(event)


def update():
    boy.update()
    for ball in balls:
        ball.update()

def draw():

    hide_lattice()
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.03)





