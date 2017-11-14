from flask import Flask
import views
from config import *

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

@app.route('/test')  
def main():
    views.findbynameanduf("SÔNIA", "ce")
    return self.render_response('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static', 'js'),   filename) 

@app.route('/consultar') 
def consultar():
    views.consultar()
    return self.render_response('index.html')

@app.route('/download')
def download():
    views.download()
    return self.render_response('index.html')

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
