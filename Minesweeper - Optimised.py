import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from helium import *
import time
import cv2
import numpy as np

import SweeperSolver

class minesweeper_identifiers:
    def __init__(self):
        self.top_bar_height = 60
        self.difficulty_info = {
                'hard':{
                    'style':'width: 600px; height: 560px;',
                    'dimensions':(24,20),
                    },
                
                'medium':{
                    'style':'width: 540px; height: 480px;',
                    'dimensions':(18,14),
                    },
                
                'easy':{
                    'style':'width: 450px; height: 420px;',
                    'dimensions':(10,8),
                    }
            }
        self.number_colours = {#hsv ranges
                '1':[[103,209,202],[105,232,212]],
                '2':[[61,151,142],[61,154,142]],
                '3':[[0,162,210],[0,199,211]] ,
                '4':[[136,127,158],[144,220,162]],
                '5':[[17,216,207],[17,255,255]],
                '6':[[91,219,166],[95,255,167]],
                '_':[[14,72,212],[15,78,230]],
            }
minesweeper_info = minesweeper_identifiers()

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def screenshot_element(element):#alternative buggy method
    image = element.screenshot(os.path.join(os.path.dirname(__file__),"screenshot.png"))
    image = cv2.imread(os.path.join(os.path.dirname(__file__),"screenshot.png"), 1) 
    image = np.array(image)
    return image

def screenshot_element2(element, screensize):
    driver.save_screenshot("screenshot.png")
    #driver.save_screenshot("entire screenshot.png")
    img = cv2.imread(os.path.join(os.path.dirname(__file__),"screenshot.png"), 1)
    img = cv2.resize(img, screensize) 

    top = element.location['y']+minesweeper_info.top_bar_height
    bottom = element.location['y']+element.size['height']
    left = element.location['x']
    right = element.location['x']+element.size['width']

    #top, bottom, left, right = int(top),int(bottom),int(left),int(right)
    
    crop_img = img[top:bottom,left:right]
    #cv2.imwrite('screenshot.png', crop_img)
    #img = cv2.imread(os.path.join(os.path.dirname(__file__),"screenshot.png"), 1) 
    img = np.array(crop_img)
    return crop_img

def colourinimage(img, min_hsv, max_hsv):
    MIN = np.array(min_hsv,np.uint8)
    MAX = np.array(max_hsv,np.uint8)

    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    frame_threshed = cv2.inRange(hsv_img, MIN, MAX)

    #cv2.imwrite('screenshot_edited2.png', img)

    if cv2.countNonZero(frame_threshed) == 0:
        return False #mask is all black therefore colour not present
    else:
        return True

def convert2table(img, difficulty):
    img_height, img_width, channels = img.shape
    rows, columns = minesweeper_info.difficulty_info[difficulty]['dimensions'][1], minesweeper_info.difficulty_info[difficulty]['dimensions'][0]
    grid = [[' ']*columns for _ in range(rows)]
    
    width = int(img_width/columns)
    height = int(img_height/rows)

    for row in range(rows): 
        for column in range(columns):
            x = int(column*(width))
            y = int(row*(height))

            margin = int(width/2.5)
            crop_img = img[y+margin:y+height-margin, x+margin:x+width-margin]
            for key, value in minesweeper_info.number_colours.items():
                if colourinimage(crop_img, value[0], value[1]):
                    #img = cv2.putText(img, key, (x,y+height), cv2.FONT_HERSHEY_SIMPLEX,  
                    #1, (255,255,255), 2, cv2.LINE_AA)
                    grid[row][column] = key
                    break
                    
    #cv2.imwrite('screenshot_edited.png', img)
    return {'data':grid,
            'image':img, 
            }

