from GameOfLife import Grid
import pygame


window_height = 680
window_width = 1280

def main():
    pygame.init()


    window = pygame.display.set_mode((window_width, window_height))

    clock = pygame.time.Clock()
    time = pygame.USEREVENT + 1
    pygame.time.set_timer(time, 100)
    grid = Grid(window_width//10, window_height//10, 100)
    grid.activate_cell(5, 5)
    grid.activate_cell(6, 5)
    grid.activate_cell(7, 5)
    grid.activate_cell(7, 4)
    grid.activate_cell(6, 3)


    move = True
    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    move = not move

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if grid.get_value(pos[0]//10, pos[1]//10) == 1:
                    grid.deactivate_cell(pos[0]//10, pos[1]//10)
                else:
                    grid.activate_cell(pos[0] // 10, pos[1] // 10)

            if event.type == time:
                for x in range(window_width//10):
                    for y in range(window_height//10):
                        if grid.get_value(x, y) == 1:
                            window.fill([100, 0, 0],((x*10, y*10), (10, 10)))
                        else:
                            window.fill([0, 0, 0], ((x * 10, y * 10), (10, 10)))
                if move:
                    grid.simulate()
                pygame.display.flip()


        
if __name__ == '__main__':
    main()

