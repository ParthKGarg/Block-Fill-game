import pygame
import random

# improvements that can be done:
# arrow key movement --> done
# level maker --> done
# fixed issue with resizing of cell size --> done
# proper level sizing -- done
# restart system --> done
# different colours --> done
# levels file 
# difficulty increase

# Solver for the levels
# mouse play system
# better keys play system hold to fill automatically

pygame.init()
pygame.display.set_caption("Block Fill")

windowWidth = 700
windowHeight = 700
gridSize = 7
cellSizes = {7:65, 8:60, 9:55, 10:50}
cellSize = cellSizes[gridSize]
WHITE = (255,255,255)
DWHITE = (245,245,245)
GRAY = (50,50,50)
DGRAY = (25,25,25)
BLACK = (0,0,0)
RED = (255,0,0)
DRED = (210,0,0)
BLUE = (0,0,255)
DBLUE = (0,0,210)
GREEN = (0,255,0)
DGREEN = (0,210,0)
YELLOW = (255,255,0)
DYELLOW = (210,210,0)
CYAN = (0,139,139)
DCYAN = (0,120,120)
# PINK = (255,192,203)
# DPINK = (255,150,160)
colourList = [(RED,DRED),(BLUE,DBLUE),(GREEN,DGREEN),(YELLOW, DYELLOW),(CYAN, DCYAN)]
# colourList = [PINK, DPINK]


lineThickness = cellSize//10
# lineLength = 1000
font = pygame.font.SysFont('comicsans', 25, True)

window=pygame.display.set_mode((windowWidth,windowHeight), pygame.RESIZABLE)

