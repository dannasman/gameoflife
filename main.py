from GameOfLife import Grid

def main():
    grid = Grid(30, 30, 3)
    grid.activate_cell(5, 5)
    grid.activate_cell(5, 6)
    grid.activate_cell(5, 7)
    grid.activate_cell(5, 8)
    grid.activate_cell(5, 9)
    
    grid.activate_cell(3, 7)
    grid.activate_cell(4, 7)
    grid.activate_cell(6, 7)
    grid.activate_cell(7, 7)
    
    grid.activate_cell(6, 8)
    
    grid.simulate()
        
main()

