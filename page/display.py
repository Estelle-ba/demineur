import pygame
from classe.generateur import*
global window_size
window_size = (1200,648)
screen = pygame.display.set_mode(window_size)

image_button_start = pygame.image.load("../asset/image/start_button.png")
image_button_tutorial = pygame.image.load("../asset/image/tutorial_button.png")
image_button_restart = pygame.image.load("../asset/image/restart_button.png")
image_button_easy = pygame.image.load("../asset/image/easy_button.png")
image_button_normal = pygame.image.load("../asset/image/normal_button.png")
image_button_hard = pygame.image.load("../asset/image/hard_button.png")
image_button_retour = pygame.image.load("../asset/image/button_retour.png")
image_button_trophy = pygame.image.load("../asset/image/trophy_button.png")
image_button_register = pygame.image.load("../asset/image/register_button.png")






class Button:
    def __init__(self, x, y, width, height,image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.coord=(self.x, self.y)

    def click(self):

        position_height = self.height + self.y
        position_width = self.width + self.x
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < position_width and self.y < mouse[1] < position_height :
            return True
        else:
            return False


button_start = Button((window_size[0]-500)//2,(window_size[1]-500)//2, 500,300,image_button_start)
button_tutorial = Button((window_size[0]-500)//2,(window_size[1]+152)//2,150,240,image_button_tutorial)
button_restart = Button((window_size[0]+20)//2,(window_size[1]+152)//2,150,240,image_button_restart)
button_normal = Button((window_size[0]-181)//2,(window_size[1]-167)//2, 181,167,image_button_normal)
button_easy = Button((window_size[0]-198)//3, (window_size[1]-162)//2, 198, 162,image_button_easy)
button_hard = Button((window_size[0]-175)-355, (window_size[1]-166)//2, 175, 166,image_button_hard)
button_retour = Button((window_size[0])-1200, (window_size[1])-624, 132, 100,image_button_retour)
button_trophy = Button (1100,0,100,200,image_button_trophy)
button_register =  Button (0,530,200,100,image_button_register)


running = 1
running_back = True
tab_difficulty = []
testing_grid = None
testgrid = None
compteur_click = 0



while running_back :
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit(0)

        elif running == 1:
            pygame.display.set_caption("Démineur - Acceuil")
            screen.blit(button_start.image,button_start.coord)
            screen.blit(button_tutorial.image,button_tutorial.coord)
            screen.blit(button_restart.image,button_restart.coord)
            screen.blit(button_trophy.image,button_trophy.coord)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.click():
                    running = 2
                    screen.fill((0,0,0))
                    break
                if button_tutorial.click():
                    running = 3
                if button_restart.click():
                    running = 4
                if button_trophy.click():
                    running = 5


        elif running == 2  :
            pygame.display.set_caption("Démineur - Difficulter")
            screen.fill((0,0,0))
            screen.blit(button_normal.image,button_normal.coord)
            screen.blit(button_easy.image,button_easy.coord)
            screen.blit(button_hard.image,button_hard.coord)
            screen.blit(button_retour.image,button_retour.coord)
            screen.blit(button_trophy.image,button_trophy.coord)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.click():
                    running = 6
                    tab_difficulty = [9,9,10]
                    testgrid = grid_print(tab_difficulty[0], tab_difficulty[1])
                    break
                if button_normal.click():
                    running = 6
                    tab_difficulty = [16, 16, 40]
                    testgrid = grid_print(tab_difficulty[0], tab_difficulty[1])
                    break
                if button_hard.click():
                    running = 6
                    tab_difficulty = [30,16,99]
                    testgrid = grid_print(tab_difficulty[0], tab_difficulty[1])
                    break
                if button_retour.click():
                    running = 1
                    screen.fill((0,0,0))
                if button_trophy.click():
                    running = 5


        elif running == 3  :
            pygame.display.set_caption("Démineur - Tutorial")
            screen.fill((0, 0, 0))
            screen.blit(button_retour.image,button_retour.coord)
            screen.blit(button_trophy.image,button_trophy.coord)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_retour.click():
                    running = 1
                    break
                if button_trophy.click():
                    running = 5

        elif running == 4  :
            pygame.display.set_caption("Démineur - Restart")
            screen.fill((0, 0, 0))
            screen.blit(button_retour.image,button_retour.coord)
            screen.blit(button_trophy.image,button_trophy.coord)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_trophy.click():
                    running = 5
                if button_retour.click():
                    running = 1
                    break


        elif running == 5 :
            pygame.display.set_caption("Démineur - Score")
            screen.fill((0, 0, 0))
            screen.blit(button_retour.image,button_retour.coord)
            screen.blit(button_trophy.image,button_trophy.coord)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_trophy.click():
                    running = 5
                if button_retour.click():
                    running = 1
                    break



        elif running == 6:
            screen.blit(button_register.image, button_register.coord)
            pygame.display.set_caption("Démineur - Jeu")
            testgrid.afficher()
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if compteur_click == 0:
                    coord_gen = testgrid.coord_click()
                    if coord_gen != []:
                        coord_click = testgrid.coord_click()
                        testing_grid = grid_hide(testgrid.width, testgrid.height, tab_difficulty[2])
                        testing_grid.random_grid(coord_gen[0], coord_gen[1], coord_gen)
                        compteur_click += 1
                        testing_grid.afficher()
                        testgrid.premier_click(coord_gen[0], coord_gen[1], testing_grid.grid)
                    print(1, coord_click)
                else:
                    coord_click = testgrid.coord_click()
                    if coord_click != []:
                        if (testgrid.list_img[coord_click[0]][coord_click[1]] == img_vide or
                                testgrid.list_img[coord_click[0]][coord_click[1]] == img_flag):
                            testgrid.retourner(coord_click[0], coord_click[1], testing_grid.grid)
                            testgrid.path(coord_click[0], coord_click[1], testing_grid.grid)
                            testgrid.victoire(testing_grid)
                            testgrid.perte(coord_click[0], coord_click[1],testing_grid,0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if compteur_click > 0:
                    coord_click = testgrid.coord_click()
                    if coord_click != []:
                        if testgrid.list_img[coord_click[0]][coord_click[1]] == img_vide:
                            testgrid.list_img[coord_click[0]][coord_click[1]] = img_flag
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_trophy.click():
                    running = 5
                    screen.fill((0,0,0))
                if button_retour.click():
                    running = 1
                    screen.fill((0, 0, 0))
