__author__ = 'jinfeng'

import tornado.ioloop
import tornado.web
from xml.etree import ElementTree
import os

def read_xml(text):
    root = ElementTree.fromstring(text)
    lst_node = root.getiterator("command")
    xml = []
    for node in lst_node:
        xml.append(node.text)
    return xml

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        xml = read_xml(open("res/meta/cmd.xml").read())
        self.write("Meta Commands" + "<br>")
        for strxml in xml:
            self.write(strxml + "<br>")

class RunCommand(tornado.web.RequestHandler):
    def get(self, command_id):
        self.write("Combined Commands: " + command_id + "<br>")
        xml = read_xml(open("res/combined/" + command_id + ".xml").read())
        for strxml in xml:
            self.write(strxml + "<br>")
            os.system(strxml)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/run/([0-9]+)", RunCommand),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()