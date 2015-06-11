import bottle

app = bottle.Bottle()

"""
Shout Mechanism
"""
@post('/shout')
def shout_post():



"""
Login Mechanism
"""
def check_login(username, password):
    """
    return True if the last 4 chars matches the password.
    """
    return username[-4:] == password


@app.get('/login')
def login_get():
    return """
        <form action="/login" method="post">
            Username: <input name="username" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    """

@app.post('/login')
def login_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_login(username, password):
        response.set_cookie('username', username)
        return "<p>Login Successfully.</p>"
    else:
        return "<p>failed.</p>"

"""
Greeting Mechanism
"""
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Stranger'):
    username = request.get_cookie('username')
    
    if username:
        return 'Hello, %s.' % username
    else:
        return 'Hello, %s.' % name

app.run(host='localhost', port=8080, debug=True)
