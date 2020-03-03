"""
testAccountService library
"""
#!/usr/bin/python3
# ConfigParser in python2
from configparser import ConfigParser, NoSectionError

class CustomConfigParser(ConfigParser):
    """ config parser for conf file """

    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, option_str):
        """ case sensitive  """
        return option_str

cf = CustomConfigParser()

cf.read("/etc/lightdm/lightdm.conf")

try:
    name = cf.get("SeatDefaults", "autologin-user")
    if name is not None:
        print("lucky %s, autologin next time!" % name)
except NoSectionError:
    print("No Section Error!")
except Exception as error_reason:
    print("failed: %s" % error_reason)
