from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.set_rotation(r=90)

from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            sense.show_message(data['text'], text_colour=(0,0,255), scroll_speed=0.04)
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
# stream.statuses.filter(track='raspberry pi')
stream.statuses.filter(track='@dallascowboys')
