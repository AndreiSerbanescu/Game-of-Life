import pygame

from src import Settings
from src.Grid import *
from src.Position import *
from src.Cell import *

def make_number(str_number):
    if str_number < 10:
        return "00" + str(str_number)

    if str_number < 100:
        return "0" + str(str_number)

    return str(str_number)




pygame.init()

pygame.display.init()
screen = pygame.display.set_mode((Settings.SCREENWIDTH, Settings.SCREENHEIGHT))
fps_clock = pygame.time.Clock()

grid = Grid()

for i in range(Settings.COLLNO):
    for j in range(Settings.ROWNO):
        grid.cells[i][j] = Cell(Position(i, j))

WHITE = (255, 255, 255)

print(grid.size)
is_paused = True
FPS = Settings.FPS
fpsCount = 0
take_screenshot = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.key == pygame.K_p:
                is_paused = not is_paused
            elif event.key == pygame.K_SPACE:
                take_screenshot = True


    if is_paused:
        FPS = 120
    else:
        FPS = Settings.FPS

    mousePos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        grid.cells[mousePos[0] // Settings.CELLSIZE]\
        [mousePos[1] // Settings.CELLSIZE].is_alive = True

    screen.fill(WHITE)

    grid.render(screen)


    if Settings.FILM and fpsCount % 1 == 0 and not is_paused:
        pygame.image.save(screen, "screenshot" + make_number(fpsCount) + ".jpg")

    if take_screenshot:
        pygame.image.save(screen, "screenshot" + str(fpsCount) + ".jpg")
        take_screenshot = False

    if not is_paused:
        grid.update()
        fpsCount += 1

    pygame.display.update()
    fps_clock.tick(FPS)
