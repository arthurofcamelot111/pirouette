'''graphical user interface'''

import gui

# --- event handlers ---

def greeting(evt):
    import wx, sys
    gui.alert('\n'.join([wx.version(), sys.version]), "gui2py hello world!")

# --- gui2py designer generated code starts ---

with gui.Window(title='gui2py minimal app', resizable=True, height='496px',
                width='400px', image='', name='mywin'):
    b = gui.Button(label='Click me!', name='button', default=True)

# --- gui2py designer generated code ends ---

mywin = gui.get("mywin")

# assign the event handlers

mywin['button'].onclick = greeting

if __name__ == '__main__':
    mywin.show()
    gui.main_loop()
