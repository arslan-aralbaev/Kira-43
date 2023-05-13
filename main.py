import pygame as py
py.init()
clock = py.time.Clock()
screen = py.display.set_mode()
x_screen, y_screen = screen.get_size()
fps = 13


class Player:
    def __init__(self, packR, packU, packD, packA):
        self.x = 0
        self.y = 0
        self.run_pic = [py.image.load(f'pictures/{numerate}') for numerate in packR]
        self.run_pic = [py.transform.scale(image, (x_screen, y_screen)) for image in self.run_pic]
        self.up_pic = [py.image.load(f'pictures/{numerate}') for numerate in packU]
        self.up_pic = [py.transform.scale(image, (x_screen, y_screen)) for image in self.up_pic]
        self.down_pic = [py.image.load(f'pictures/{numerate}') for numerate in packD]
        self.down_pic = [py.transform.scale(image, (x_screen, y_screen)) for image in self.down_pic]
        self.attak_pic = [py.image.load(f'pictures/{numerate}') for numerate in packA]
        self.attak_pic = [py.transform.scale(image, (x_screen, y_screen)) for image in self.attak_pic]
        [image.set_colorkey((110, 125, 145)) for image in self.run_pic]
        [image.set_colorkey((110, 125, 145)) for image in self.up_pic]
        [image.set_colorkey((110, 125, 145)) for image in self.down_pic]
        [image.set_colorkey((110, 125, 145)) for image in self.attak_pic]
        [image.set_colorkey((110, 125, 145)) for image in self.attak_pic]
        self.mainList = self.run_pic
        self.mainImage = self.mainList[0]
        self.time = 0
        self.time = 0
        self.positions = ['jump', 'run', 'ride', 'attak']
        self.position = self.positions[1]

    def draw(self):
        keys = py.key.get_pressed()
        self.mainImage.set_alpha(140)
        screen.blit(self.mainImage, (self.x, self.y))
        if keys[py.K_w]:
            self.time = 0
            self.mainList = self.up_pic
            self.position = self.positions[0]
        elif keys[py.K_s]:
            self.time = 0
            self.mainList = self.down_pic
        elif keys[py.K_q]:
            self.time = 0
            self.mainList = self.attak_pic
            self.position = self.positions[3]
        if self.position == self.positions[0]:
            self.y -= 23
        elif self.position != self.positions[0] and self.y < 0:
            self.y += 23
        self.time += 1
        self.mainList = self.run_pic if self.time % 10 == 0 else self.mainList
        self.position = self.positions[1] if self.time % 10 == 3 else self.position
        self.mainImage = self.mainList[self.time % 10]
        self.mainImage.set_alpha(255)
        screen.blit(self.mainImage, (self.x, self.y))


player = Player(['r1.png', 'r2.png', 'r3.png', 'r4.png', 'r5.png', 'r6.png', 'r7.png', 'r8.png', 'r9.png', 'r10.png'],
                ['u1.png', 'u2.png', 'u3.png', 'u4.png', 'u5.png', 'u6.png', 'u7.png', 'u8.png', 'u9.png', 'u10.png'],
                ['d1.png', 'd2.png', 'd3.png', 'd4.png', 'd5.png', 'd6.png', 'd7.png', 'd8.png', 'd9.png', 'd10.png'],
                ['a1.png', 'a2.png', 'a3.png', 'a4.png', 'a5.png', 'a6.png', 'a7.png', 'a8.png', 'a9.png', 'a10.png'])
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    screen.fill((125, 125, 255))
    player.draw()
    clock.tick(fps)
    py.display.update()
