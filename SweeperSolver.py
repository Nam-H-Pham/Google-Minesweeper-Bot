data = [['1', 'X', '_', '_', '_', '_', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '_', '1', '1', '1', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '_', '1', ' ', '1', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '_', '1', '1', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '_', '_', '_', ' ', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '1', ' ', ' ', ' ', '1', '1', '2', ' ', ' ', ' ', ' ', '_', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '1', '_', '1', ' ', ' ', ' ', ' ', '_', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', '_', '_', '1', ' ', ' ', ' ', ' ', '_', '2'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', '1', '_', '1', ' ', ' ', ' ', ' ', '_', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', '_', '2', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '_', '2', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', '_', '1', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '2', '1', '1', '2', '1', '1', '1', '1', '1', '_', '1', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', '1', '_', '_', '_', '_', '_', '_', '_', '_', '_', '1', ' ', ' ', ' ', ' ', ' ', ' ']]
data = [
[' ', ' ', ' ', ' ', ' ', '1', '_', '_', '_', '1', '2', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', '2', '1', '_', '_', '1', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', 'X', '2', '_', '_', '1', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', '5', '2', '1', '_', '2', '+', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', '1', 'X', '2', '+', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'X', 'X', '4', '2', '1', '1', 'X', '+', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'X', '3', '1', '_', '_', '1', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', '1', '1', '_', '_', '_', '_', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', 'X', '2', '2', '1', '_', '1', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', 'X', 'X', '2', '2', '2', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

data = [
[' ', ' ', ' ', ' ', ' ', '1', '_', '_', '_', '1', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', '2', '1', '_', '_', '1', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', '2', '_', '_', '1', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', '5', '2', '1', '_', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1', ' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#not neccessary, testing purposes only
[' ', ' ', ' ', ' ', ' ', ' ', '4', '2', '1', '1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', '3', '1', '_', '_', '1', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', '1', '1', '_', '_', '_', '_', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', '2', '2', '1', '_', '1', '2', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '2', '2', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
import itertools

def flatten_list(nasted_list):
    list_of_lists = []
    for item in nasted_list:
        list_of_lists.extend(item)
    return list_of_lists

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def Get_Square_(direction, data, row, column, dimensions):
    try:
        square = None
        if direction == None:
            square = data[row][column]
            row, column = [row, column]
        
        if direction == 'up':
            square = data[row-1][column]
            row, column = [row-1, column]
        if direction == 'down':
            square = data[row+1][column]
            row, column = [row+1, column]
        if direction == 'left':
            square = data[row][column-1]
            row, column = [row, column-1]
        if direction == 'right':
            square = data[row][column+1]
            row, column = [row, column+1]

        if direction == 'up-left':
            square = data[row-1][column-1]
            row, column = [row-1, column-1]
        if direction == 'up-right':
            square = data[row-1][column+1]
            row, column = [row-1, column+1]
        if direction == 'down-left':
            square = data[row+1][column-1]
            row, column = [row+1, column-1]
        if direction == 'down-right':
            square = data[row+1][column+1]
            row, column = [row+1, column+1]

        if row not in range(dimensions[0]) or column not in range(dimensions[1]):
            return None

        return {'row': row,
            'column': column,
            'value': square,
            }
    except:
        return None

def Process_Data(mine_data, data):
    og_mine_data, og_data = mine_data, data
    columns = len(data[0])
    rows = len(data)

    total_possible_mines = []
    list_of_mine_combinations = []
                                
    
    for row, line in enumerate(data):
        for column, square in enumerate(line):
            if RepresentsInt(square):
                if int(square) > 0:
                    surrounding_directions = ['up','down','left','right','up-left','up-right','down-left','down-right']
                    possible_mines = []

                    absolute_mines = []
                    for direction in surrounding_directions:
                        square = Get_Square_(direction, data, row, column, [rows,columns])
                        if square != None and square['value'] == ' ':
                            #mine_data[square['row']][square['column']] += int(data[row][column])

                            possible_mines.append(square)
                            if square not in total_possible_mines:
                                total_possible_mines.append(square)
                        if square != None and square['value'] == 'X':
                            absolute_mines.append(square)
                                
                    if len(possible_mines+absolute_mines) == int(data[row][column]):
                        for mine in possible_mines:
                            og_data[mine['row']][mine['column']] = 'X'
                            og_mine_data[mine['row']][mine['column']] = 1
                            #print('replaced mine')
                            if mine['value'] == '_':
                                absolute_mines.append(mine)
                                
                    mine_combinations = list(itertools.combinations(possible_mines, int(data[row][column])))
                    for index, combo in enumerate(mine_combinations):
                        if 'X' in combo or '_' in combo or ' ' in combo:
                            mine_combinations.pop(index)
                    list_of_mine_combinations.append(mine_combinations)

    return og_mine_data, og_data, total_possible_mines, list_of_mine_combinations

def Process_Data2(mine_data, data):
    og_mine_data, og_data = mine_data, data
    columns = len(data[0])
    rows = len(data)
    
    for row, line in enumerate(data):
        for column, square in enumerate(line):
            if RepresentsInt(square):
                if int(square) > 0:
                    surrounding_directions = ['up','down','left','right','up-left','up-right','down-left','down-right']
                    possible_mines = []

                    absolute_mines = []                    
                    for direction in surrounding_directions:
                        square = Get_Square_(direction, data, row, column, [rows,columns])
                        if square != None and square['value'] == ' ':
                            #mine_data[square['row']][square['column']] += int(data[row][column])
                            possible_mines.append(square)
                        if square != None and square['value'] == 'X':
                            absolute_mines.append(square)
                            
                    #print(absolute_mines)
                    if len(absolute_mines) == int(data[row][column]):
                        for mine in possible_mines:
                            if mine not in absolute_mines:
                                og_data[mine['row']][mine['column']] = '+'
                                og_mine_data[mine['row']][mine['column']] = 0.001
                      
    return og_mine_data, og_data

def Assemble_Mine_Data(data):
    mine_data = [[0]*(len(data[0])) for _ in range(len(data))]
    

    mine_data, data, total_possible_mines, list_of_mine_combinations = Process_Data(mine_data, data)#get absolute mines
    mine_data, data = Process_Data2(mine_data, data)#get absolute not mines
    mine_data, data, total_possible_mines, list_of_mine_combinations = Process_Data(mine_data, data)#get combos
    
    #print(list_of_mine_combinations)
    #for combo in list_of_mine_combinations:
    #    print (combo)
    for possible_mine in total_possible_mines:
        valid_combinations = []
        for combinations in list_of_mine_combinations:
            if possible_mine in flatten_list(combinations):
                valid_combinations.append(combinations)
                
        number_present_in = 0
        number_absent_in = 0
        for combo in flatten_list(valid_combinations):
            if possible_mine in combo:
                number_present_in += 1
            else:
                number_absent_in += 1

        #print(number_present_in,'/',number_present_in+number_absent_in)
        try:
            probability = round(number_present_in/(number_present_in+number_absent_in),3)
            #print(probability)
            mine_data[possible_mine['row']][possible_mine['column']] += probability
        except:
            pass

    #print(mine_data)
    return mine_data
'''
for i in (data):
    print(i)
print('-'*8) 
for i in Assemble_Mine_Data(data):
    print(i)'''
#print(Assemble_Mine_Data(data))
