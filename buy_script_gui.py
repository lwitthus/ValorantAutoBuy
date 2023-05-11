import wx
from gui import MyFrame1
from hot_ley_listener import HotKeyListener
from auto_buy import AutoBuy
from hot_key_manager import hotkey_manager

# Beispielverwendung
listener = HotKeyListener()

auto_buy = AutoBuy()


class MyCustomFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.weapon_name = ""
        self.pistol_name = ""
        self.shield_name = "NoShield"
        self.utility_name = "NoUtility"
        self.hotkey = None
        self.utility_bool = False

    # Überschreiben der Event-Methoden mit Ihren eigenen Methoden
    def m_textCtrl2OnChar(self, event):
        keycode = event.GetKeyCode()
        if chr(keycode).isalpha():
            self.m_textCtrl2.SetValue(chr(keycode).lower())
            self.hotkey = chr(keycode)

    def m_button5OnButtonClick(self, event):
        hotkey_manager.add_hotkey(
            self.hotkey, auto_buy.auto_buy, self.weapon_name, self.pistol_name, self.shield_name, self.utility_bool)
        self.reset_gui()
        self.refresh_m_list_box()

        event.Skip()

    def reset_gui(self):
        self.m_textCtrl2.SetValue("")
        self.m_choice1.SetSelection(0)
        self.m_choice2.SetSelection(0)
        self.m_radioBox1.SetSelection(0)
        self.m_radioBox2.SetSelection(0)
        self.weapon_name = ""
        self.pistol_name = ""
        self.shield_name = "NoShield"
        self.utility_name = "NoUtility"
        self.utility_bool = False

    def m_choice1OnChoice(self, event):
        selected_option = self.m_choice1.GetString(
            self.m_choice1.GetSelection())
        self.weapon_name = selected_option
        event.Skip()

    def m_choice2OnChoice(self, event):
        selected_option = self.m_choice2.GetString(
            self.m_choice2.GetSelection())
        self.pistol_name = selected_option
        event.Skip()

    def m_radioBox1OnRadioBox(self, event):
        selected_option = event.GetEventObject().GetSelection()
        if selected_option == 0:
            self.shield_name = "NoShield"
        if selected_option == 1:
            self.shield_name = "LightShield"
        if selected_option == 2:
            self.shield_name = "HeavyShield"
        event.Skip()

    def m_radioBox2OnRadioBox(self, event):
        selected_option = event.GetEventObject().GetSelection()
        if selected_option == 0:
            self.utility_name = "NoUtility"
            self.utility_bool = False
        if selected_option == 1:
            self.utility_name = "FullUtility"
            self.utility_bool = True
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
        text = self.m_listBox1.GetString(index)
        hotkey = text.split(": ")[1].split()[0]
        hotkey_manager.remove_hotkey(hotkey)
        self.refresh_m_list_box()
        event.Skip()

    def refresh_m_list_box(self):
        hotkeys = hotkey_manager.get_all_hotkeys()
        self.m_listBox1.Clear()
        width = 20
        # pylint: disable=C0206:consider-using-dict-items
        for key in hotkeys:
            hotkey = hotkeys[key]
            utility_bool = hotkey['utility_bool']
            utility_str = ""
            hotkey_str = f"Hotkey: {key:<{width-15}}\t"
            weapon_str = f"Weapon: {hotkey['weaponName']:<{width}}\t" if len(
                hotkey['weaponName']) > 0 else f"{'':<{width}}\t\t"
            pistol_str = f"Pistol: {hotkey['pistolName']:<{width}}\t" if len(
                hotkey['pistolName']) > 0 else f"{'':<{width}}\t\t"
            shield_str = f"Shield: {hotkey['shieldName']:<{width}}\t"
            if utility_bool:
                utility_str = "Utility: FullUtility"
            else:
                utility_str = "Utility: NoUtility"
            hotkey_display_str = hotkey_str
            hotkey_display_str += weapon_str
            hotkey_display_str += pistol_str
            hotkey_display_str += shield_str
            hotkey_display_str += utility_str
            self.m_listBox1.Append(hotkey_display_str)


# pylint: disable=E1101:no-member
wx.SizerFlags.DisableConsistencyChecks()

app = wx.App()
frame = MyCustomFrame(None)
frame.Show(True)
app.MainLoop()