class cell:
    def __init__(self, pos, cellSize, type, colours):
        self.type = type
        self.pos = pos
        self.button = pygame.Rect(pos[0], pos[1], cellSize, cellSize)
        self.conNeighbour = []
        if self.type == 1:
            self.state = True
        else:
            self.state = False
        self.colour1 = colours[0]
        self.colour2 = colours[1]
        self.center = (self.pos[0] + cellSize/2, self.pos[1] + cellSize/2)
        self.circleRadius = cellSize//6
        self.rectWidth = self.circleRadius*2
        self.rectHeight = cellSize + lineThickness
        self.borderRadius = 3
        self.upper_rect = (self.center[0]-self.circleRadius, self.center[1] - self.rectHeight, self.rectWidth, self.rectHeight)
        self.lower_rect = (self.center[0]-self.circleRadius, self.center[1], self.rectWidth, self.rectHeight)
        self.right_rect = (self.center[0], self.center[1] - self.circleRadius, self.rectHeight, self.rectWidth)
        self.left_rect = (self.center[0]-self.rectHeight, self.center[1] -self.circleRadius, self.rectHeight, self.rectWidth)
    
    def checkWin(self):
        aliveCount = 0
        boxCount = 0
        for cell in cells:
            if cell.state :
                aliveCount += 1
        for i in level:
            for j in i:
                if j != 0:
                    boxCount += 1
        if boxCount == aliveCount:
            return True
        else:
            return False


    def draw(self, window):
        if self.type == 1:
            pygame.draw.rect(window, self.colour1, self.button, border_radius = self.borderRadius)
            pygame.draw.circle(window, self.colour2, (self.center[0],self.center[1]), cellSize//2 -5)
            for i in self.conNeighbour:
                if i == 'w':
                    pygame.draw.rect(window, self.colour2, self.upper_rect)
                if i == 'a':
                    pygame.draw.rect(window, self.colour2, self.left_rect)
                if i == 's':
                    pygame.draw.rect(window, self.colour2, self.lower_rect)
                if i == 'd':
                    pygame.draw.rect(window, self.colour2, self.right_rect)
        elif self.type == 2:
            if self.state:
                pygame.draw.rect(window, self.colour1, self.button, border_radius = self.borderRadius)
                pygame.draw.circle(window, self.colour2, (self.center[0],self.center[1]), self.circleRadius)
                for i in self.conNeighbour:
                    if i == 'w':
                        pygame.draw.rect(window, self.colour2, self.upper_rect)
                    if i == 'a':
                        pygame.draw.rect(window, self.colour2, self.left_rect)
                    if i == 's':
                        pygame.draw.rect(window, self.colour2, self.lower_rect)
                    if i == 'd':
                        pygame.draw.rect(window, self.colour2, self.right_rect)
            else:
                pygame.draw.rect(window, GRAY, self.button, border_radius = self.borderRadius)
        if self.type == 3:
            if self.state:
                pygame.draw.rect(window, self.colour1, self.button, border_radius = self.borderRadius)
                pygame.draw.circle(window, self.colour2, (self.center[0],self.center[1]),self.circleRadius)
                for i in self.conNeighbour:
                    if i == 'w':
                        pygame.draw.rect(window, self.colour2, self.upper_rect)
                    if i == 'a':
                        pygame.draw.rect(window, self.colour2, self.left_rect)
                    if i == 's':
                        pygame.draw.rect(window, self.colour2, self.lower_rect)
                    if i == 'd':
                        pygame.draw.rect(window, self.colour2, self.right_rect)
                if self.checkWin():
                    pygame.draw.circle(window, self.colour2, (self.center[0],self.center[1]), cellSize/2-5)
            else:
                pygame.draw.rect(window, GRAY, self.button, border_radius = self.borderRadius)

def checkDirs(path, cord, dirs):
    n=0
    x,y = cord
    for i in dirs:
        if i=='w' and (x-1,y) in path:
            n+=1
        if i=='a' and (x,y-1) in path:
            n+=1
        if i=='s' and (x+1,y) in path:
            n+=1
        if i=='d' and (x,y+1) in path:
            n+=1

    return n

def neighbours(cords, path, grid_size):
    x, y = cords
    dirs = []
    if x > 0:
        dirs.append('w')
    if y > 0:
        dirs.append('a')
    if x < grid_size:
        dirs.append('s')
    if y < grid_size:
        dirs.append('d')
    return checkDirs(path, cords, dirs)

def levelMaker():
    level = [[0 for _ in range(gridSize)] for _ in range(gridSize)]
    grid_size = gridSize-1

    while True:
        x = random.randint(0, grid_size)
        y = random.randint(0, grid_size)
        length = random.randint(gridSize**2 - gridSize - 5, gridSize**2-gridSize)
        startCords = (x, y)

        path = [startCords]
        currentCords = startCords

        for _ in range(length - 1):
            x, y = currentCords
            directions = ['w', 'a', 's', 'd']
            valid_move = False

            while directions:
                dir = random.choice(directions)
                directions.remove(dir)

                if dir == 'w' and x > 0 and (x-1, y) not in path and neighbours((x-1, y), path, grid_size) < 3:
                    currentCords = (x-1, y)
                    path.append(currentCords)
                    valid_move = True
                    break
                elif dir == 'a' and y > 0 and (x, y-1) not in path and neighbours((x, y-1), path, grid_size) < 3:
                    currentCords = (x, y-1)
                    path.append(currentCords)
                    valid_move = True
                    break
                elif dir == 's' and x < grid_size and (x+1, y) not in path and neighbours((x+1, y), path, grid_size) < 3:
                    currentCords = (x+1, y)
                    path.append(currentCords)
                    valid_move = True
                    break
                elif dir == 'd' and y < grid_size and (x, y+1) not in path and neighbours((x, y+1), path, grid_size) < 3:
                    currentCords = (x, y+1)
                    path.append(currentCords)
                    valid_move = True
                    break

            if not valid_move:
                break

        if len(path) == length and neighbours(path[-1], path, grid_size)<2:
            totalN = 0
            for i in path:
                totalN += neighbours(i, path, grid_size)
            if totalN//len(path) >= 2 and (neighbours(path[-2], path, grid_size)>2 or (neighbours(path[-2], path, grid_size)==2 and random.randint(0,99)<25)):
                break

    for i in range(grid_size+1):
        for j in range(grid_size+1):
            if (i, j) == startCords:
                level[i][j] = 1  
            elif (i, j) == path[-1]:
                level[i][j] = 3  
            elif (i, j) in path:
                level[i][j] = 2

    return level

cells = []
cells2 = []
def levelBuilder(level):
    colours = random.choice(colourList)
    buttonCordsList = []
    buttonx = (windowWidth-cellSize*gridSize-lineThickness*(gridSize-1))/2
    buttony = (windowHeight-cellSize*gridSize-lineThickness*(gridSize-1))/2
    for i in range(gridSize):
        l=[]
        for j in range(gridSize):
            if level[i][j] != 0:
                buttonCordsList.append((buttonx,buttony))
                if level[i][j]==1:
                    c = cell((buttonx,buttony),cellSize,1, colours)
                elif level[i][j]==2:
                    c = cell((buttonx,buttony),cellSize,2, colours)
                elif level[i][j]==3:
                    c = cell((buttonx,buttony),cellSize,3, colours)
                cells.append(c)
                l.append(c)
            else:
                l.append(None)
            buttonx += (cellSize+lineThickness)
        buttony += (cellSize+lineThickness)
        buttonx = (windowWidth-cellSize*gridSize-lineThickness*(gridSize-1))/2
        cells2.append(l)

def removeCorrect(k, currentCords):
    if k[0] == currentCords[0]:
        if k[1]>currentCords[1]:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('d')
        elif k[1]<currentCords[1]:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('a')
    if k[1] == currentCords[1]:
        if k[0]>currentCords[0]:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('s')
        elif k[0]<currentCords[0]:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('w')


def move(event, currentCords):
    flag = False
    if event == 'w':
        if cells2[currentCords[0]-1][currentCords[1]].state == False :
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('w')
            currentCords = (currentCords[0]-1, currentCords[1])
            cells2[currentCords[0]][currentCords[1]].state = True
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('s')
        elif cells2[currentCords[0]-1][currentCords[1]].state == True:
            if 's' in cells2[currentCords[0]-1][currentCords[1]].conNeighbour :
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('w')
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0]-1, currentCords[1])
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('s')
            else:
                flag =True
                cells2[currentCords[0]][currentCords[1]].conNeighbour = []
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0]-1, currentCords[1])

    elif event == 'a':
        if cells2[currentCords[0]][currentCords[1]-1].state == False:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('a')
            currentCords = (currentCords[0], currentCords[1]-1)
            cells2[currentCords[0]][currentCords[1]].state = True
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('d')
        elif cells2[currentCords[0]][currentCords[1]-1].state == True:
            if 'd' in cells2[currentCords[0]][currentCords[1]-1].conNeighbour:
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('a')
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0], currentCords[1]-1)
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('d')
            else:
                flag = True
                cells2[currentCords[0]][currentCords[1]].conNeighbour = []
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0], currentCords[1]-1)

    elif event == 's':
        if cells2[currentCords[0]+1][currentCords[1]].state == False:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('s')
            currentCords = (currentCords[0]+1, currentCords[1])
            cells2[currentCords[0]][currentCords[1]].state = True
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('w')
        elif cells2[currentCords[0]+1][currentCords[1]].state == True :
            if 'w' in  cells2[currentCords[0]+1][currentCords[1]].conNeighbour :
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('s')
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0]+1, currentCords[1])
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('w')
            else:
                flag =True
                cells2[currentCords[0]][currentCords[1]].conNeighbour = []
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0]+1, currentCords[1])

    elif event == 'd':
        if cells2[currentCords[0]][currentCords[1]+1].state == False:
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('d')
            currentCords = (currentCords[0], currentCords[1]+1)
            cells2[currentCords[0]][currentCords[1]].state = True
            cells2[currentCords[0]][currentCords[1]].conNeighbour.append('a')
        elif cells2[currentCords[0]][currentCords[1]+1].state == True:
            if 'a' in cells2[currentCords[0]][currentCords[1]+1].conNeighbour:
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('d')
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0], currentCords[1]+1)
                cells2[currentCords[0]][currentCords[1]].conNeighbour.remove('a')
            else:
                flag =True
                cells2[currentCords[0]][currentCords[1]].conNeighbour = []
                cells2[currentCords[0]][currentCords[1]].state = False
                currentCords = (currentCords[0], currentCords[1]+1)
    if flag:
        for i in path[::-1]:
            if i != currentCords:
                k=i
                cells2[i[0]][i[1]].state = False
                cells2[i[0]][i[1]].conNeighbour = []
            elif i == currentCords:
                removeCorrect(k, currentCords)
                break
    return currentCords

