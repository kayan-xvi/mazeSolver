#This version is copy pasting the correct sections from 1.0 and 1.1
# While making it work with the way which works using a dictionary inside a class and the exec function
#This is a working MVP of the maze solver 

#This class is used to define the maze's attributes 
class MazeAttributes: 
    def __init__ (self, width, height, layout):
        self.width = width
        self.height = height
        self.layout = layout
        self.startX = None
        self.startY = None
        self.goal = 'B'
        # X counts up as moving to the right 
        # Y counts up as moving down

# Reading the maze dimensions and layout from the txt file 
with open(r'maze4.txt') as r: 
    size = r.readline().split(',')
    layout = r.read()
    maze = MazeAttributes(int(size[0]),int(size[1]),[[]],)
    #print(f'r = {size}')
    #print(f'Width = {maze.width}')s
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

#Class using for counting 
class Counter: 
    def __init__ (self, count):
        self.count = count

nodesExist = Counter(0)

#This class is used to store all of the nodes information, but in a single dictionary 
#
#The form: name = Node('key',{dict})
# Must be used when first creating the instance - frontier and explorred must be instances of this class 
#
#After that the form: name.info['key'] = {dict}
#Can be used to manually add to the dictionary 
class Node: 
    def __init__ (self, name, info):
        self.info = {} 
        self.info[name] = info

#This is creating that starting node ('node0')
nodes = Node('node0',{'name' : 'node0', 'x' : maze.startX, 'y' : maze.startY, 'parent' : None})
frontier = Node('node0',{'name' : 'node0', 'x' : maze.startX, 'y' : maze.startY, 'parent' : None})
explored = Node('node0',{'name' : 'node0', 'x' : maze.startX, 'y' : maze.startY, 'parent' : None})

########
#Need to integrate call counter into the loop to make sure name changes 
nodesExist.count = 1 

#This functions checks whether the position being checked is valid to create a new node using criteria: 
    #Is within the constraints of the maze size 
    #Is not a wall 
    #Has not already been explored 
def checkValidity(x,y): 
    #print(f'X,Y being checked are: {x}, {y}')
    if 0 <= x < maze.width:
        #print('test')
        if 0 <= y < maze.height: 
            #print('test1')
            if maze.layout[y][x] != '#': 
                #print('test2')
                for namesSearched in nodes.info: 
                    #print(type(explored.info))
                    #print(explored.info)
                    #print(explored.info['node0'])
                    #print(namesSearched)
                    #print(f'''{explored.info[namesSearched]['x']} == {x} {explored.info[namesSearched]['x'] == x}''')
                    #print(f'''{explored.info[namesSearched]['y']} == {y} {explored.info[namesSearched]['y'] == y}''')
                    #print(f'''Is matching? {explored.info[namesSearched]['x'] == x and explored.info[namesSearched]['y'] == y}''')
                    #print(f'''Is valid? {not(explored.info[namesSearched]['x'] == x and explored.info[namesSearched]['y'] == y)}''')
                    #print('\n')
                    if nodes.info[namesSearched]['x'] == x and nodes.info[namesSearched]['y'] == y: 
                        #print('test3')
                        #print('FAILEDDDDD2')
                        return False
                return True 
    #print('FAILEDDDDD')
    return False 


#This function can be used for the computer to create its own nodes 
def createNode(parentNode, x, y): 
    i = nodesExist.count
    print(f'node created at {x}, {y}')
    #maze.layout[y][x] =
    #print('\n')
    #print(f'inputNode = {inputNode}')
    #print( f'''inputNode['y'] = {inputNode['y']}''' )
    #print(f'type of inputNode[x] = {inputNode['x']}')
    j = {'name' : 'node' + str(i) , 'x' : x, 'y' : y, 'parent' : parentNode['name']}
    #m = 'name' : 'node' + str(i) , 'x' : x, 'y' : y, 'parent' : parentNode['name']
    #n = 'node' + str(i)
    #print(f'n = {n}')
    #exec( f'''k = {n} : {j}''')
    #p = {}
    #exec(f'''p[str({n})] = {j}''')
    #exec(f'''nodes.info.update(p)''')
    #exec(f'''frontier.info.update(p)''')
    exec( f'''nodes.info['node{i}'] = {j}''')
    exec( f'''frontier.info['node{i}'] = {j}''')
    #print(nodes.info)
    nodesExist.count += 1 

