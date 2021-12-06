import os
import IPython
import random

early_setup="""
chmod +x 7zz
chmod +x ffmpeg
apt install mediainfo
apt install python3-libtorrent
7z x All_Needy_Fonts.7z -o/usr/share/fonts/ -y
rm /usr/share/fonts/pHalls*
fc-cache -f
touch /content/INSTALLED
"""

logger_code="""
import logging
import sys
logging.basicConfig(filename="debug.log",
                            filemode='a',
                            format='%(asctime)s: %(message)s',
                            datefmt='%y/%m/%d  %H:%M:%S',
                            level=logging.INFO)

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.WARNING)
logging.getLogger('').addHandler(console)
"""

def install_essentials():
    with open("/usr/lib/python3.7/logging/__init__.py", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write("from pytz import timezone\nfrom datetime import datetime\n" + content)
    with open("/content/early_setup.sh","w") as f:
        f.write(early_setup)
    os.system("chmod +x /content/early_setup.sh")
    o=IPython.get_ipython().run_cell("!./early_setup.sh")
    IPython.display.clear_output()
    exec(logger_code)
    with open("/root/.ipython/profile_default/startup/startup.py","a") as f:
        f.write(logger_code)


