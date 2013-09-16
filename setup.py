import os
import sys

from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

zip_includes = [(os.path.abspath('freesansbold.ttf'), 'pygame/freesansbold.ttf')]
options = {
    'zip_includes': zip_includes,
}

setup(
    name="Definitely Don't Find The Kitty",
    version='0.5',
    description='Do your best not to find the kitty',
    options={'build_exe': options},
    executables=[Executable('main.py', base=base)]
)

