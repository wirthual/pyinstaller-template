import json
import os
import PySimpleGUI as sg


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__=='__main__':
   file_path = resource_path(os.path.join("additional_data","extra_data.json"))

   with open(file_path) as f:
     data = json.load(f)

   sg.theme('DarkAmber')   # Add a touch of color
   # All the stuff inside your window.
   layout = [  [sg.Text(data['key'])],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

   # Create the Window
   window = sg.Window('Window Title', layout)
   # Event Loop to process "events" and get the "values" of the inputs
   while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

   window.close()
