import random
import json
import os

from pico2d import *

import game_framework
import title_state
import game_over

from UI import UI

name = "MainState"

boy = None
grass = None
font = None
ui = None

class Ball:

    drop_sound = None

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())

    def __init__(self):
        self.x, self.y = random.randint(0,600), random.randint(800,900)
        self.image = load_image('dung.png')
        self.speed = random.randint(5,10)

        if Ball.drop_sound == None:
            Ball.drop_sound = load_wav('pickup.wav')
            Ball.drop_sound.set_volume(64)


    def drop(self):
        self.drop_sound.play()

    def update(self):
        self.y -= self.speed
        if self.y <= 63:
            ball.drop()
            self.x, self.y = random.randint(0,600), random.randint(800,900)
            self.speed = random.randint(5,10)

        if ui.time >= 5:
            self.speed = random.randint(7,11)

        if ui.time >= 10:
            self.speed = random.randint(9,13)

        if ui.time >= 15:
            self.speed = random.randint(11,15)

        if ui.time >= 20:
            self.speed = random.randint(13,16)

        if ui.time >= 30:
            self.speed = random.randint(15,17)

        if ui.time >= 40:
            self.speed = random.randint(16,18)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x -10, self.y -8, self.x +10, self.y +10


class BigBall:

    drop_sound = None

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())

    def __init__(self):
        self.x, self.y = random.randint(0,600), random.randint(800,900)
        self.image = load_image('dung2.png')
        self.speed = random.randint(5,11)

        if BigBall.drop_sound == None:
            BigBall.drop_sound = load_wav('pickup.wav')
            BigBall.drop_sound.set_volume(64)



    def drop(self):
        self.drop_sound.play()


    def update(self):
        self.y -= self.speed
        if self.y <= 63:
            big_ball.drop()
            self.x, self.y = random.randint(0,600), random.randint(800,900)
            self.speed = random.randint(5,11)

        if ui.time >= 5:
            self.speed = random.randint(8,13)

        if ui.time >= 10:
            self.speed = random.randint(11,15)

        if ui.time >= 15:
            self.speed = random.randint(13,16)

        if ui.time >= 20:
            self.speed = random.randint(14,17)

        if ui.time >= 30:
            self.speed = random.randint(15,18)

        if ui.time >= 40:
            self.speed = random.randint(16,19)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x -20, self.y -15, self.x +20, self.y +18

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.bgm = load_music('football.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(300, 30)



class Boy:
    step_sound = None

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    #def draw_bb(self):
        #draw_rectangle(*self.get_bb())

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 300, 90
        self.frame = random.randint(0, 7)
        self.state = self.RIGHT_STAND

        self.image = load_image('animation_sheet.png')

        if Boy.step_sound == None:
            Boy.step_sound = load_wav('step.wav')
            Boy.step_sound.set_volume(16)


    def step(self):
        self.step_sound.play()

    def get_bb(self):
        return  self.x - 13, self.y -25, self.x + 13, self.y +30

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
            self.x = min(580,self.x + 7)
            boy.step()
        elif self.state == self.LEFT_RUN:
            self.x = max(20, self.x - 7)
            boy.step()

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

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
    global boy, grass, ball, balls, big_ball, big_balls, ui
    boy = Boy()
    grass = Grass()
    ball = Ball()
    big_ball = BigBall()
    ui = UI()

    big_balls = [BigBall() for i in range(11)]
    balls = [Ball() for i in range(12)]

    balls = balls + big_balls



def exit():
    global boy, grass, balls, big_balls
    del(boy)
    del(grass)
    del(balls)
    del(big_balls)




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

    #for ball in balls:
    for ball in balls:
        ball.update()

        if collide(boy, ball):
            game_framework.push_state(game_over)


    ui.update()


def draw():

    hide_lattice()
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in balls:
        ball.draw()


    #boy.draw_bb()
    #for ball in balls:
        #ball.draw_bb()

    ui.draw()

    update_canvas()

    delay(0.03)





