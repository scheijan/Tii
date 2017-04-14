import os
import os.path

import cherrypy

import tii


class TiiServer(object):
    @cherrypy.expose
    def index(self):
        return open('../static/html/index.html').read()

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
        result = '<p>'
        result += '<br/>'.join(g.gameState().split('\n'))
        result += '</p>'

        return result


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
    cherrypy.quickstart(TiiServer(), '/', conf)
