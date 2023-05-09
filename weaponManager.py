import pyautogui

# Definde the windows size
WINDOW_WIDTH, WINDOW_HEIGHT = pyautogui.size()

# Define the divide value in relation to Monitor-Size and Buy menu cords
WEAPON_DIVIDE_1_ROW = 5.23636363636
WEAPON_DIVIDE_2_ROW = 3.03157894737
WEAPON_DIVIDE_3_ROW = 2.14925373134
WEAPON_DIVIDE_4_ROW = 1.65517241379


WEAPON_DIVIDE_1_COLUMN = 2.81318681319
WEAPON_DIVIDE_2_COLUMN = 2.11745244003
WEAPON_DIVIDE_3_COLUMN = 1.6253968254

PISTOL_DIVIDE_COLUMN = 4.03785488959

CLASSIC_DIVIDE_1_ROW = 5.53846153846
SHORTY_DIVIDE_2_ROW = 3.3488372093
FRENZY_DIVIDE_3_ROW = 2.50434782609
GHOST_DIVIDE_4_ROW = 1.92
SHERIFF_DIVIDE_5_ROW = 1.6

class Weapon:
    name = ""
    divide_row = 0
    divide_column = 0
    
    def __init__(self, name, divide_row, divide_column):
        self.name = name
        self.divide_row = divide_row
        self.divide_column = divide_column 
        
    def getWeaponPixel(self):
        return (WINDOW_WIDTH / self.divide_column, WINDOW_HEIGHT / self.divide_row)
    
stinger = Weapon("STINGER", WEAPON_DIVIDE_1_ROW, WEAPON_DIVIDE_1_COLUMN)
spectre = Weapon("SPECTRE", WEAPON_DIVIDE_2_ROW, WEAPON_DIVIDE_1_COLUMN)
bucky = Weapon("BUCKY", WEAPON_DIVIDE_3_ROW, WEAPON_DIVIDE_1_COLUMN)
judge = Weapon("JUDGE", WEAPON_DIVIDE_4_ROW, WEAPON_DIVIDE_1_COLUMN)

bulldog = Weapon("BULLDOG", WEAPON_DIVIDE_1_ROW, WEAPON_DIVIDE_2_COLUMN)
guardian = Weapon("GUARDIAN", WEAPON_DIVIDE_2_ROW, WEAPON_DIVIDE_2_COLUMN)
phantom = Weapon("PHANTOM", WEAPON_DIVIDE_3_ROW, WEAPON_DIVIDE_2_COLUMN)
vandal = Weapon("VANDAL", WEAPON_DIVIDE_4_ROW, WEAPON_DIVIDE_2_COLUMN)

marshal = Weapon("MARSHAL", WEAPON_DIVIDE_1_ROW, WEAPON_DIVIDE_3_COLUMN)
operator = Weapon("OPERATOR", WEAPON_DIVIDE_2_ROW, WEAPON_DIVIDE_3_COLUMN)
ares = Weapon("ARES", WEAPON_DIVIDE_3_ROW, WEAPON_DIVIDE_3_COLUMN)
oding = Weapon("ODIN", WEAPON_DIVIDE_4_ROW, WEAPON_DIVIDE_3_COLUMN)
    
# Pistols
classic = Weapon("CLASSIC", CLASSIC_DIVIDE_1_ROW, PISTOL_DIVIDE_COLUMN)
shorty = Weapon("SHORTY", SHORTY_DIVIDE_2_ROW, PISTOL_DIVIDE_COLUMN)
frenzy = Weapon("FRENZY", FRENZY_DIVIDE_3_ROW, PISTOL_DIVIDE_COLUMN)
ghost = Weapon("GHOST", GHOST_DIVIDE_4_ROW, PISTOL_DIVIDE_COLUMN)
sheriff = Weapon("SHERIFF", SHERIFF_DIVIDE_5_ROW, PISTOL_DIVIDE_COLUMN)

    
class ShoppingCart:
    weapons = []
    pistols = []
    
    def __init__(self, weapons, pistols):
        self.weapons = weapons
        self.pistols = pistols
        
    def getWeapon(self, name):
        for weapon in self.weapons:
            if weapon.name == name:
                return weapon
            
    def getPistol(self, name):
        for pistol in self.pistols:
            if pistol.name == name:
                return pistol 
    
    
weapons = [stinger, spectre, bucky, judge, bulldog, guardian, phantom, vandal, marshal, operator, ares, oding]

pistols = [classic, shorty, frenzy, ghost, sheriff]
    
shoppingCart = ShoppingCart(weapons, pistols)
    
    
