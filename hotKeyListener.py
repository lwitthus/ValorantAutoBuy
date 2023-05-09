from pynput.keyboard import Listener
from hotKeyManager import hotkey_manager

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
            
    def run_hotkey_func(_, key):
        try:
            if (key.char != "b" and key.char != "esc"):
                weaponNameToBuy = hotkey_manager.get_hotkey_weaponName(key.char)
                pistolNameToBuy = hotkey_manager.get_hotkey_pistolName(key.char)
                func = hotkey_manager.get_hotkey_func(key.char)
                func(weaponNameToBuy, pistolNameToBuy)
        except:
            return hotkey_manager.get_hotkey_func(key)