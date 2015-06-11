import bottle

app = bottle.Bottle()

"""
Greeting Mechanism
"""
@app.route('/hello')
def hello():
    return 'Hello World!'

app.run(host='localhost', port=8080, debug=True)
