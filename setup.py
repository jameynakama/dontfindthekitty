import sys

from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name="Definitely Don't Find The Kitty",
    version='0.5',
    description='Do your best not to find the kitty',
    options={},
    executables=[Executable('src/main.py', base=base)]
)
