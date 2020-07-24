#!/usr/bin/python3

import socket
import time


def connect_check(server_url, check_interval, check_time, check_timeout):
    """Check server connect availiable

    server_url: Server url path
    check_interval: from this to next check interval
    check_time: check time for called
    check_timeout: socket timeout

    return: True if server_url running or return False
    """
    if not server_url or (not server_url.startswith("http://")):
        print("server url error, lost info")
        return False

    if check_time < 1 or check_interval < 1 or check_timeout < 1:
        print("check argument failed, just quit")
        return False

    success = False
    url_info = server_url.split("://")[1].split(":")
    url_info_len = len(url_info)
    if url_info_len == 1:
        ip_addr = url_info[0]
        port = 80
    else:
        ip_addr = url_info[0]
        port = int(url_info[1])

    index = 0
    for index in range(0, check_time):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(check_timeout)
        try:
            sk.connect((ip_addr, port))
            success = True
        except Exception as err:
            print(err)
            index = index + 1
        sk.close()
        if success:
            break
        time.sleep(check_interval)

    return success

# print("TestSocket3:")
# res = connect_check("", 2, 4, 10)
# print("result: %d" % res)

# print("TestSocket2")
# res = connect_check("http://192.168.1.1:8009", 2, 1, 1)
# print("result: %d" % res)

# print("TestSocket3")
# res = connect_check("http://127.0.0.1:8000", 3, 5, 3)
# print("result: %d" % res)
