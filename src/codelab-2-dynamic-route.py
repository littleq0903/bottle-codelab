import bottle

app = bottle.Bottle()

"""
Greeting Mechanism
"""
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Stranger'):
    return 'Hello, %s.' % name

app.run(host='localhost', port=8080, debug=True)