def redrawGameWindow():
    window.fill(DGRAY)
    
    for cell in cells:
        cell.draw(window)

    pygame.display.update()

def glow(cords):
    window.fill(DGRAY)

    cell = cells2[cords[0]][cords[1]]
    x= cell.pos[0]-lineThickness
    y= cell.pos[1]-lineThickness
    
    pygame.draw.rect(window, DWHITE, (x, y, cellSize+lineThickness*2, cellSize+lineThickness*2), width=lineThickness+1, border_radius = cell.borderRadius)
    for cell in cells:
        cell.draw(window)
    pygame.display.update()
    pygame.time.delay(25)

def restart():
    global path, currentCords
    for i in path[1:]:
        cells2[i[0]][i[1]].state = False
        cells2[i[0]][i[1]].conNeighbour = []

    i = path[0]
    cells2[i[0]][i[1]].conNeighbour = []
    
    currentCords = startCords
    path = [startCords]

level = levelMaker()
# for i in level:
#     print(i)
levelBuilder(level)

startCords = tuple()
currentCords = tuple()
for i in range(len(level)):
    for j in range(len(level)):
        if level[i][j]==1:
            startCords = (i,j)
path = [startCords]
currentCords = startCords

run= True
while run:
    pygame.time.delay(50)

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.KEYDOWN:
            flag = False
            if events.key == pygame.K_q:
                run = False
            elif (events.key == pygame.K_w or events.key == pygame.K_UP)  and currentCords[0]!=0 and cells2[currentCords[0]-1][currentCords[1]]!=None:
                currentCords = move('w', currentCords)
                flag = True
            elif (events.key == pygame.K_a or events.key == pygame.K_LEFT) and currentCords[1]!=0 and cells2[currentCords[0]][currentCords[1]-1]!=None:
                currentCords = move('a', currentCords)
                flag = True
            elif (events.key == pygame.K_s or events.key == pygame.K_DOWN) and currentCords[0]!=len(level)-1 and cells2[currentCords[0]+1][currentCords[1]]!=None:
                currentCords = move('s', currentCords)
                flag = True
            elif (events.key == pygame.K_d or events.key == pygame.K_RIGHT) and currentCords[1]!=len(level)-1 and cells2[currentCords[0]][currentCords[1]+1]!=None:
                currentCords = move('d', currentCords)
                flag = True
            elif (events.key == pygame.K_r):
                restart()
            
            if flag:
                if currentCords in path:
                    for i in path[::-1]:
                        if i != currentCords:
                            path.pop()
                        else:
                            break
                elif currentCords not in path:
                    path.append(currentCords)

    redrawGameWindow()
    
    if cells[0].checkWin():
        for i in path:
            glow(i)
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                break
        run = False

pygame.quit()