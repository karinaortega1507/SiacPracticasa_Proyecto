from app.loguin import bp

@bp.route('/test_aparte')
def aparte():
    return "esto es una prueba de ruta aparte"#render_template('loguin/index.html')