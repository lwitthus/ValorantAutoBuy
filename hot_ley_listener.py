from pynput.keyboard import Listener
from hot_key_manager import hotkey_manager


class HotKeyListener:
    def __init__(self):
        self.listener = None

    def start(self):
        if self.listener is None:
            self.listener = Listener(on_press=self.run_hotkey_func)
            self.listener.start()

    def stop(self):
        if self.listener is not None:
            self.listener.stop()
            self.listener = None

    def run_hotkey_func(self, key):
        try:
            if key.char not in ('b', 'esc'):
                weapon_name_to_buy = hotkey_manager.get_hotkey_weapon_name(
                    key.char)
                pistol_name_to_buy = hotkey_manager.get_hotkey_pistol_name(
                    key.char)
                shield_name_to_buy = hotkey_manager.get_hotkey_shield_name(
                    key.char)
                utility_bool = hotkey_manager.get_hotkey_utility_bool(
                    key.char)
                func = hotkey_manager.get_hotkey_func(key.char)
                func(weapon_name_to_buy, pistol_name_to_buy, shield_name_to_buy, utility_bool)
            return
        except:
            pass
