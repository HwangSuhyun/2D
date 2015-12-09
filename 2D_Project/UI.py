__author__ = 'user'

from pico2d import *

class UI:
    def __init__(self):
        self.time = 0
        self.font = load_font('ConsolaMalgun.ttf', 30)

    def update(self):
        #print(get_time())
        self.time += 0.04

    def draw(self):
        print('시간 : %d' % self.time)
        self.font.draw(300,660,'Time : %f' % self.time)


def test_ui():

    open_canvas()
    ui = UI()
    ui.update()
    ui.draw()
    update_canvas()

    delay(2)
    close_canvas()

if __name__ == "__main__":
    test_ui()
