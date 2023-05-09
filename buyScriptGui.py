import sys
import wx
import os
from gui import MyFrame1
from hotKeyListener import HotKeyListener
from autoBuy import AutoBuy
from hotKeyManager import hotkey_manager


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Beispielverwendung
listener = HotKeyListener()

autoBuy = AutoBuy()

class MyCustomFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.weaponName = ""
        self.pistolName = ""

    # Überschreiben der Event-Methoden mit Ihren eigenen Methoden
    def m_textCtrl2OnChar(self, event):
        keycode = event.GetKeyCode()
        if chr(keycode).isalpha():
            self.m_textCtrl2.SetValue(chr(keycode).lower())
            self.hotkey = chr(keycode)

    def m_button5OnButtonClick( self, event ):
        hotkey_manager.add_hotkey(self.hotkey, autoBuy.autoBuy, self.weaponName, self.pistolName)
        self.m_textCtrl2.SetValue("")
        self.m_choice1.SetSelection(0)
        self.m_choice2.SetSelection(0)
        self.weaponName = ""
        self.pistolName = ""
        self.refresh_m_listBox()
        event.Skip()

    def m_choice1OnChoice(self, event):
        selected_option = self.m_choice1.GetString(self.m_choice1.GetSelection())
        self.weaponName = selected_option
        event.Skip()
        
    def m_choice2OnChoice( self, event ):
        selected_option = self.m_choice2.GetString(self.m_choice2.GetSelection())
        self.pistolName = selected_option
        event.Skip()

    def start_buttonOnButtonClick(self, event):
        listener.start()
        self.start_button.Disable()  # disable the start button
        self.stop_button.Enable()   # enable the stop button
        event.Skip()

    def stop_buttonOnButtonClick(self, event):
        listener.stop()
        self.stop_button.Disable()  # disable the stop button
        self.start_button.Enable()  # enable the start button
        event.Skip()

    def m_listBox1OnListBoxDClick(self, event):
        index = self.m_listBox1.GetSelection()
        if index != wx.NOT_FOUND:
            text = self.m_listBox1.GetString(index)
            hotkey = text.split(": ")[1].split()[0]
            hotkey_manager.remove_hotkey(hotkey)
            self.refresh_m_listBox()
        event.Skip()

    def refresh_m_listBox(self): 
        hotkeys = hotkey_manager.getAllHotkeys()
        self.m_listBox1.Clear()
        hotkey_width = 25
        weapon_width = 50
        pistol_width = 50
        for key in hotkeys:
            hotkey = hotkeys[key]
            hotkey_str = f"Hotkey: {key:<{hotkey_width-7}}\t"
            weapon_str = f"Waffe: {hotkey['weaponName']:<{weapon_width-7}}"
            pistol_str = f"Pistole: {hotkey['pistolName']:<{pistol_width-7}}"
            hotkey_display_str = hotkey_str + weapon_str + pistol_str
            self.m_listBox1.Append(hotkey_display_str)

wx.SizerFlags.DisableConsistencyChecks()

app = wx.App()
frame = MyCustomFrame(None)
frame.Show(True)
app.MainLoop()


