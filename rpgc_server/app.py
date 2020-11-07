from rpgc_server import app, lg
from rpgc_server.handlers.messagehandler import MessageHandler
from rpgc_server.handlers.roomhandler import RoomHandler
from rpgc_server.handlers.userhandler import UserHandler
from rpgc_server.handlers.presethandler import PresetHandler


# adding bp
app.register_blueprint(RoomHandler, url_prefix='/rooms')
app.register_blueprint(MessageHandler, url_prefix='/messages')
app.register_blueprint(UserHandler, url_prefix='/users')
app.register_blueprint(PresetHandler, url_prefix='/presets')


@app.route('/', methods=["GET"], defaults={'page': 'index'})
@app.route('/<page>', methods=["GET"])
# @auth.login_required
def index(page):
    return "It works!"
    # try:
    #     return render_template('%s.html' % page.replace('.html', ''))
    # except TemplateNotFound:
    #     abort(404)


# @app.route('/favicon.ico')
# def favicon():
#     return redirect(url_for('static', filename='favicon.ico'))
#

if __name__ == "__main__":
    logo = """
                _ _______        _     
     /\        | |__   __|      | |    
    /  \   _ __| | _| | ___  ___| |__  
   / /\ \ | '__| |/ / |/ _ \/ __| '_ \ 
  / ____ \| |  |   <| |  __/ (__| | | |
 /_/    \_\_|  |_|\_\_|\___|\___|_| |_|
                                       
                                       """
    lg.info(logo)
    lg.info('Server starting')
    app.run()
