import subprocess
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

programs = [
    "main.py",
    "history_writer.py",
    "watchdog.py"
]

for p in programs:

    subprocess.Popen(
        [PYTHON, os.path.join(BASE, p)],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

print("PLTMG AI Server Started")
