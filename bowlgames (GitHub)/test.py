# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Coming June 2015: Lee Family College Bowl"]
