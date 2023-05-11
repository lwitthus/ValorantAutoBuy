import sys
from time import sleep
import win32gui
import keyboard
import pyautogui
from PIL import Image
import dxcam
# pylint: disable=W0401:wildcard-import,W0614:unused-wildcard-import
from cords import *

from weapon_manager import shoppingCart
print("Buyscript started...")


class AutoBuy():
    def __init__(self):
        self.camera = None

    # Set the default pause time for PyAutoGUI
    pyautogui.PAUSE = 0.05

    # Define the key that is pressed to buy weapons and equipment
    BUY_BUTTON = "b"

    # DEFINDE the green RGB of the "X" to check if the Buy menu is open
    RGB_GREEN = (71, 255, 191)

    # DEFINE the RGB of WHITE
    RGB_WHITE = (255, 255, 255)
    # pylint: disable=R1710:inconsistent-return-statements

    def auto_buy(self, weapon_name_to_buy, pistol_name_to_buy, shield_name_to_buy, utility_bool):
        # This function is called when the hotkey is pressed
        try:
            try:
                # assuming this is the window title of Valorant
                # pylint: disable=I1101:c-extension-no-member
                if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == 'VALORANT  ':
                    self.open_buy_menu()
                    sleep(0.5)
                    if self.is_buy_menu_open():
                        self.buy_full(weapon_name_to_buy,
                                      pistol_name_to_buy, shield_name_to_buy, utility_bool)
                    print("bought")
                else:
                    print("The hotkey was not used in the Valorant window.")
                    # return a default color if Valorant window is not active
                    return (0, 0, 0)
            except Exception as e_e:
                # Handle any errors that occur while processing the hotkey
                print(f"An error occurred: {e_e}")
        except:
            pass

    def is_buy_menu_open(self):
        # Get the Color of X to check if the buy menu is open
        color_of_x = self.get_pixel_color(BUYMENU_X, BUYMENU_Y)
        return color_of_x in (self.RGB_WHITE, self.RGB_GREEN)

    def open_buy_menu(self):
        # Get the Color of X to check if the buy menu is already open
        color_of_x = self.get_pixel_color(BUYMENU_X, BUYMENU_Y)
        if color_of_x not in (self.RGB_WHITE, self.RGB_GREEN):
            # If the Buy menu is not open, press and release the BUY_BUTTON to open the buy menu
            keyboard.press_and_release(self.BUY_BUTTON)

    def buy_full(self, weapon_name_to_buy, pistol_name_to_buy, shield_name_to_buy, utility_bool):
        self.buy_weapon(weapon_name_to_buy)
        self.buy_pistol(pistol_name_to_buy)
        self.buy_shield(shield_name_to_buy)
        if utility_bool:
            self.buy_util()
        # Press the Esc key to close the Buy menu
        keyboard.press_and_release("esc")

    def buy_weapon(self, weapon_name_to_buy):
        # This function buys all the necessary weapons and equipment
        weapon = shoppingCart.get_weapon(weapon_name_to_buy)
        if weapon:
            if self.is_weapon_buyable():
                pixel_x, pixel_y = weapon.get_weapon_pixel()
                self.move_and_click(pixel_x, pixel_y, 1)
        else:
            print("weapon is not defined")

    def buy_pistol(self, pistol_name_to_buy):
        # This function buys the necessary pistol
        pistol = shoppingCart.get_pistol(pistol_name_to_buy)
        if pistol:
            if self.is_pistol_buyable():
                pixel_x, pixel_y = pistol.get_weapon_pixel()
                self.move_and_click(pixel_x, pixel_y, 1)
        else:
            print("pistol is not defined")

    def buy_shield(self, shield_name_to_buy):
        # Check if the Shield button is available and click it if it is
        if shield_name_to_buy == "NoShield":
            return
        if self.is_shield_buyable():
            if shield_name_to_buy == "LightShield":
                self.move_and_click(SHIELD_LIGHT_X, SHIELD_LIGHT_Y, 1)
            if shield_name_to_buy == "HeavyShield":
                self.move_and_click(SHIELD_HEAVY_X, SHIELD_HEAVY_Y, 1)

    def buy_util(self):
        # Click the left, middle, and right utility slots twice each
        self.move_and_click(LEFT_X, LEFT_Y, 2)
        self.move_and_click(MID_X, MID_Y, 2)
        self.move_and_click(RIGHT_X, RIGHT_Y, 2)

    def move_and_click(self, pixel_x, pixel_y, times):
        # This function moves the mouse cursor to the specified coordinates and clicks a certain number of times
        pyautogui.moveTo(pixel_x, pixel_y)
        for _ in range(0, times):
            pyautogui.click()

    def get_pixel_color(self, pixel_x, pixel_y):
        if not self.camera:
            self.camera = dxcam.create()
        max_attempts = 100000
        attempts = 0
        frame = None

        while attempts < max_attempts and frame is None:
            frame = self.camera.grab()
            attempts += 1

        if frame is not None:
            image = Image.fromarray(frame)
            rgb_im = image.convert('RGB')
            color = rgb_im.getpixel((pixel_x, pixel_y))
            return color
        else:
            print("Fehler beim Abrufen des Kamerabildes nach mehreren Versuchen")
            sys.exit(0)

    def is_shield_buyable(self):
        # Check if the Shield button is available
        (r_heavy, g_heavy, b_heavy) = self.get_pixel_color(
            SHIELD_HEAVY_N_X, SHIELD_HEAVY_N_Y)
        (r_light, g_light, b_light) = self.get_pixel_color(
            SHIELD_LIGHT_N_X, SHIELD_LIGHT_N_Y)
        return (r_heavy < 230 and g_heavy < 230 and b_heavy < 230) and (r_light < 230 and g_light < 230 and b_light < 230)

    def is_pistol_buyable(self):
        # Check if the Pistol button is available
        (r_1, g_1, b_1) = self.get_pixel_color(
            PISTOL_NEED_X, PISTOL_NEED_Y_SHORTY)
        (r_2, g_2, b_2) = self.get_pixel_color(
            PISTOL_NEED_X, PISTOL_NEED_Y_FRENZY)
        (r_3, g_3, b_3) = self.get_pixel_color(
            PISTOL_NEED_X, PISTOL_NEED_Y_GHOST)
        (r_4, g_4, b_4) = self.get_pixel_color(
            PISTOL_NEED_X, PISTOL_NEED_Y_SHERIFF)

        return not ((r_1 > 230 and g_1 > 230 and b_1 > 230) or (r_2 > 230 and g_2 > 230 and b_2 > 230)
                    or (r_3 > 230 and g_3 > 230 and b_3 > 230) or (r_4 > 230 and g_4 > 230 and b_4 > 230))

    def is_weapon_buyable(self):
        # Check if the Weapon button is available
        (r_1, g_1, b_1) = self.get_pixel_color(
            WEAPON_NEED_X_1, WEAPON_NEED_Y_1)
        (r_2, g_2, b2_) = self.get_pixel_color(
            WEAPON_NEED_X_2, WEAPON_NEED_Y_2)
        (r_3, g_3, b_3) = self.get_pixel_color(
            WEAPON_NEED_X_3, WEAPON_NEED_Y_3)
        (r_4, g_4, b_4) = self.get_pixel_color(
            WEAPON_NEED_X_4, WEAPON_NEED_Y_4)
        (r_5, g_5, b_5) = self.get_pixel_color(
            WEAPON_NEED_X_5, WEAPON_NEED_Y_5)

        return (r_1 < 120 and g_1 < 120 and b_1 < 120 and r_2 < 120 and g_2 < 120 and b2_ < 120
                and r_3 < 120 and g_3 < 120 and b_3 < 120 and r_4 < 120 and g_4 < 120 and b_4 < 120
                and r_5 < 120 and g_5 < 120 and b_5 < 120)
