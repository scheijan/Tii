import os
import os.path

import cherrypy

from jinja2 import Environment, FileSystemLoader

import tii


class TiiServer(object):
    def __init__(self):
        self.jinjaEnv = Environment(loader=FileSystemLoader('../static/html'))

    @cherrypy.expose
    def index(self):
        template = self.jinjaEnv.get_template('index.html')
        return template.render()

    @cherrypy.expose
    def cards(self):
        template = self.jinjaEnv.get_template('cards.html')
        return template.render()

    @cherrypy.expose
    def game(self, p=2, r=20):
        p = int(p)
        r = int(r)
        g = tii.Game(p)

        for p in [x for x in g.players if not g.won]:
            for i in [i for i in range(0, r) if not g.won]:
                won = p.turn()
                if won:
                    break

        result = '<div class="center"><br/>'
        result += '<br/>'.join(g.gameState().split('\n'))
        result += '</div>'

        template = self.jinjaEnv.get_template('index.html')
        return template.render(content=result)


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
