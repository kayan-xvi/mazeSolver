class Counter: 
    def __init__ (self, count):
        self.count = count

class Node: 
    def __init__ (self, x, y, parent, parentX, parentY):
        self.x = x
        self.y = y
        self.parent = parent
        self.parentX = parentX
        self.parentY = parentY

class MazeAttributes: 
    def __init__ (self, width, height, layout, startX, startY, frontier, explored):
        self.width = width
        self.height = height
        self.layout = layout
        self.startX = startX
        self.startY = startY
        self.frontier = frontier
        self.explored = explored
        # X counts up as moving to the right 
        # Y counts up as moving down

# Reading the maze dimensions and layout from the txt file 
with open(r'c:\Users\kayan\Documents\Code\Python\CS50\Maze\maze1.txt') as r: 
    size = r.readline().split(',')
    layout = r.read()
    maze = MazeAttributes(int(size[0]),int(size[1]),[[]],0,0,[],[])
    
    #print(f'r = {size}')
    #print(f'Width = {maze.width}')
    #print(f'Height = {maze.height}')

#Translating the maze from a string in 'layout' to single strings in an embedded array in maze.layout
newLines = 0 
for row in range(maze.height):
    for column in range(maze.width):
        if layout[column + row * maze.width + newLines] == '\n':
            newLines += 1 
        maze.layout[row].append(layout[column + row * maze.width + newLines])
    maze.layout.append([])

    #print(len(r.read()))

# Finding the start coordinates of the maze (A) 
for row in range(maze.height):
    print(f'{maze.layout[row]} \n')
    for column in range(maze.width):
        if maze.layout[row][column] == 'A':
            maze.startX = column
            maze.startY = row
            
            #print(row)
            #print(column)
            #print(maze.startX)
            #print(maze.startY)

#Creating the starting node of search to be at position A 
#print(f'maze.startY = {maze.startY}') 
#print(f'maze.startX = {maze.startX}')
#print(type(maze.startY))
start = Node(maze.startX, maze.startY,'-','-','-')
#print(f'start.y = {start.y}')
#print(f'start.x = {start.x}')
searchFromNodeClass = Counter(0)

#Checks to see if the Node has already been searched 
def checkExploredUp(node): 
    
    for nodes in maze.explored: 
        #print(f'node type: {type(nodes)}')
        if node.x == nodes.x and node.y - 1 == nodes.y: 
            return True 
    return False 
def checkExploredDown(node): 
    
    for nodes in maze.explored: 
        #print(f'node type: {type(nodes)}')
        if node.x == nodes.x and node.y + 1 == nodes.y: 
            return True 
    return False 
def checkExploredLeft(node): 
    
    for nodes in maze.explored: 
        #print(f'node type: {type(nodes)}')
        if node.x - 1 == nodes.x and node.y == nodes.y: 
            return True 
    return False 
def checkExploredRight(node): 
    
    for nodes in maze.explored: 
        #print(f'node type: {type(nodes)}')
        if node.x + 1 == nodes.x and node.y == nodes.y: 
            return True 
    return False 

#Searching in each horizontal and vertical direction from the node 
def searchFromNode(node): 
    searchFromNodeClass.count += 1 
    maze.explored.append(node)
    #print(maze.explored)
    #print(node.y)
    if node.y != 0: 
        print('test')
        if checkExploredUp(node) == False:
            print('test2')
            print(searchFromNodeClass.count)
            exec(f'node{searchFromNodeClass.count} = Node(node.x, node.y - 1, node, node.x, node.y)')
            print(node1)

    '''
    if node.x != maze.width -1: 

    if node.y != 0: 

    if node.y != maze.height -1: 
    '''

#print(type(maze.explored))
searchFromNode(start)
print(searchFromNodeClass.count)