import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

GAME_URL = "https://elgoog.im/dinosaur-game/"

# using chrome as browser, pre-downloaded chrome driver
chrome_driver_path = "chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=service)

# open website full screen
driver.get(GAME_URL)
driver.maximize_window()


if __name__ == "__main__":
    time.sleep(2)
    # start game by pressing up key
    pyautogui.keyDown('up')
    # give game time to expand
    time.sleep(5)

    # THE FOLLOWING CODE WAS ONLY RUN ONCE, TO GET THE LOCATION ON THE SCREEN AND DETERMINE A RANGE
    # get position of Dino on the screen
    # screenshot 'dino.png' was taken beforehand
    dino_position = pyautogui.locateCenterOnScreen('dino.png', region=(0, 600, 500, 300), confidence=0.9)
    print(dino_position)
    # Point(x=152, y=781)

    # find color of background, first locating the mouse position to make sure it's on background, then use position
    # to get color
    mouse = pyautogui.position()
    background_color = pyautogui.pixel(mouse[0], mouse[1])
    print(background_color)
    # (255, 255, 255)

    original_x = 160
    while True:
        # check if there is an obstacle by checking if there is a colored pixel
        for x in range(int(original_x), int(original_x) + 3):
            for y in range(785, 790):
                if not pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
                    pyautogui.sleep(.15)
                    print(x, y)
                    pyautogui.sleep(.1)
                    # add a small amount to original_x as obstacles move faster the longer the game goes on
                    original_x += 0.1
                    pyautogui.keyDown('up')
                    break