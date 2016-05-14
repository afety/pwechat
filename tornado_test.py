#coding:utf-8
#file is used to use tornado
#time : 2016.05.14
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define,options
from BaseClass import MainHandler, StoryHandler

__author__ = 'tanghan'

setting = {'debug':True}
define("port", default=8888, help="run on the given port", type=int)


if __name__ =="__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application(
        [(r"/",MainHandler),
        (r"/story/([0-9]+)", StoryHandler),]
    ,**setting)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
