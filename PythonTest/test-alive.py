import os
import subprocess
import time
import signal

get_sesssion_cmd = 'pgrep -U {} -f gedit'.format(os.getuid())
session_pid = subprocess.check_output(get_sesssion_cmd, shell=True).decode('utf-8').split()[0]
while True:
    try:
        os.kill(int(session_pid), 0)
    except ProcessLookupError:
        print('Stop with gnome-session-binary')
        os.kill(os.getpid(), signal.SIGTERM)
    else:
        print("wait..........")
        time.sleep(3)
