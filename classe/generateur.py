from random import randint
import pygame

from pygame import mixer

# Starting the mixer
mixer.init()
# Loading the song
mixer.music.load("../asset/sound/bk.mp3")
# Setting the volume
mixer.music.set_volume(0.7)
# Start playing the song
mixer.music.play()


clock = pygame.time.Clock()

global window_size
window_size = (1200, 648)
screen = pygame.display.set_mode(window_size)


img0 = pygame.image.load("../asset/image/0.png").convert()
img1 = pygame.image.load("../asset/image/1.png")
img2 = pygame.image.load("../asset/image/2.png")
img3 = pygame.image.load("../asset/image/3.png")
img4 = pygame.image.load("../asset/image/4.png")
img5 = pygame.image.load("../asset/image/5.png")
img6 = pygame.image.load("../asset/image/6.png")
img7 = pygame.image.load("../asset/image/7.png")
img8 = pygame.image.load("../asset/image/8.png")
imgX = pygame.image.load("../asset/image/X.png").convert()
imgB = pygame.image.load("../asset/image/B.png")

img_vide = pygame.image.load("../asset/image/vide.png")
img_done = pygame.image.load("../asset/image/done.png")
img_flag = pygame.image.load("../asset/image/flag.png")


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class grid_print(Grid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        if width == 9:
            self.px = 72
            self.images=[img0, img1, img2, img3, img4, img5, img6, img7, img8, imgB]
        elif width  == 16 :
            self.px = 40
            self.images = [img0, img1, img2, img3, img4, img5, img6, img7, img8, imgB]
        else:
            self.px = 20
            self.images = [img0, img1, img2, img3, img4, img5, img6, img7, img8, imgB]
        self.coord = [(window_size[1]-(self.px*self.height))//2, (window_size[0]-(self.px*self.width))//2]
        self.list_img = [[img_vide for j in range(width)] for i in range(height)]

    def afficher(self):
        y = self.coord[0]
        x = self.coord[1]
        for i in range(self.height):
            for j in range(self.width):
                screen.blit(self.list_img[i][j], (x, y))
                x += self.px
            y += self.px
            x = self.coord[1]

    def coord_click(self):
        mouse = pygame.mouse.get_pos()
        xsouris = mouse[0] - self.coord[1]
        ysouris = mouse[1] - self.coord[0]
        if xsouris < 0 or xsouris > self.width * self.px or ysouris < 0 or ysouris > self.height * self.px:
            print("T'es pas dans la fenêtre")
            return[]
        else :
            return [ysouris // self.px, xsouris // self.px]

    def perte(self, y, x, grid_hide, compteur):
        FPS = 30
        if grid_hide.grid[y][x] == "B":
            compteur += 1
            if grid_hide.grid[y][x] == "B":
                self.afficher()
                pygame.display.flip()
                clock.tick(FPS)
                self.list_img[y][x] = imgB
            if x - 1 >= 0:
                if self.list_img[y][x - 1] != imgB and self.list_img[y][x - 1] != img_done:
                    self.perte(y,x - 1, grid_hide,compteur)
            if x + 1 < len(self.list_img[0]):
                if self.list_img[y][x + 1] != imgB and self.list_img[y][x + 1] != img_done:
                    self.perte(y,x + 1, grid_hide,compteur)
            if y - 1 >= 0:
                if self.list_img[y - 1][x] != imgB and self.list_img[y- 1][x] != img_done:
                    self.perte(y-1, x, grid_hide,compteur)

            if  y + 1 < len(self.list_img):
                if self.list_img[y + 1][x] != imgB and self.list_img[y + 1][x] != img_done:
                    self.perte(y + 1, x, grid_hide,compteur)
        elif compteur > 0:
            self.afficher()
            pygame.display.flip()
            clock.tick(FPS)
            self.list_img[y][x]= img_done
            if x - 1 >= 0:
                if self.list_img[y][x - 1] != imgB and self.list_img[y][x - 1] != img_done:
                    self.perte(y, x - 1, grid_hide, compteur)
            if x + 1 < len(self.list_img[0]):
                if self.list_img[y][x + 1] != imgB and self.list_img[y][x + 1] != img_done:
                    self.perte(y, x + 1, grid_hide, compteur)
            if y - 1 >= 0:
                if self.list_img[y - 1][x] != imgB and self.list_img[y - 1][x] != img_done:
                    self.perte(y - 1, x, grid_hide, compteur)

            if y + 1 < len(self.list_img):
                if self.list_img[y + 1][x] != imgB and self.list_img[y + 1][x] != img_done:
                    self.perte(y + 1, x, grid_hide, compteur)
            return None

    def victoire(self, grid_hide):
        case_hide = 0
        total_bombs = grid_hide.bomb
        for i in range(self.height):
            for j in range(self.width):
                if self.list_img[i][j] == img_vide:

                    case_hide += 1
        if case_hide == total_bombs:
            print("Victoire!")
            return True
        else :
            return False

    def path(self, y, x, grid_hide):
        if self.list_img[y][x] == img0:
            if x - 1 >= 0:
                if self.list_img[y][x - 1] == img_vide:
                    self.retourner(y, x - 1, grid_hide)
                    if self.list_img[y][x - 1] == img0:
                        self.path(y, x - 1, grid_hide)

            if x + 1 < len(self.list_img[0]):
                if self.list_img[y][x + 1] == img_vide:
                    self.retourner(y, x + 1, grid_hide)
                    if self.list_img[y][x + 1] == img0:
                        self.path(y, x + 1, grid_hide)

            if y - 1 >= 0:
                if self.list_img[y - 1][x] == img_vide:
                    self.retourner(y - 1, x, grid_hide)
                    if self.list_img[y - 1][x] == img0:
                        self.path(y - 1, x, grid_hide)

            if  y + 1 < len(self.list_img):
                if self.list_img[y + 1][x] == img_vide:
                    self.retourner(y + 1, x, grid_hide)
                    if self.list_img[y + 1][x] == img0:
                        self.path(y + 1, x, grid_hide)



    def retourner(self, y, x, grid_hide):
        if grid_hide[y][x] != "B" and grid_hide[y][x] != "X":
            self.list_img[y][x]= self.images[int(grid_hide[y][x])]




    def premier_click(self, y, x, grid_hide):
        self.list_img[y][x] = imgX
        if x - 1 >= 0:
            self.retourner(y, x - 1, grid_hide)
            self.path(y, x - 1, grid_hide)
            if y - 1 >= 0:
                self.retourner(y - 1, x - 1, grid_hide)

            if y + 1 < len(self.list_img):
                self.retourner(y + 1, x - 1, grid_hide)

        if x + 1 < len(self.list_img[0]):
            self.retourner(y, x + 1, grid_hide)
            self.path(y, x + 1, grid_hide)
            if y - 1 >= 0:
                self.retourner(y - 1, x + 1, grid_hide)

            if y + 1 < len(self.list_img):
                self.retourner(y + 1, x + 1, grid_hide)

        if y - 1 >= 0:
            self.retourner(y - 1, x, grid_hide)
            self.path(y - 1, x, grid_hide)
        if y + 1 < len(self.list_img):
            self.retourner(y + 1, x, grid_hide)
            self.path(y + 1, x, grid_hide)
        return None



class grid_hide(Grid):
    def __init__(self, width, height, bomb):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.bomb = bomb
        self.grid = [["0" for j in range(width)] for i in range(height)]


    def remplissage(self, y, x):
        """
        Fills the grid with the number of bombs around
        :param y: vertical coordinate of the grid
        :param x: horizontal coordinate of the grid
        """
        if x - 1 >= 0:
            if self.grid[y][x - 1] != "B":
                self.grid[y][x - 1] = str(int(self.grid[y][x - 1]) + 1)

            if y - 1 >= 0 and self.grid[y - 1][x - 1] != "B":
                self.grid[y - 1][x - 1] = str(int(self.grid[y - 1][x - 1]) + 1)

            if y + 1  < len(self.grid) and self.grid[y + 1][x - 1] != "B":
                self.grid[y + 1][x - 1] = str(int(self.grid[y + 1][x - 1]) + 1)

        if x + 1 < len(self.grid):
            if self.grid[y][x + 1] != "B":
                self.grid[y][x + 1] = str(int(self.grid[y][x + 1]) + 1)

            if y - 1>= 0 and self.grid[y - 1][x + 1 ] != "B":
                self.grid[y - 1][x + 1 ] = str(int(self.grid[y - 1][x + 1]) + 1)

            if y + 1 < len(self.grid) and self.grid[y + 1][x + 1] != "B":
                self.grid[y + 1][x + 1] = str(int(self.grid[y + 1][x + 1]) + 1)


        if y - 1 >= 0 and self.grid[y - 1][x] != "B":
            self.grid[y - 1][x] = str(int(self.grid[y -1][x]) + 1)

        if y + 1  < len(self.grid) and self.grid[y + 1][x] != "B":
            self.grid[y + 1 ][x] = str(int(self.grid[y + 1][x]) + 1)

        return None


    def random_grid(self, y, x, coordinated:list):
        """
        Generates a grid around the first click
        :param y: vertical coordinate of the grid
        :param x: horizontal coordinate of the grid
        : coordinated param: allows you to have the first coordinate of the player
        """
        self.grid[coordinated[0]][coordinated[1]] = "X"
        if self.bomb == 0:
            return None
        if (x < coordinated[1] - 2 or x > coordinated[1] + 2) and (y < coordinated[0] - 2 or y > coordinated[0] + 2):
            if self.grid[y][x] != "B":
                self.grid[y][x] = "B"
                self.remplissage(y, x)
                self.bomb -= 1
        y = randint(0, len(self.grid) - 1)
        x = randint(0, len(self.grid[0]) - 1)
        self.random_grid(y, x, coordinated)


    def afficher(self):
        """
        Displays the grid
        """
        for i in range(len(self.grid)):
            print(self.grid[i])
        print()



