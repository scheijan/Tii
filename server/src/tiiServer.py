import os
import os.path

import cherrypy

from jinja2 import Environment, FileSystemLoader

import coloredlogs

import tii

cherrypy.log.error_log.propagate = False
cherrypy.log.access_log.propagate = False


class TiiServer(object):
    def __init__(self):
        self.jinjaEnv = Environment(loader=FileSystemLoader('../static/html'))
        self.game = tii.Game(2)
        coloredlogs.install(level='INFO', fmt='[%(asctime)s] %(levelname)s %(message)s', datefmt='%d/%b/%Y:%I:%M:%S')

    @cherrypy.expose
    def index(self):
        template = self.jinjaEnv.get_template('index.html')
        return template.render()

    @cherrypy.expose
    def board(self, n=0):
        template = self.jinjaEnv.get_template('board.html')
        return template.render(n=n)

    @cherrypy.expose
    def play(self, p=2, r=10):
        p = int(p)
        r = int(r)
        self.game = tii.Game(p)

        for i in [i for i in range(0, r) if not self.game.won]:
            for player in [x for x in self.game.players if not self.game.won]:
                won = player.turn()
                if won:
                    break

        result = '<div class="center"><br/>'
        result += '<br/>'.join(self.game.gameState().split('\n'))
        result += '</div>'

        template = self.jinjaEnv.get_template('index.html')
        return template.render(content=result)

    @cherrypy.expose
    def state(self, n=1):
        return self.game.playerState(int(n))


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '../static'
        }
    }
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(TiiServer(), '/', conf)
