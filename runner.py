import pyautogui

def runner():
    while True:
        backpixel = pyautogui.pixelMatchesColor(105,131,(32,33,36), tolerance = 10)
        darkpixel = pyautogui.pixelMatchesColor(260,450,(32,33,36), tolerance = 10)
       
        if((darkpixel == False and backpixel == False)):
            pyautogui.press('space')
        elif(darkpixel == True and backpixel == False):
            pyautogui.press('space')

runner()