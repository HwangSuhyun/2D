import game_framework
import main_state
from pico2d import *


name = "GameOver"
image = None


def enter():
    global image
    image = load_image('title.png')
    global effect
    effect = load_wav('over.wav')
    effect.set_volume(32)
    effect.play(1)

    global bgm
    bgm = load_music('bgm.mp3')
    bgm.set_volume(32)
    bgm.repeat_play()




def exit():
    global image, effect
    del(image)
    del(effect)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                    game_framework.change_state(main_state)
def draw():
    clear_canvas()
    image.draw(300,350)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






