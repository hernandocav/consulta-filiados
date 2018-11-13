from flask import Flask

from blueprints.filiados.app import filiados_blueprint

app = Flask('consultafiliados', static_folder='static', static_url_path='/static')
app.config.from_object('config')
app.register_blueprint(filiados_blueprint)

# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     root_dir = os.path.dirname(os.getcwd())
#     return send_from_directory(os.path.join(root_dir, 'static', 'js'),   filename) 

@app.route("/")
def index():
    """
    Pagina principal
    """
    return "Essa e a pagina principal"

if __name__ == 'consultafiliados':
    app.run(debug=True, use_reloader=True)
