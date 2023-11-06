from pywinauto.application import Application
from pywinauto import Desktop

BUTTON_NINE = 'num9button'
WAIT_TIMEOUT = 10

app = Application(backend="uia").start("calc.exe")
dlg = Desktop(backend="uia").Calculator

dlg.wait('visible', WAIT_TIMEOUT)
dlg.child_window(auto_id=BUTTON_NINE).click_input
