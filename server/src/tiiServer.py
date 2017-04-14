import os
import os.path

import cherrypy

import tii


class TiiServer(object):
    @cherrypy.expose
    def index(self):
        return """<html>
         <head profile="http://www.w3.org/2005/10/profile">
         <link rel="shortcut icon" type="image/png" href="/static/favicon.png"/>
          <body>
            <p>Hello World!</p>
          </body>
        </html>"""

    @cherrypy.expose
    def game(self, p=2):
        g = tii.Game(p)

        for p in [p for p in g.players if not g.won]:
            for i in [i for i in range(0, 20) if not g.won]:
                won = p.turn()
                if won:
                    break

        return g.gameState()


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
