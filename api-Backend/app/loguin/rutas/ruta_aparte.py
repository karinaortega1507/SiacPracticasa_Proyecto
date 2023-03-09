from app.login import bp
from flask_cors import cross_origin


@bp.route('/test_aparte')
@cross_origin()
def aparte():
    return "esto es una prueba de ruta aparte"#render_template('login/index.html')