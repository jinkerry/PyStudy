__author__ = 'jinfeng'

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Recieve get request...' + '<br>')
        print self.request
        code = self.get_argument('code')
        self.write('Code: ' + code)
        filehandler = open('code.txt', 'w')
        filehandler.write(code)
        filehandler.close()

application = tornado.web.Application([
    (r"/", MainHandler)
    ])

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()
