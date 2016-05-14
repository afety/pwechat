from tornado import  web
from hashlib import sha1

__author__ = 'tanghan'

TOKEN = "weixin"

class MainHandler(web.RequestHandler):
    def get(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        s = [timestamp, nonce, TOKEN]
        s.sort()
        s = ''.join(s)
        if sha1(s).hexdigest == signature:
            self.write(echostr)

class StoryHandler(web.RequestHandler):
    def get(self,storyid):
        self.write("You requestd the story "+storyid)