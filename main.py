import json
import os


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

   print(data['key'])
