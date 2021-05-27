class Cell:
    def __init__(self, x , y, isalive = 0):
        self.x = x
        self.y = y
        self.isalive = isalive
        self.next_state = isalive
        
    def set_alive(self):
        self.isalive = 1
        
    def set_dead(self):
        self.isalive = 0
        
class Grid:
    def __init__(self, width, height, max_generations):
        self.max_generations = max_generations
        self.generation = 0
        
        self.width = width
        self.height = height
        self.grid = self.__add_cells(width, height)
        self.active_cells = []
        
    def __add_cells(self, width, height):
        grid = []
        for x in range(width):
            grid.append([])
            for y in range(height):
                grid[x].append(Cell(x, y))
        return grid
    
    def activate_cell(self, x, y):
        self.grid[x][y].set_alive()

    def deactivate_cell(self, x, y):
        self.grid[x][y].set_dead()
        
    def set_next_state(self, x, y):
        alive = 0
        if(x > 0 and y > 0 and x < self.width - 1 and y < self.height - 1):
            alive += self.grid[x+1][y].isalive
            alive += self.grid[x+1][y+1].isalive
            alive += self.grid[x+1][y-1].isalive
            alive += self.grid[x-1][y].isalive
            alive += self.grid[x-1][y+1].isalive
            alive += self.grid[x-1][y-1].isalive
            alive += self.grid[x][y-1].isalive
            alive += self.grid[x][y+1].isalive
        
        if(self.grid[x][y].isalive):
            if(alive == 2 or alive == 3):
                self.grid[x][y].next_state = 1
            else:
                self.grid[x][y].next_state = 0
                
        else:
            if(alive == 3):
                self.grid[x][y].next_state = 1
                
    def compute_next_state(self):
        for x in range(self.width):
            for y in range(self.height):
                self.set_next_state(x, y)
            
        
    def transition(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].isalive = self.grid[x][y].next_state

    def transition_one(self, x, y):
        self.grid[x][y].isalive = self.grid[x][y].next_state
                
    def simulate(self):
        self.compute_next_state()
        self.transition()
        
    def __str__(self):
        string = ""
        for y in range(self.height):
            for x in range(self.width):
                string += str(self.grid[x][y].isalive) + " "
            string += "\n"
        return string

    def get_value(self, x, y):
        return self.grid[x][y].isalive
    
