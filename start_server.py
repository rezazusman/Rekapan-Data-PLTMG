import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

python = sys.executable

subprocess.Popen(
    [python, os.path.join(BASE_DIR, "main.py")],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)

subprocess.Popen(
    [python, os.path.join(BASE_DIR, "history_writer.py")],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)

print("PLTMG AI Server Started")
