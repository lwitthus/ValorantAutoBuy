class HotkeyManager:
    def __init__(self):
        self.hotkeys = {}

    def add_hotkey(self, key, func, weapon_name, pistol_name, shield_name, utility_bool):
        if weapon_name or pistol_name or shield_name or utility_bool:
            if not key == "b" and not key == "esc" and not key is None:
                self.hotkeys[key] = {"func": func, "weaponName": weapon_name,
                                     "pistolName": pistol_name, "shieldName": shield_name, "utility_bool": utility_bool}

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

    def get_hotkey_weapon_name(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("weaponName")
        else:
            return None

    def get_hotkey_pistol_name(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("pistolName")
        else:
            return None

    def get_hotkey_shield_name(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("shieldName")
        else:
            return None

    def get_hotkey_utility_bool(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            return hotkey.get("utility_bool")
        else:
            return None

    def run_hotkey_func(self, key):
        hotkey = self.hotkeys.get(key)
        if hotkey:
            func = hotkey.get("func")
            if func:
                func()

    def get_all_hotkeys(self):
        return self.hotkeys


hotkey_manager = HotkeyManager()
