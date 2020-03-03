"""
test Debug
"""
#!/usr/bin/python3
from datetime import datetime


class WikiDebug:
    """This Class is just for wiki to debug python pracitice"""

    def __init__(self):
        print("wiki debug __init__")
        self.now = datetime.now()

    def get_timestamp(self):
        """get_timestamp"""
        self.now = datetime.now()
        timestamp = datetime.timestamp(self.now)  # after python 3.3
        mil_seconds = datetime.fromtimestamp(timestamp)
        print(mil_seconds)


def main():
    """main function"""
    d = WikiDebug()
    d.get_timestamp()
    d.get_timestamp()


if __name__ == '__main__':
    """run test in single file"""
    main()
