from GameOfLife import Grid
import pygame


window_height = 680
window_width = 1280
window = pygame.display.set_mode((window_width, window_height))
def main():
    pygame.init()




    clock = pygame.time.Clock()
    time = pygame.USEREVENT + 1
    pygame.time.set_timer(time, 100)
    grid = Grid(window_width//10, window_height//10, 100)
    grid.activate_cell(5, 5)
    grid.activate_cell(6, 5)
    grid.activate_cell(7, 5)
    grid.activate_cell(7, 4)
    grid.activate_cell(6, 3)

    mouse = 0
    move = True
    running = True
    erase = False
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move = not move

                if event.key == pygame.K_e:
                    erase = not erase

                if event.key == pygame.K_m:
                    for x in range(window_width // 10):
                        for y in range(window_height // 10):
                            grid.deactivate_cell(x, y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = 1

            if event.type == pygame.MOUSEBUTTONUP:
                mouse = 0

            if mouse and not erase:
                pos = pygame.mouse.get_pos()
                grid.activate_cell(pos[0] // 10, pos[1] // 10)

            if mouse and erase:
                pos = pygame.mouse.get_pos()
                grid.deactivate_cell(pos[0] // 10, pos[1] // 10)

            if event.type == time:
                for x in range(window_width//10):
                    for y in range(window_height//10):
                        if grid.get_value(x, y) == 1:
                            window.fill([0, 128, 0],((x*10, y*10), (10, 10)))
                        else:
                            window.fill([193, 154, 108], ((x * 10, y * 10), (10, 10)))
                if move:
                    grid.simulate()

                draw_grid()
                pygame.display.flip()

def draw_grid():
    blockSize = 10 #Set the size of the grid block
    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, [78, 53, 36], rect, 1)
        
if __name__ == '__main__':
    main()


