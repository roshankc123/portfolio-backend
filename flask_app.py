from flask import * 
from OpenSSL import SSL
from flask_cors import CORS
import repos_list
from middleware import middleware 

app = Flask(__name__)
# or remove the origins field for allowing all origins
CORS(app, origins=['your_website'])

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

app.wsgi_app = middleware(app.wsgi_app)

@app.route('/')
def index():
    return 'success'

@app.route('/projects')
def projects():
    return repos_list.get_repos()

@app.route('/update')
def update():
    repos_list.update_repos()
    return ''

@app.route('/visitor')
def visitor():
    return open('count','r+').read()


if __name__ == "__main__":
    app.run('127.0.0.1', '8000' ,debug=True)