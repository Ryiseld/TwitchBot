import utils
import time

# Function: display_time
# Displays the current time
#   Parameters:
#       s - the socket in which to perform the command
def display_time(s):
    utils.chat(s, "It is currently " + time.strftime("%I:%M %p %Z on %A, %B, %d, %Y."))

def display_social(s):
    utils.chat(s, "Twitter: twitter.com/ryiseld | YouTube: youtube.com/ryiseld")
    utils.chat(s, "Follow me on Twitter and subscribe to my YouTube channel to support me! :)")