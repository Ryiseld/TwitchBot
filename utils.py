import cfg
import json
import urllib2
import thread
from time import sleep

# Function: chat
# Send a chat message to the server
#   Parameters:
#       sock - the socket over which to send the message
#       msg  - the message to send
def chat(sock, msg):
    sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg))

# Function: ban
# Ban a user from the channel
#   Parameters:
#       sock - the socket over which to send the ban command
#       user - the user to ban
def ban(sock, user):
    chat(sock, ".ban {}".format(user))

# Function: timeout
# Timeout a user for a set period of time
#   Parameters:
#       sock - the socket over which to send the timeout command
#       user - the user to be timed out
#       seconds - the length of the timeout in seconds (default 600)
def timeout(sock, user, seconds = 600):
    chat(sock, ".timeout {}".format(user, seconds))

# Function: thread_fill_op_list
# In a separate thread, fill up the op list
def thread_fill_op_list():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/ryiseld/chatters"
            req = urllib2.Request(url, headers = {"accept": "*/*"})
            response = urllib2.urlopen(req).read()

            # If the page loaded successfully and we didn't get a 502 Bad Gateway
            if response.find("502 Bad Gateway") == -1:
                cfg.oplist.clear()
                data = json.loads(response)

                for p in data["chatters"]["moderators"]:
                    cfg.oplist[p] = "mod"

                for p in data["chatters"]["global_mods"]:
                    cfg.oplist[p] = "global_mod"

                for p in data["chatters"]["admins"]:
                    cfg.oplist[p] = "admin"

                for p in data["chatters"]["staff"]:
                    cfg.oplist[p] = "staff"

        except:
            'do nothing'

        sleep(5)

# Function: is_op
# Check if the user is an op
#   Parameters:
#       user - the user to check
def is_op(user):
    return user in cfg.oplist