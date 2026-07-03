import psutil
import subprocess
import time
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

CHECK_INTERVAL = 10


def running(script):

    for p in psutil.process_iter(['cmdline']):

        try:

            cmd = p.info["cmdline"]

            if cmd and script in " ".join(cmd):
                return True

        except:
            pass

    return False


while True:

    if not running("main.py"):

        print("main.py mati. Restart...")

        subprocess.Popen(
            [PYTHON, os.path.join(BASE, "main.py")],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    if not running("history_writer.py"):

        print("history_writer.py mati. Restart...")

        subprocess.Popen(
            [PYTHON, os.path.join(BASE, "history_writer.py")],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )

    time.sleep(CHECK_INTERVAL)
