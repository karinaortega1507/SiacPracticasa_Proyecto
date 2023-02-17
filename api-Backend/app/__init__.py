from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    from app.extensions import db
    db.init_app(app)

    from app.extensions import ma
    ma.init_app(app)

    # --------------------------------------

    # Register blueprints here

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.loguin import bp as loguin_bp
    app.register_blueprint(loguin_bp, url_prefix='/loguin')

    # sdfvsgedg

    # --------------------------------------

    # Register error handlers here
    @app.errorhandler(404)
    def page_not_found(e):
        return '<h1>404</h1><p>The resource could not be found.</p>', 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return '<h1>500</h1><p>An internal error occurred.</p>', 500
    
    # --------------------------------------
    # test page
    @app.route('/test/')
    def test_page():
        return '<h1>TEST</h1>'

    return app