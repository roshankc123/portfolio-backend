from typing import Any


class middleware():
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):
        self.count()
        return self.app(environ, start_response)
    
    def count(app):
        try:
            c = open('count','r+').read()
            if c == '':
                c = 1
        except:
            open('count', 'w')
            c = 1

        c = int(c)
        print(c)
        open('count','w').write(str(c + 1))
        return app