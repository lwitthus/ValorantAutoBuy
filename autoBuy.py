import keyboard
import pyautogui
from PIL import Image
import dxcam
import win32gui
from weaponManager import shoppingCart
print("Buyscript started...")
from cords import *


class AutoBuy():
    def __init__(self):
        pass
     
    # Set the default pause time for PyAutoGUI
    pyautogui.PAUSE = 0.05

    # Define the key that is pressed to buy weapons and equipment
    BUY_BUTTON = "b"

    # DEFINDE the green RGB of the "X" to check if the Buy menu is open
    RGB_GREEN = (71, 255, 191)

    # DEFINE the RGB of WHITE
    RGB_WHITE = (255, 255, 255)


    def autoBuy(self, weaponNameToBuy, pistolNameToBuy):
        # This function is called when the hotkey is pressed
        try:
            try:
                hwnd = win32gui.GetForegroundWindow()
                if win32gui.GetWindowText(hwnd) == 'VALORANT  ': # assuming this is the window title of Valorant
                    if self.openBuyMenu():
                        # If the Buy menu is open, call the buyFull function to purchase weapon, pistol and equipment
                        self.buyFull(weaponNameToBuy, pistolNameToBuy)
                        print("bought")
                else:
                    print("The hotkey was not used in the Valorant window.")
                    return (0,0,0) # return a default color if Valorant window is not active
            except Exception as e:
                # Handle any errors that occur while processing the hotkey
                print(f"An error occurred: {e}")
        except:
            pass
            
    def openBuyMenu(self):
        # Get the Color of X to check if the buy menu is already open
        (colorOfX, _) = self.getPixelColor(BUYMENU_X, BUYMENU_Y)
        if colorOfX != self.RGB_WHITE and colorOfX != self.RGB_GREEN:
            # If the Buy menu is not open, press and release the BUY_BUTTON to open the buy menu
            keyboard.press_and_release(self.BUY_BUTTON)
            
        # Update the color of X to check if the buy menu is open
        (colorOfX, _) = self.getPixelColor(BUYMENU_X, BUYMENU_Y)
        
        return colorOfX == self.RGB_WHITE or colorOfX == self.RGB_GREEN
          
        
    def buyFull(self, weaponNameToBuy, pistolNameToBuy):
        self.buyWeapon(weaponNameToBuy)
        self.buyPistol(pistolNameToBuy)
        self.buyShield()
        self.buyUtil()
        # Press the Esc key to close the Buy menu
        keyboard.press_and_release("esc")
        self.rgb_im_last = None

    def buyWeapon(self, weaponNameToBuy):
        # This function buys all the necessary weapons and equipment
        weapon = shoppingCart.getWeapon(weaponNameToBuy)
        if weapon:
            if (self.isWeaponBuyable()):
                x, y = weapon.getWeaponPixel()
                self.moveAndClick(x, y, 1)
        else:
            print("weapon is not defined")
            
    def buyPistol(self, pistolNameToBuy):
        # This function buys the necessary pistol
        pistol = shoppingCart.getPistol(pistolNameToBuy)
        if pistol:
            if (self.isPistolBuyable()): 
                x, y = pistol.getWeaponPixel()
                self.moveAndClick(x, y, 1)
        else:
            print("pistol is not defined")
        
    def buyShield(self):
        # Check if the Shield button is available and click it if it is
        ((r, g, b), rgb_im_last) = self.getPixelColor(SHIELD_N_X, SHIELD_N_Y, self.rgb_im_last)
        if (r < 230 and g < 230 and b < 230):
            self.moveAndClick(SHIELD_X, SHIELD_Y, 1)
        self.rgb_im_last = rgb_im_last

    def buyUtil(self):
        # Click the left, middle, and right utility slots twice each
        self.moveAndClick(LEFT_X, LEFT_Y, 2)
        self.moveAndClick(MID_X, MID_Y, 2)
        self.moveAndClick(RIGHT_X, RIGHT_Y, 2)

    def moveAndClick(self, x, y, times):
        # This function moves the mouse cursor to the specified coordinates and clicks a certain number of times
        pyautogui.moveTo(x, y)
        for i in range(0, times):
            pyautogui.click()

    def getPixelColor(self, x, y, rgb_im_last = None):
        # This function gets the RGB color of a pixel at the specified coordinates
        
        # Use the dxcam library to capture a frame from the game and extract the pixel color
        if rgb_im_last is None:
            # capture a new frame and extract the pixel color
            camera = dxcam.create()
            frame = camera.grab()
            im = Image.fromarray(frame)
            rgb_im = im.convert('RGB')
            del camera
            color = rgb_im.getpixel((x, y))
            return color, rgb_im
        else:
            # extract the pixel color from the existing image
            color = rgb_im_last.getpixel((x, y))
            return color, rgb_im_last

    def isPistolBuyable(self):
        # Check if the Pistol button is available
        ((r1, g1, b1), rgb_im_last) = self.getPixelColor(PISTOL_NEED_X, PISTOL_NEED_Y_SHORTY)
        ((r2, g2, b2), rgb_im_last) = self.getPixelColor(PISTOL_NEED_X, PISTOL_NEED_Y_FRENZY, rgb_im_last)
        ((r3, g3, b3), rgb_im_last) = self.getPixelColor(PISTOL_NEED_X, PISTOL_NEED_Y_GHOST, rgb_im_last)
        ((r4, g4, b4), rgb_im_last) = self.getPixelColor(PISTOL_NEED_X, PISTOL_NEED_Y_SHERIFF, rgb_im_last)
                
        self.rgb_im_last = rgb_im_last
        
        if ((r1 > 230 and g1 > 230 and b1 > 230) or (r2 > 230 and g2 > 230 and b2 > 230)
            or (r3 > 230 and g3 > 230 and b3 > 230) or (r4 > 230 and g4 > 230 and b4 > 230)):
            return False
        else:
            return True

    def isWeaponBuyable(self):
        # Check if the Weapon button is available
        ((r1, g1, b1), rgb_im_last) = self.getPixelColor(WEAPON_NEED_X_1, WEAPON_NEED_Y_1)
        ((r2, g2, b2), rgb_im_last) = self.getPixelColor(WEAPON_NEED_X_2, WEAPON_NEED_Y_2, rgb_im_last)
        ((r3, g3, b3), rgb_im_last) = self.getPixelColor(WEAPON_NEED_X_3, WEAPON_NEED_Y_3, rgb_im_last)
        ((r4, g4, b4), rgb_im_last) = self.getPixelColor(WEAPON_NEED_X_4, WEAPON_NEED_Y_4, rgb_im_last)
        ((r5, g5, b5), rgb_im_last) = self.getPixelColor(WEAPON_NEED_X_5, WEAPON_NEED_Y_5, rgb_im_last)
        
         
        
        self.rgb_im_last = rgb_im_last
        
        if (r1 < 120 and g1 < 120 and b1 < 120 and r2 < 120 and g2 < 120 and b2 < 120 
            and r3 < 120 and g3 < 120 and b3 < 120 and r4 < 120 and g4 < 120 and b4 < 120
            and r5 < 120 and g5 < 120 and b5 < 120):
            return True
        else:
            return False