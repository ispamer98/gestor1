from main import app

def application(environ, start_response):
    return app(environ, start_response)
