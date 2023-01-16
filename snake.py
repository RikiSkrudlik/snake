import pygame

class snake():
    
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self): #add length of snake
        pass

    def draw(self, surface):
        pass


def drawGrid(width, rows, surface):
    space = width // rows
    x = 0
    y = 0
    for row in range(rows): #Draw a line horizontally and vertically to draw n rows and columns
        x += space
        y += space
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

def redrawWindow(surface):
    global WIDTH, rows
    surface.fill((0, 0, 0))
    drawGrid(WIDTH, rows, surface)
    pygame.display.update()

def main():
    pygame.init()
    global WIDTH, rows
    WIDTH = 500
    rows = 20
    window = pygame.display.set_mode((WIDTH, WIDTH))
    s = snake((255, 0, 0), (10, 10))
    playing = True

    clock = pygame.time.Clock()

    while (playing):
        pygame.time.delay(50)
        clock.tick(10) #Frames per second (10)
        redrawWindow(window)

    pass

main()