#This function is the container of all exploration functions to identify and create new nodes 
def exploreFromNode(parentNode): 
    print(f'''\nExploring {parentNode['x']}, {parentNode['y']} ''')
    frontier.info.pop(parentNode['name'])
    explored.info[parentNode['name']] = parentNode 
    # tempdict = {parentNode['name'] : parentNode }
    # explored.info.update(tempdict)
    # print(explored.info)
    maze.layout[parentNode['y']][parentNode['x']] = len(list(explored.info.keys()))

    #This sections checks the validity of all around the current node
    if(checkValidity(parentNode['x'], parentNode['y'] - 1)): #above 
        createNode(parentNode, parentNode['x'], parentNode['y'] - 1)
    if(checkValidity(parentNode['x'], parentNode['y'] + 1)): #below
        createNode(parentNode, parentNode['x'], parentNode['y'] + 1)
    if(checkValidity(parentNode['x'] + 1, parentNode['y'])): #right 
        createNode(parentNode, parentNode['x'] + 1, parentNode['y'])
    if(checkValidity(parentNode['x'] - 1, parentNode['y'])): #left
        #print('Creating left')
        createNode(parentNode, parentNode['x'] - 1, parentNode['y'])
    
    #TESTING BLOCK
    # print(f'NODES {nodes.info}')
    # print(f'FRONTIER {frontier.info}')
    # print(f'EXPLORED {explored.info}')
    # print('\n')

#print(nodes.info)
#print(type(nodes.info['node0']))
#print(list(frontier.info.keys()))
#print(frontier.info.keys())
#print(type(list(frontier.info.keys())[0]))
#print(frontier.info[list(frontier.info.keys())[0]])
###############
#exploreFromNode(frontier.info['node0'])

while maze.layout[frontier.info[list(frontier.info.keys())[0]]['y']][frontier.info[list(frontier.info.keys())[0]]['x']] != maze.goal: 
    # print(len(list(frontier.info.keys()))-1)
    exploreFromNode(frontier.info[list(frontier.info.keys())[0]])#[len(list(frontier.info.keys()))-1]])
    

'''
#TESTING BLOCK
print(f'NODES {nodes.info}')
print(f'FRONTIER {frontier.info}')
print(f'EXPLORED {explored.info}')
print('\n')

exploreFromNode(frontier.info['node1'])
#exploreFromNode(nodes.info['node0'])

#TESTING BLOCK
print(f'NODES {nodes.info}')
print(f'FRONTIER {frontier.info}')
print(f'EXPLORED {explored.info}')
'''
#print(frontier.info[list(frontier.info.keys())[0]]['x'])
#print(frontier.info[list(frontier.info.keys())[0]]['y'])
#print(maze.layout[frontier.info[list(frontier.info.keys())[0]]['x']])
#print(maze.layout[frontier.info[list(frontier.info.keys())[0]]['y']][frontier.info[list(frontier.info.keys())[0]]['x']])
'''
while maze.layout[frontier.info[list(frontier.info.keys())[0]]['y']][frontier.info[list(frontier.info.keys())[0]]['x']] != maze.goal: 
    exploreFromNode(frontier.info[list(frontier.info.keys())[0]])
    #TESTING BLOCK
    print(f'NODES {nodes.info}')
    print(f'FRONTIER {frontier.info}')
    print(f'EXPLORED {explored.info}')
    print('\n')
    #break 
'''

for row in range(maze.height):
    print(f'{maze.layout[row]} \n')