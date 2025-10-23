def configure_all(app):
    configure_routes


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route)


def configure_db(app):
    pass