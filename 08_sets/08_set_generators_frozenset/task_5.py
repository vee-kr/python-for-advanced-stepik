files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG',
         'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
photos = {file.lower() for file in files if file.lower().endswith(".png")}
print(*sorted(photos))
