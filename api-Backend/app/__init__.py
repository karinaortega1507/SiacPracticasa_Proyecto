from flask import Flask

from config import Config
from flask_jwt_extended import JWTManager
from flask import jsonify

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize Flask extensions here

    from app.extensions import db
    db.init_app(app)

    from app.extensions import ma
    ma.init_app(app)

    from app.extensions import cors
    cors.init_app(app,resources={r"/*": {"origins": "*", "headers":["Content-Type", "Authorization"]}})

    jwt = JWTManager(app)
    # --------------------------------------

    # Register blueprints here

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.login import bp as login_bp
    app.register_blueprint(login_bp, url_prefix='/login')

    from app.productos import bp as productos_bp
    app.register_blueprint(productos_bp, url_prefix='/productos')

    from app.proformas import bp as proformas_bp
    app.register_blueprint(proformas_bp, url_prefix='/proformas')
    # sdfvsgedg

    # --------------------------------------

    # Register error handlers here
    @app.errorhandler(404)
    def page_not_found(e):
        return '<h1>404</h1><p>The resource could not be found.</p>', 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return '<h1>500</h1><p>An internal error occurred.</p>', 500



    @jwt.expired_token_loader
    def handle_jwt_error(jwt_header, jwt_payload):
        
        return jsonify({'err': {
            'msg':"El token ha caducado"
        }}), 401

    @jwt.invalid_token_loader
    def handle_jwt_error(err):
        return jsonify({'err': {
            'msg':"El token es inválido"
        }}), 401

    
    # --------------------------------------
    # test page
    @app.route('/test/')
    def test_page():
        return '<h1>TEST</h1>'

    return app