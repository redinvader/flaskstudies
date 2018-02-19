from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'None'


@app.route('/index')
def index2():
    return ''' 
        <h1>Index page</h1>
        <hr/>
        <a href='hello' > goto hello </a>
    '''


@app.route('/hello')
def hello_world():
    return 'Hello nasty world<hr/>'


@app.route('/user/<username>')
def show_user_profile( username ):
    return 'User %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d'%post_id

if __name__=='__main__':
    app.run( port=5000, debug=True)