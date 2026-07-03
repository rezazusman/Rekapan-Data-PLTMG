import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

print("="*50)
print("PLTMG AI SERVER")
print("="*50)

subprocess.Popen(
    [PYTHON, os.path.join(BASE_DIR, "main.py")],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)

subprocess.Popen(
    [PYTHON, os.path.join(BASE_DIR, "history_writer.py")],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)

print("Server berhasil dijalankan.")
