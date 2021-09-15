"""
Credited to https://stackoverflow.com/a/41318195, https://apple.stackexchange.com/a/115373
"""

import os
import subprocess

CMD = """
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
"""


def notify(title, text='Restocked!! Go and check', sound='Funk'):
    subprocess.call(['osascript', '-e', CMD, title, text])
    os.system(f'say "Check notification!"')
    os.system(f'afplay /System/Library/Sounds/{sound}.aiff')
