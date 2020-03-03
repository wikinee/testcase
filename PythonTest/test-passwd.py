"""
Test
"""
#!/usr/bin/python3

import pexpect
import gi
from gi.repository import GObject
import threading


class TestPexpectLine(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        is_pass = False
        try:
            envtest = {
                "LC_ALL": "C"
            };
            child = pexpect.spawn("/usr/bin/passwd", timeout=1, env=envtest)
            # child.logfile = open("mylog", "w")
            # child.logfile_send=sys.stdout
            child.expect("(current).*:")
            child.sendline("12345678")
            child.expect("Enter new UNIX.*:")
        except pexpect.EOF:
            print("except:EOF is_pass:%d" % is_pass)
        except pexpect.TIMEOUT:
            print("except:TIMEOUT is_pass:%d" % is_pass)
        else:
            is_pass = True
            child.close()
            print("child close;is_pass:%d" % is_pass)


def main():
    t = TestPexpectLine()
    t.start()


if __name__ == "__main__":
    main()
