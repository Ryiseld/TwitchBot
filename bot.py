import cfg
import utils
import custom_commands

import socket
import re
import time
from time import sleep
import thread


def main():
    # Networking
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    utils.chat(s, "Hi everyone!")

    # Run the fill_op_list_function on a separate thread
    thread.start_new(utils.thread_fill_op_list, ())

    while True:
        response = s.recv(1024).decode("utf-8")

        # If the message is a PING, send back a PONG
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)
            print(response)

            # Custom commands
            if message.strip() == "!time":
                custom_commands.display_time(s)

            if message.strip() == "!messages":
                custom_commands.display_social(s)

        sleep(1)

if __name__ == "__main__":
    main()