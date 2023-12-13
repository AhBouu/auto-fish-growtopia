import pyautogui as py
import keyboard as key
import time
import win32api as wapi
import win32con as wcon
loop = True
water_x = 0
water_y = 0
bait_x = 0
bait_y = 0
x_s = 0
y_s = 0
width_s = 1000
height_s = 1000
def get_pos():
     while loop:
          if key.is_pressed('ctrl'):
             return py.position()
def water_pos():
    global water_x
    global water_y
    py.alert('water_x and water_y')
    time.sleep(1)
    water_x,water_y = get_pos()
    print(water_x,water_y)

#def bait_pos():
    #global bait_x
    #global bait_y
    #py.alert('bait_x and bait_y')
    #time.sleep(1)
    #bait_x,bait_y = get_pos()
    #print(bait_x,bait_y)

def ss_coor ():
    py.alert('x1 and y1 pos')
    x1 , y1 = get_pos()
    py.alert(f'its {x1} and {y1}')
    time.sleep(1)
    py.alert('x2 and y2 pos')
    x2 ,y2 = get_pos()
    py.alert(f'its {x2} and {y2}')
    width = x2 - x1
    height = y2 - y1
    global x_s,y_s,width_s,height_s
    x_s,y_s = x1,y1
    width_s = width
    height_s = height
    
    take_ss(x1,y1,width,height)

def take_ss(x,y,width,height):
    screenshot = py.screenshot(region=(x,y,width ,height))
    screenshot.save('chest.png')


def click(x,y):
     wapi.SetCursorPos((x,y))
     wapi.mouse_event(wcon.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
     time.sleep(0.1)
     wapi.mouse_event(wcon.MOUSEEVENTF_LEFTUP,0,0,0,0)
def detect(t_start):
    while True:
        if key.is_pressed('ctrl+e'):
            py.alert('Ended.')
            return
        if key.is_pressed('ctrl+s'):
            pause()
        print(f"Region: (x={x_s - 10}, y={y_s - 10}, width={width_s}, height={height_s})")
        #print(f"Image dimensions: {py.screenshot().size}")
        try:
         check = py.locateOnScreen('chest.png',region=(x_s -10,y_s - 10,width_s+ 10,height_s + 10),confidence=0.9)
         print(check)
         if check is None :
             #click water
             click(water_x,water_y)
             time.sleep(0.5)
             #click bait
             #click(bait_x,bait_y)
             #time.sleep(1)
             break
        except py.ImageNotFoundException:
             #click water
             click(water_x,water_y)
             time.sleep(0.5)
             #click bait
             #click(bait_x,bait_y)
             #time.sleep(1)
             break
        if time.time() - t_start > 60:
           break
        #sleep to make so that it is less taxing on your pc    
        time.sleep(0.1)
    start_fish()
        
def start_fish():
    #click water
    if key.is_pressed('ctrl+e'):
            py.alert('Ended.')
            return
    if key.is_pressed('ctrl+s'):
            pause()
    else:
     click(water_x,water_y)
     time.sleep(2)
     time_s = time.time()
     detect(time_s)

def start():
    py.alert('Start?')
    time.sleep(1)
    #bait_pos()
    #time.sleep(0.5)
    water_pos()
    time.sleep(0.5)
    ss_coor()
    time.sleep(0.5)
    py.alert('Done getting coordinate.')
    time.sleep(2)
    py.alert('Start Fishing?')
    time.sleep(2)
    start_fish()

def pause():
    py.alert('Continue?')
    time.sleep(1)
    time_s = time.time()
    detect(time_s)

start()