def visualise_mines(img, data, difficulty, element, autoclick):
    img_height, img_width, channels = img.shape
    rows, columns = minesweeper_info.difficulty_info[difficulty]['dimensions'][1], minesweeper_info.difficulty_info[difficulty]['dimensions'][0]

    width = int(img_width/columns)
    height = int(img_height/rows)
        
    squares = []
    
    x_mines = []
    y_mines = []
    for row, line in enumerate(data):
        for column, square in enumerate(line):
            x = int(column*(width))
            y = int(row*(height))
            if square > 0:
                #img = cv2.putText(img, str(square), (x,int(y+height/2)), cv2.FONT_HERSHEY_SIMPLEX,  
                #    0.3, (0,0,255), 1, cv2.LINE_AA)
                squares.append([square, x, y])

                coordinate = (int(element.location['x']+x),int(element.location['y']+minesweeper_info.top_bar_height+y))
                
    #cv2.imwrite('screenshot_edited2.png', img)

    draw_rect = '''
        //Position parameters used for drawing the rectangle
        var x = {x};
        var y = {y};
        var width = {width};
        var height = {height};

        var canvas = document.createElement('canvas'); //Create a canvas element
        canvas.id='cheat_overlay'
        //Set canvas width/height
        canvas.style.width='100%';
        canvas.style.height='100%';
        //Set canvas drawing area width/height
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        //Position canvas
        canvas.style.position='absolute';
        canvas.style.left=0;
        canvas.style.top=0;
        canvas.style.zIndex=100000; 
        canvas.style.pointerEvents='none'; //Make sure you can click 'through' the canvas
        document.body.appendChild(canvas); //Append canvas to body element
        var context = canvas.getContext('2d');
        //Draw rectangle
        context.rect(x, y, width, height);
        context.fillStyle = 'yellow';
        context.stroke();
    '''

    clear_canvas = '''
        var canvas = document.getElementById("cheat_overlay");
        canvas.parentNode.removeChild(canvas);
    '''

    
    sorted_squares = sorted(squares)
    if len(sorted_squares) > 0:
        og_coordinate = (int(element.location['x']+sorted_squares[0][1]),int(element.location['y']+minesweeper_info.top_bar_height+sorted_squares[0][2]))
        coordinate = (og_coordinate[0]*1.01, og_coordinate[1])
        try:driver.execute_script(clear_canvas)
        except:pass
        driver.execute_script(draw_rect.format(x=coordinate[0], y=coordinate[1], width=width, height=height))
        if autoclick == True:
            set_driver(driver)
            click(Point(int(og_coordinate[0]+(width*0.7)),int(og_coordinate[1]+(height*0.7))) )
            #time.sleep(0.01)

def auto_flag(img, data, difficulty, element):
    img_height, img_width, channels = img.shape
    rows, columns = minesweeper_info.difficulty_info[difficulty]['dimensions'][1], minesweeper_info.difficulty_info[difficulty]['dimensions'][0]

    width = int(img_width/columns)
    height = int(img_height/rows)

    coordinates = []
    for row, line in enumerate(data):
        for column, square in enumerate(line):
            x = int(column*(width))
            y = int(row*(height))
            if square == 1:
               coordinate = (int(element.location['x']+x+width/2),int(element.location['y']+minesweeper_info.top_bar_height+y+height/2))
               coordinates.append(coordinate)
    
    for coordinate in coordinates:
        set_driver(driver)
        coordinate = (coordinate[0]*1.01, coordinate[1])
        rightclick(Point(int(coordinate[0]),int(coordinate[1])) )

                
options = webdriver.ChromeOptions()
options.add_argument("window-size=700,700")
driver_path = os.path.join(os.path.dirname(__file__),"chromedriver.exe")
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(executable_path=driver_path, options=options)

driver.get('https://www.google.com/search?client=opera&q=minesweeper&sourceid=opera&ie=UTF-8&oe=UTF-8')

board = None
difficulty = None
wait = input('start:')
while board == None:
    for key, value in minesweeper_info.difficulty_info.items():
        try:
            search_phrase = ("//*[contains(@style, '{}')]".format(value['style']))
            print(search_phrase)
            board = driver.find_elements_by_xpath(search_phrase)[0]
            difficulty = key
            break
        except:
            pass
    
print (board)
print ('mode:', difficulty)
print ('size:', board.size['width'],',', board.size['height'])
print ('> game board found')

screensize = (driver.execute_script("return window.innerWidth"), #Get size of the part of the screen visible in the screenshot
              driver.execute_script("return window.innerHeight"))
while True:
    #screensize = (driver.execute_script("return window.innerWidth"), #Get size of the part of the screen visible in the screenshot
    #          driver.execute_script("return window.innerHeight"))
    #board = driver.find_elements_by_xpath(search_phrase)[0]
    
    boardscreenshot = screenshot_element2(board, screensize)
    boarddata = convert2table(boardscreenshot, difficulty)

    mine_data = SweeperSolver.Assemble_Mine_Data(boarddata['data'])
    #for i in mine_data:
    #    print(i)
    visualise_mines(boarddata['image'], mine_data, difficulty, board, autoclick = True)
    #print(mine_data)

    #auto_flag(boarddata['image'], mine_data, difficulty, board)
    #auto_flag(boarddata['image'], mine_data, difficulty, board)

    #wait = input('input to refresh:')

