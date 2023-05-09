class HotkeyManager:
    def __init__(self):
        self.hotkeys = {}

    def add_hotkey(self, key, func, weaponName, pistolName):
        if weaponName or pistolName:
            if not key == "b" and not key == "esc":
                self.hotkeys[key] = {"func": func, "weaponName": weaponName, "pistolName": pistolName}
    
    def remove_hotkey(self, key):
        if key in self.hotkeys:
            del self.hotkeys[key]

    def clear_hotkeys(self):
        self.hotkeys = {}

    def get_hotkey_func(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("func")
        else:
            return None

    def get_hotkey_weaponName(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("weaponName")
        else:
            return None
    
    def get_hotkey_pistolName(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("pistolName")
        else:
            return None
    
    def run_hotkey_func(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            func = hotkey.get("func")
            if func:
                func()
                
    def getAllHotkeys(self):
        return self.hotkeys
                
hotkey_manager = HotkeyManager()